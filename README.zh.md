# Agora Python Tensorflow快速入门
Other languages： [English](https://github.com/AgoraIO-Community/Agora-Python-Tensorflow-Demo)

本教程介绍如何使用Python集成Tensorflow并使用Agora构建示例应用程序。

## 所需环境
* Python 3.6

* Tensorflow >= 1.12

* opencv-python

* pillow

## 主要功能
* 加入通话和离开通话；

* 识别画面物体；

## 创建一个帐户并获取一个App ID
### 要构建和运行示例应用程序，请首先获取Agora App ID：

* 在agora.io创建开发人员帐户。完成注册过程后，您将被重定向到仪表板页面

* 在左侧的仪表板树中导航到项目 > 项目列表

* 将从仪表板获取的App ID复制到文本文件中。您将在启动应用程序时用到它

## 编译指南
* 下载 [Python SDK Demo](https://github.com/AgoraIO-Community/Agora-Python-SDK) 

* 若是 Windows，复制.pyd and .dll文件到本文件夹根目录；若是IOS，复制.so文件到本文件夹根目录

* 下载 [Tensorflow模型](https://github.com/tensorflow/models),然后把 object_detection 文件复制.到本文件夹根目录

* 安装 Protobuf。然后运行： protoc object_detection/protos/*.proto --python_out=.

* 从这里下载预先训练的模型([下载链接](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md))

* 推荐使用 ssd_mobilenet_v1_coco 和 ssdlite_mobilenet_v2_coco，因为他们相对运行较快

* 提取 frozen graph,命令行运行：python extractGraph.py --model_file='FILE_NAME_OF_YOUR_MODEL'

* 最后，在 callBack.py 中修改 model name，在 demo.py 中修改Appid，然后运行即可


## License
MIT




