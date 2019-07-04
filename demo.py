import IAgoraRtcEngine
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox
import MainWindow
import sys
from PyQt5 import QtOpenGL
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QThread, pyqtSignal
from callBack import EventHandlerData
import numpy as np
import tensorflow as tf
from utility import checkStr

appId = b"466c2ed3224c4e42996f7e08d2bb7193"

Engine = IAgoraRtcEngine.pycreateAgoraRtcEngine()
ctx = IAgoraRtcEngine.pyRtcEngineContext()
ctx.eventHandler = IAgoraRtcEngine.pyEventHandler()
ctx.appId = appId
Engine.initialize(ctx)
EngineParam = IAgoraRtcEngine.pyRtcEngineParameters()
localWinId = -1
remoteWinId = -1

class callBackListener(QThread):
    def __init__(self):
        super().__init__()
    def run(self):
        while (True):
            if EventHandlerData.localWindowSet == False:
                if EventHandlerData.localUid != -1:
                    window.channelEdit.setEnabled(False)
                    window.joinButton.setEnabled(False)
                    window.leaveButton.setEnabled(True)
                    LocalCanvas = IAgoraRtcEngine.pyVideoCanvas()
                    LocalCanvas.construct_2(localWinId, IAgoraRtcEngine.pyRENDER_MODE_TYPE.RENDER_MODE_HIDDEN,
                                            EventHandlerData.localUid)
                    Engine.setupLocalVideo(LocalCanvas)
                    EventHandlerData.localWindowSet = True

            if EventHandlerData.remoteUserWindowSet == False:
                if EventHandlerData.remoteUid != -1:
                    RemoteCanvas = IAgoraRtcEngine.pyVideoCanvas()
                    RemoteCanvas.construct_2(remoteWinId, IAgoraRtcEngine.pyRENDER_MODE_TYPE.RENDER_MODE_HIDDEN,
                                             EventHandlerData.remoteUid)
                    Engine.setupRemoteVideo(RemoteCanvas)
                    EventHandlerData.remoteUserWindowSet = True
            if EventHandlerData.isImageDetect == False and EventHandlerData.detectReady:
                objectDetect = objectDetectThread()
                objectDetect.objectSignal.connect(window.setObjectText)
                EventHandlerData.detectReady = False
                objectDetect.start()

class joinChannelThread(QThread):
    def __init__(self):
        super().__init__()
        self.channel = ""
    def run(self):
        Engine.joinChannel(appId, self.channel, b"", 0)
        VideoEncoderConfiguration = IAgoraRtcEngine.pyVideoEncoderConfiguration()
        VideoEncoderConfiguration.construct_2(
            1280, 720,
            IAgoraRtcEngine.pyFRAME_RATE.FRAME_RATE_FPS_60,
            0,
            IAgoraRtcEngine.pyORIENTATION_MODE.ORIENTATION_MODE_ADAPTIVE
        )
        Engine.setVideoEncoderConfiguration(VideoEncoderConfiguration)
        Engine.enableVideo()
        EngineParam.construct_3(Engine)
        EngineParam.enableLocalVideo(True)
        EngineParam.muteLocalVideoStream(False)
        MediaEngine = IAgoraRtcEngine.pyGetMediaEngine(Engine)
        MediaEngine.registerVideoFrameObserver(IAgoraRtcEngine.pyVideoFrameObserver())

class leaveChannelThread(QThread):
    def __init__(self):
        super().__init__()
    def run(self):
        Engine.leaveChannel()

class objectDetectThread(QThread):
    objectSignal = pyqtSignal(str)
    def __init__(self):
        super().__init__()
    def run(self):
        detection_graph = EventHandlerData.detection_graph
        with detection_graph.as_default():
            with tf.Session(graph=detection_graph) as sess:
                (im_width, im_height) = EventHandlerData.image.size
                image_np = np.array(EventHandlerData.image.getdata()).reshape((im_height, im_width, 3)).astype(np.uint8)
                image_np_expanded = np.expand_dims(image_np, axis=0)
                image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
                boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
                scores = detection_graph.get_tensor_by_name('detection_scores:0')
                classes = detection_graph.get_tensor_by_name('detection_classes:0')
                num_detections = detection_graph.get_tensor_by_name('num_detections:0')
                (boxes, scores, classes, num_detections) = sess.run(
                    [boxes, scores, classes, num_detections],
                    feed_dict={image_tensor: image_np_expanded})
                objectText = []
                for i, c in enumerate(classes[0]):
                    if scores[0][i] > 0.4:
                        object = EventHandlerData.category_index[int(c)]['name']
                        if object not in objectText:
                            objectText.append(object)
                    else:
                        break
                self.objectSignal.emit(', '.join(objectText))
                EventHandlerData.detectReady = True
                EventHandlerData.isImageDetect = True


class MyWindow(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        MainWindow.Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.window1 = GLwindow()
        self.window2 = GLwindow()
        self.gridLayout.addWidget(self.window1)
        self.gridLayout_2.addWidget(self.window2)
        self.joinButton.clicked.connect(self.joinChannel)
        self.leaveButton.clicked.connect(self.leaveChannel)
        self.leaveButton.setEnabled(False)
        self.objectText.setEnabled(False)
        self.callBackListener = callBackListener()
        self.callBackListener.start()

    def joinChannel(self):
        if EventHandlerData.joinChannelSuccess == False:
            self.joinThread = joinChannelThread()
            checkChnnelMessage = checkStr(self.channelEdit.toPlainText())
            if checkChnnelMessage != "":
                self.showMessage(checkChnnelMessage)
                return
            global localWinId, remoteWinId
            localWinId = self.window1.effectiveWinId().__int__()
            remoteWinId = self.window2.effectiveWinId().__int__()
            self.joinThread.channel = bytes(self.channelEdit.toPlainText(), 'ascii')
            self.joinThread.start()

    def leaveChannel(self):
        if EventHandlerData.joinChannelSuccess == True:
            self.leaveThread = leaveChannelThread()
            self.leaveThread.start()
            self.joinButton.setEnabled(True)
            self.leaveButton.setEnabled(False)
            self.channelEdit.setEnabled(True)

    def setObjectText(self, objectSignal):
        self.objectText.setText(objectSignal)

    def showMessage(self, content):
        QMessageBox.information(self, "Message", content, QMessageBox.Yes)

class GLwindow(QtOpenGL.QGLWidget):
    def __init__(self):
        QtOpenGL.QGLWidget.__init__(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
