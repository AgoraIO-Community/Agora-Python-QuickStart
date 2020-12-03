from PIL import Image
import numpy as np
import face_recognition
from keras.models import load_model
import cv2
import os
import time

counter = 0
face_names = []
face_emotions = []
genders = []
ages = []


class faceRecognition():

    def __init__(self):
        print("============loading face database============")
        tic = time.time()
        db_path = "database"
        self.known_face_encodings = []
        self.known_face_names = []
        if os.path.isdir(db_path):
            for r, d, f in os.walk(db_path):
                for file in f:
                    if (".jpg" in file) or (".jpeg" in file) or (".png" in file) or (".JPEG" in file):
                        img_path = r + "/" + file
                        img = face_recognition.load_image_file(img_path)
                        if len(face_recognition.face_encodings(img)) == 0:
                            print("WARNING: There is no face in " + str(file) + ".")
                        else:
                            img_face_encoding = face_recognition.face_encodings(img)[0]
                            self.known_face_encodings.append(img_face_encoding)
                            self.known_face_names.append(file[: file.find(".")])
        if len(self.known_face_names) == 0:
            print("WARNING: There is no image in this path ( ", db_path, ") . Face recognition will not be performed.")
        else:
            print(self.known_face_names)

        toc = time.time()
        print("============finish loading face database in {} seconds============".format(round((toc - tic), 1)))

        # Initialize some variables
        print("============loading model============")
        tic = time.time()
        self.face_locations = []
        self.face_encodings = []
        self.face_names = []
        self.emotion_dict = {'Angry': 0, 'Sad': 5, 'Neutral': 4, 'Disgust': 1, 'Surprise': 6, 'Fear': 2, 'Happy': 3}
        print("============loading model 1============")
        self.model = load_model("model/model_v6_23.hdf5")
        print("============finish loading model 1============")
        print("============loading model 2============")
        self.model_enhanced = load_model("model/weights.28-3.73.hdf5")
        print("============finish loading model 2============")
        toc = time.time()
        print("============finish loading model in {} seconds============".format(round((toc - tic), 1)))

    def predict_emotion(self, face_image):
        face_image_reshape = cv2.resize(face_image, (48, 48))
        face_image_reshape = cv2.cvtColor(face_image_reshape, cv2.COLOR_BGR2GRAY)
        face_image_reshape = np.reshape(face_image_reshape,
                                        [1, face_image_reshape.shape[0], face_image_reshape.shape[1], 1])
        predicted_class = np.argmax(self.model.predict(face_image_reshape))
        label_map = dict((v, k) for k, v in self.emotion_dict.items())
        predicted_label = label_map[predicted_class]
        return predicted_label

    def predict_gender_age(self, face_image):
        result = self.model_enhanced.predict(cv2.resize(face_image, (64, 64)).reshape(-1, 64, 64, 3))
        return result

    def frame_process(self, im, gender_age=False):
        """
        Input
        im: the raw input frame in PIL.image
        adaptive_size: whether use the full size or the adaptive size (use adaptive size as default)
        gender_age: whether predict the gender and age features (not predict as default)
        Output
        the processed frame fitting the required size in PIL.image
        """
        global counter, face_names, face_emotions, genders, ages

        frame = cv2.cvtColor(np.asarray(im), cv2.COLOR_RGB2BGR)

        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        if True:
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            if counter == 0:
                for i in range(len(face_encodings)):
                    matches = face_recognition.compare_faces(self.known_face_encodings, face_encodings[i])
                    name = "Unknown"

                    face_distances = face_recognition.face_distance(self.known_face_encodings, face_encodings[i])
                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                        name = self.known_face_names[best_match_index]

                    face_names.append(name)
                    top, right, bottom, left = face_locations[i]
                    face_image = rgb_small_frame[top:bottom, left:right]
                    face_emotions.append(self.predict_emotion(face_image))
                    if gender_age:
                        res = self.predict_gender_age(face_image)
                        genders.append("M" if np.argmax(res[0], axis=1)[0] == 1 else "F")
                        ages.append(np.argmax(res[1], axis=1)[0] - 5)
                    else:
                        genders.append("N/A")
                        ages.append(-1)

        face_names_return = face_names
        face_emotions_return = face_emotions
        genders_return = genders
        ages_return = ages
        if counter < 15:
            counter += 1
        else:
            counter = 0
            face_names = []
            face_emotions = []
            genders = []
            ages = []

        return [[[f_l[i] * 4 for i in range(len(f_l))] for f_l in face_locations], face_names_return,
                face_emotions_return, ages_return, genders_return]
