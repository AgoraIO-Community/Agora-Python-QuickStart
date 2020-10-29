# Agora Python 快速开始

*[English](README.md) | 中文*

本仓库中包含一些代码示例。您可以选择一些示例进行运行体验。



## 索引

- [Agora基础一对一视频电话示例](https://github.com/AgoraIO-Community/Agora-Python-QuickStart/tree/master/basic_one_to_one_video)
- [Agora人脸识别示例](https://github.com/AgoraIO-Community/Agora-Python-QuickStart/tree/master/face_recognition)



## 运行环境

- Xcode (macOS)
- Visual Studio 2017+，需要添加C++支持 (Windows)
- Python 3.6+



## 快速开始

您也可以根据如下教程完成一个简单的示例。

1. 安装Agora Python SDK。

   **方法一：使用PyPI（推荐）**

   ```bash
   pip3 install agora-python-sdk
   ```

   **方法二：用源码编译SDK**

   详细信息请参考[这里](https://github.com/AgoraIO-Community/Agora-Python-SDK/blob/master/Readme.zh.md#%E6%96%B9%E6%B3%95%E4%BA%8C%E7%BC%96%E8%AF%91sdk)。

2. 在终端（macOS）或PowerShell（Windows）中打开一个Python3控制台。

   ```bash
   python3
   ```

3. 在Python控制台中完成示例。

   ```python
   >>> import agorartc
   >>> rtc = agorartc.createRtcEngineBridge()
   >>> eventHandler = agorartc.RtcEngineEventHandlerBase()
   >>> rtc.initEventHandler(eventHandler)
   0 （成功）
   >>> rtc.initialize("您的appID", None, agorartc.AREA_CODE_GLOB & 0xFFFFFFFF)  # 如您还未获取App ID，您可以查看附录(https://github.com/AgoraIO-Community/Agora-Python-SDK/blob/master/Readme.zh.md#%E9%99%84%E5%BD%95)。
   0 （成功）
   >>> rtc.enableVideo()
   0 （成功）
   >>> rtc.joinChannel("", "channel-name", "", 0)
   0 （成功）
   >>> rtc.leaveChannel()  # 离开频道
   0 （成功
   ```



## 附录

### 创建Agora账户并获取App ID

如果想要使用我们的SDK，您需要先获得一个App ID：

1. 在[agora.io](https://dashboard.agora.io/signin/)中注册一个账号。当您完成注册后，您将被链接至控制台。
2. 在控制台左侧点击**Projects** > **Project List**。
3. 请将您从控制台中获取的App ID保存，您将会在调用SDK时使用。