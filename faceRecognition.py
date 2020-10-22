from PIL import Image
import numpy as np
import face_recognition
from keras.models import load_model
import cv2
import os
import time


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

    def frame_process(self, im, width, height, adaptive_size=True, gender_age=False):
        """
        Input
        im: the raw input frame in PIL.image
        adaptive_size: whether use the full size or the adaptive size (use adaptive size as default)
        gender_age: whether predict the gender and age features (not predict as default)
        Output
        the processed frame fitting the required size in PIL.image
        """
        frame = cv2.cvtColor(np.asarray(im), cv2.COLOR_RGB2BGR)

        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        if True:
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            face_emotions = []
            genders = []
            ages = []
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
                    ages.append(np.argmax(res[1], axis=1)[0] - 10)
                else:
                    genders.append("N/A")
                    ages.append(-1)

        # Render output frame
        if not adaptive_size:
            scale = 469 / width if width > height else 349 / height
        else:
            scale = 349 / height if width > height else 469 / width

        frame_output = cv2.resize(frame, (0, 0), fx=scale, fy=scale)
        for (top, right, bottom, left), name, emotion, gender, age in zip(face_locations, face_names, face_emotions,
                                                                          genders, ages):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= int(4 * scale)
            right *= int(4 * scale)
            bottom *= int(4 * scale)
            left *= int(4 * scale)

            # Draw a box around the face
            cv2.rectangle(frame_output, (left, top), (right, bottom), (0, 0, 255), int(2 * scale), 1)

            # Draw a label with a name below the face
            cv2.rectangle(frame_output, (left, bottom - int(40 * scale)), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            if gender != "N/A" or age != -1:
                cv2.putText(frame_output, gender + "-" + str(age), (left + int(6 * scale), bottom - int(25 * scale)),
                            font, 0.7 * scale, (255, 255, 255), 1)
            cv2.putText(frame_output, name + "-" + emotion, (left + int(6 * scale), bottom - int(6 * scale)), font,
                        0.7 * scale, (255, 255, 255), 1)

        im_processed = Image.fromarray(cv2.cvtColor(frame_output, cv2.COLOR_BGR2RGB))
        return im_processed
