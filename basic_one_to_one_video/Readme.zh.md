# Agora基础一对一视频通话示例

*[English](README.md) | 中文*



## 安装

### 运行环境

- Python 3.6+
- Xcode (macOS)
- Visual Studio 2017+，需要添加C++支持 (Windows)

### 依赖包

- Agora Python SDK
- PyQt5

### 安装步骤：

**通过PyPI安装依赖包**

```bash
pip3 install agora-python-sdk pyqt5
```

## 运行示例

前往``basic_one_to_one_video``目录，运行命令`python3 one2one.py`。

*如您还未获取App ID，您可以查看附录。*



## 附录

### 创建Agora账户并获取App ID

如果想要使用我们的SDK，您需要先获得一个App ID：

1. 在[agora.io](https://dashboard.agora.io/signin/)中注册一个账号。当您完成注册后，您将被链接至控制台。
2. 在控制台左侧点击**Projects** > **Project List**。
3. 请将您从控制台中获取的App ID保存，您将会在运行示例时使用（示例图形化界面中有输入框）。