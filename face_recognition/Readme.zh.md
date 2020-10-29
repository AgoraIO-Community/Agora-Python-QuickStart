# Agora人脸识别示例

*[English](README.md) | 中文*

本示例在一对一视频电话的基础上增加了实时人脸识别的特性。它支持人脸识别、表情、年龄和性别预测。



## 安装

### 运行环境

- Python 3.6+
- macOS （face_recognition所依赖的dlib目前对Windows尚未正式支持，Windows平台不能保证完美支持）
- Xcode (macOS)
- Visual Studio 2017+，需要添加C++支持 (Windows)

### 依赖包

- Agora Python SDK
- numpy
- OpenCV (headless)
- Keras
- PyQt5
- face_recognition

### 安装步骤：

您可以使用现有的Python3，但建议安装[Anaconda](https://www.anaconda.com/)并[创建一个独立的环境](https://docs.anaconda.com/anaconda/navigator/tutorials/manage-environments/#id3)，这样可以避免本示例所使用的依赖包不会对您其他的项目产生冲突。在创建全新的环境后，从base切换至您新创建的环境：

```bash
conda activate [your-env-name]
```

#### 1. 通过PyPI安装依赖包（除face_recognition外）

```bash
pip3 install agora-python-sdk numpy pyqt5 opencv-python-headless pillow keras
```

#### 2. 安装face_recognition

*本小节是从[这里](https://github.com/ageitgey/face_recognition/blob/master/README.md#installation)翻译而来。*

##### 在macOS上安装

**首先，确保您已安装cmake：**

推荐使用[Homebrew](https://brew.sh/)进行安装：`brew install cmake`。

**其次，确保您已安装dlib并与Python相关联：**

- [如何用源码在macOS或Ubuntu上安装dlib](https://gist.github.com/ageitgey/629d75c1baac34dfa5ca2a1928a7aeaf)

**最后，用pip从PyPI上安装依赖包：**

```bash
pip3 install face_recognition
```

##### 在Windows上安装

虽然Windows目前还未正式支持，热心的网友提供了一些安装指南：

- [@masoudr's Windows 10 installation guide (dlib + face_recognition)](https://github.com/ageitgey/face_recognition/issues/175#issue-257710508)

或者**您也可以使用预配置好的虚拟机镜像**：

- [从这里下载预配置的虚拟机镜像](https://medium.com/@ageitgey/try-deep-learning-in-python-now-with-a-fully-pre-configured-vm-1d97d4c3e9b) （支持VMware Player和VirtualBox）。

## 运行示例

#### 1. 下载预训练好的模型

从以下仓库下载预训练好的模型：

- [emotion_detector_model](https://github.com/priya-dwivedi/face_and_emotion_detection/blob/master/emotion_detector_models/model_v6_23.hdf5)
- [age_gender_detection_model](https://github.com/yu4u/age-gender-estimation/releases/download/v0.5/weights.28-3.73.hdf5)

根据以下文件夹结构，在仓库根目录创建`model`文件夹，并将模型复制到其中。

```
face_recognition
├── model
│   ├── model_v6_23.hdf5
│   ├── weights.28-3.73.hdf5
```

#### 2. （可选）将一些现有的人脸照片根据以下数据结构添加

被添加的人脸照片将被读取和识别。例如若您将您自己的照片添加在其中，在您运行示例时，您的人脸将被识别并与您的名字对应。

根据以下文件夹结构，在仓库根目录创建`database`文件夹，并在其中为每一个人创建一个以其名字命名的文件夹，并把照片放入对应文件夹中。

```
face_recognition
├── database
│   ├── 张三
│   │   ├── 张三1.jpg
│   │   ├── 张三2.jpg
│   ├── 李四
│   │   ├── 李四1.jpg
```

#### 3. 运行示例

前往`face_recognition`目录，运行命令`python3 face_recog.py`。

*如您还未获取App ID，您可以查看附录。*



## 附录

### 创建Agora账户并获取App ID

如果想要使用我们的SDK，您需要先获得一个App ID：

1. 在[agora.io](https://dashboard.agora.io/signin/)中注册一个账号。当您完成注册后，您将被链接至控制台。
2. 在控制台左侧点击**Projects** > **Project List**。
3. 请将您从控制台中获取的App ID保存，您将会在调用SDK时使用。