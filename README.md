# Agora 1-to-1 Python Demo Integrated with Tensorflow
This is a simple python demo for Agora 1-to-1 video call extended by Tensorflow object detection API.

其他语言版本：  [简体中文](https://github.com/AgoraIO-Community/Agora-Python-Tensorflow-Demo/blob/master/README.zh.md)



## Requirements
- Python 3.6
- Tensorflow >= 1.12
- opencv-python
- pillow

## Installation
- Get Agora Python SDK from [here](https://github.com/AgoraIO-Community/Agora-Python-SDK) and put the corresponding files to the root directory of this project. For Windows, you need `.pyd` and `.dll` files. For Mac, you need the `.so` file.
- Download [Tensorflow models](https://github.com/tensorflow/models) and put the `object_detection` directory to the root directory of this project. 
- Install [Protobuf](https://github.com/protocolbuffers/protobuf/releases). Then run:
```
protoc object_detection/protos/*.proto --python_out=.
```
- Download pre-trained models from [here](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md). We recommend `ssd_mobilenet_v1_coco` and `ssdlite_mobilenet_v2_coco` since they are much faster.
- To extract the frozen graph, run:
```
python extractGraph.py --model_file='FILE_NAME_OF_YOUR_MODEL'
```
- Finally, specify your model name in the beginning of `callBack.py` and your AppId in the beginning of `demo.py`.

## License
- MIT
