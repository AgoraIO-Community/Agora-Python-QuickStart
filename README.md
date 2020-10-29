# Agora Python Quick-Start

*[中文](Readme.zh.md) | English*

Several demos are contained in this repository. You may pick up some demos to run!



## Index

- [Agora Basic One-to-One Video Call Demo](https://github.com/AgoraIO-Community/Agora-Python-QuickStart/tree/master/basic_one_to_one_video)
- [Agora Face Recognition Demo](https://github.com/AgoraIO-Community/Agora-Python-QuickStart/tree/master/face_recognition)



## Prerequisites

- Xcode (macOS)
- Visual Studio 2017+ with C++ (Windows)
- Python 3.6+



## Quick-Start

You can also write a simple demo yourself by the following instructins.

1. Install Agora Python SDK.

   **Method 1: Use PyPI (Recommended)**

   ```bash
   pip3 install agora-python-sdk
   ```

   **Method 2: Compile from Source Code**

   For detail information, please visit [here](https://github.com/AgoraIO-Community/Agora-Python-SDK#method-2-compile-sdk).

2. Open a Python3 console in Terminal (macOS) or PowerShell (Windows).

   ```bash
   python3
   ```

3. Write a simple demo in Python console.

   ```python
   >>> import agorartc
   >>> rtc = agorartc.createRtcEngineBridge()
   >>> eventHandler = agorartc.RtcEngineEventHandlerBase()
   >>> rtc.initEventHandler(eventHandler)
   0 (Success)
   >>> rtc.initialize("your-appID", None, agorartc.AREA_CODE_GLOB & 0xFFFFFFFF)  # If you do not have an App ID, see Appendix (https://github.com/AgoraIO-Community/Agora-Python-SDK#appendix).
   0 (Success)
   >>> rtc.enableVideo()
   0 (Success)
   >>> rtc.joinChannel("", "channel-name", "", 0)
   0 (Success)
   >>> rtc.leaveChannel()  # Leave channel
   0 (Success)
   ```



## Appendix

### Create an Account and Obtain an App ID

To use our SDK, you must obtain an app ID: 

1. Create a developer account at [agora.io](https://dashboard.agora.io/signin/). Once you finish the sign-up process, you are redirected to the dashboard.
2. Navigate in the dashboard tree on the left to **Projects** > **Project List**.
3. Copy the app ID that you obtained from the dashboard into a text file. You will use it when you call our SDK.