# Agora Face Recognition Demo

*[中文](Readme.zh.md) | English*

This is a python demo for Agora 1-to-1 video call extended a new feature -- Real Time Face Recognition. It supports for face recognition and emotion, age and gender detection.



## Installation

### Requirements

- Python 3.6+
- macOS (Windows not officially supported due to the requirement of dlib required by face_recognition, but might work)
- Xcode (macOS)
- Visual Studio 2017+ with C++ (Windows)

### Dependencies

- Agora Python SDK
- numpy
- OpenCV (headless)
- TensorFlow
- Keras
- PyQt5
- face_recognition

### Installation Options:

We encourage you to use [Anaconda](https://www.anaconda.com/) to [create a new separate environment](https://docs.anaconda.com/anaconda/navigator/tutorials/manage-environments/#id3) other than using your existed Python to avoid possible environmental conflicts to your other projects. After creating a new environment, switch from base to your new environment:

```bash
conda activate [your-env-name]
```

#### 1. Install all required packages via PyPI (except face_recognition)

```bash
pip3 install agora-python-sdk numpy pyqt5 opencv-python-headless pillow keras tensorflow
```

⚠️The related package, h5py, that keras calls may cause an error due to the upgrade of h5py package. If you meet h5py related error when running our demo, please uninstall the current h5py `pip3 uninstall h5py` and install an earlier version `pip install h5py==2.10.0`.

#### 2. Install face_recognition

*Adapted from [here](https://github.com/ageitgey/face_recognition/blob/master/README.md#installation).*

##### Installing on macOS

**First, make sure you have cmake installed:**

We recommend you to use [Homebrew](https://brew.sh/) on macOS: `brew install cmake`.

**Then, make sure you have dlib already installed with Python bindings:**

- [How to install dlib from source on macOS or Ubuntu](https://gist.github.com/ageitgey/629d75c1baac34dfa5ca2a1928a7aeaf)

**Finally, install this module from PyPI using pip:**

```bash
pip3 install face_recognition
```

##### Installing on Windows

While Windows has not been officially supported yet, helpful users have posted instructions on how to install this library:

- [@masoudr's Windows 10 installation guide (dlib + face_recognition)](https://github.com/ageitgey/face_recognition/issues/175#issue-257710508)

or **installing a pre-configured Virtual Machine image**:

- [Download the pre-configured VM image](https://medium.com/@ageitgey/try-deep-learning-in-python-now-with-a-fully-pre-configured-vm-1d97d4c3e9b) (for VMware Player or VirtualBox).

## Run Demo

#### 1. Download the required pre-trained models

Download the following 2 pre-trained models:

- [emotion_detector_model](https://github.com/priya-dwivedi/face_and_emotion_detection/blob/master/emotion_detector_models/model_v6_23.hdf5)
- [age_gender_detection_model](https://github.com/yu4u/age-gender-estimation/releases/download/v0.5/weights.28-3.73.hdf5)

Create an empty folder called `model` and move the models into the folder via the following directory structure:

```
face_recognition
├── model
│   ├── model_v6_23.hdf5
│   ├── weights.28-3.73.hdf5
```

#### 2. (Optional) Add some face photos

Create an empty folder called `database` and add some face photos via the following directory structure. For each person, create a seperate folder with his or her name.

```
face_recognition
├── database
│   ├── Alice
│   │   ├── Alice1.jpg
│   │   ├── Alice2.jpg
│   ├── Bob
│   │   ├── Bob.jpg
```

#### 3. Run Demo

Go to `face_recognition` folder, run `python3 face_recog.py`.

*If you do not have an App ID, see Appendix.*



## Appendix

### Create an Account and Obtain an App ID

To use our SDK, you must obtain an app ID: 

1. Create a developer account at [agora.io](https://dashboard.agora.io/signin/). Once you finish the sign-up process, you are redirected to the dashboard.
2. Navigate in the dashboard tree on the left to **Projects** > **Project List**.
3. Copy the app ID that you obtained from the dashboard into a text file. You will use it when you run demo (there is an input box in our GUI demo).
