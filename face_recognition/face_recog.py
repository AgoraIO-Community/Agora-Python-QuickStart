import agorartc
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox
import MainWindow
import faceRecognition
import sys
from PyQt5 import QtOpenGL
from PyQt5.QtWidgets import QApplication

import ctypes
from PIL import Image

localWinId = -1
remoteWinId = -1

fc = faceRecognition.faceRecognition()
global img_label
age_gender_predict = False


class MyRtcEngineEventHandler(agorartc.RtcEngineEventHandlerBase):

    def __init__(self, rtc):
        super().__init__()
        self.rtc = rtc

    def onWarning(self, warn, msg):
        print("warn: ")
        print(warn)

    def onError(self, err, msg):
        print("err: ")
        print(err)

    def onJoinChannelSuccess(self, channel, uid, elapsed):
        print("onJoinChannelSuccess")

    def onRejoinChannelSuccess(self, channel, uid, elapsed):
        print("onRejoinChannelSuccess")

    def onLeaveChannel(self, stats):
        print("onLeaveChannel")

    def onClientRoleChanged(self, oldRole, newRole):
        print("onClientRoleChanged")

    def onUserJoined(self, uid, elapsed):
        global remoteWinId
        if remoteWinId != -1:
            remoteVideoCanvas = agorartc.createVideoCanvas(remoteWinId)
            remoteVideoCanvas.uid = uid
            self.rtc.setupRemoteVideo(remoteVideoCanvas)

    def onUserOffline(self, uid, reason):
        print("onUserOffline")

    def onLastmileQuality(self, quality):
        print("onLastmileQuality")

    def onLastmileProbeResult(self, res):
        print("onLastmileProbeResult")

    def onConnectionInterrupted(self):
        print("onConnectionInterrupted")

    def onConnectionLost(self):
        print("onConnectionLost")

    def onConnectionBanned(self):
        print("onConnectionBanned")

    def onApiCallExecuted(self, err, api, res):
        print("onApiCallExecuted" + str(api))

    def onRequestToken(self):
        print("onRequestToken")

    def onTokenPrivilegeWillExpire(self, token):
        print("onTokenPrivilegeWillExpire")

    def onAudioQuality(self, uid, quality, delay, lost):
        print("onAudioQuality")

    def onRtcStats(self, stats):
        print("onRtcStats")

    def onNetworkQuality(self, uid, txQuality, rxQuality):
        print("onNetworkQuality")

    def onLocalVideoStats(self, stats):
        print("onLocalVideoStats")

    def onRemoteVideoStats(self, stats):
        print("onRemoteVideoStats")

    def onLocalAudioStats(self, stats):
        print("onLocalAudioStats")

    def onRemoteAudioStats(self, stats):
        print("onRemoteAudioStats")

    def onLocalAudioStateChanged(self, state, error):
        print("onLocalAudioStateChanged")

    def onRemoteAudioStateChanged(self, uid, state, reason, elapsed):
        print("onRemoteAudioStateChanged")

    def onAudioVolumeIndication(self, speakers, speakerNumber, totalVolume):
        print("onAudioVolumeIndication")

    def onActiveSpeaker(self, uid):
        print("onActiveSpeaker")

    def onVideoStopped(self):
        print("onVideoStopped")

    def onFirstLocalVideoFrame(self, width, height, elapsed):
        print("onFirstLocalVideoFrame")

    def onFirstRemoteVideoDecoded(self, uid, width, height, elapsed):
        print("onFirstRemoteVideoDecoded")

    def onFirstRemoteVideoFrame(self, uid, width, height, elapsed):
        print("onFirstRemoteVideoFrame")

    def onUserMuteAudio(self, uid, muted):
        print("onUserMuteAudio")

    def onUserMuteVideo(self, uid, muted):
        print("onUserMuteVideo")

    def onUserEnableVideo(self, uid, enabled):
        print("onUserEnableVideo")

    def onAudioDeviceStateChanged(self, deviceId, deviceType, deviceState):
        print("onAudioDeviceStateChanged")

    def onAudioDeviceVolumeChanged(self, deviceType, volume, muted):
        print("onAudioDeviceVolumeChanged")

    def onCameraReady(self):
        print("onCameraReady")

    def onCameraFocusAreaChanged(self, x, y, width, height):
        print("onCameraFocusAreaChanged")

    def onCameraExposureAreaChanged(self, x, y, width, height):
        print("onCameraExposureAreaChanged")

    def onAudioMixingFinished(self):
        print("onAudioMixingFinished")

    def onAudioMixingStateChanged(self, state, errorCode):
        print("onAudioMixingStateChanged")

    def onRemoteAudioMixingBegin(self):
        print("onRemoteAudioMixingBegin")

    def onRemoteAudioMixingEnd(self):
        print("onRemoteAudioMixingEnd")

    def onAudioEffectFinished(self, soundId):
        print("onAudioEffectFinished")

    def onFirstRemoteAudioDecoded(self, uid, elapsed):
        print("onFirstRemoteAudioDecoded")

    def onVideoDeviceStateChanged(self, deviceId, deviceType, deviceState):
        print("onVideoDeviceStateChanged")

    def onLocalVideoStateChanged(self, localVideoState, error):
        print("onLocalVideoStateChanged")

    def onVideoSizeChanged(self, uid, width, height, rotation):
        print("onVideoSizeChanged")

    def onRemoteVideoStateChanged(self, uid, state, reason, elapsed):
        print("onRemoteVideoStateChanged")

    def onUserEnableLocalVideo(self, uid, enabled):
        print("onUserEnableLocalVideo")

    def onStreamMessage(self, uid, streamId, data, length):
        print("onStreamMessage")

    def onStreamMessageError(self, uid, streamId, code, missed, cached):
        print("onStreamMessageError")

    def onMediaEngineLoadSuccess(self):
        print("onMediaEngineLoadSuccess")

    def onMediaEngineStartCallSuccess(self):
        print("onMediaEngineStartCallSuccess")

    def onChannelMediaRelayStateChanged(self, state, code):
        print("onChannelMediaRelayStateChanged")

    def onChannelMediaRelayEvent(self, code):
        print("onChannelMediaRelayEvent")

    def onFirstLocalAudioFrame(self, elapsed):
        print("onFirstLocalAudioFrame")

    def onFirstRemoteAudioFrame(self, uid, elapsed):
        print("onFirstRemoteAudioFrame")

    def onRtmpStreamingStateChanged(self, url, state, errCode):
        print("onRtmpStreamingStateChanged")

    def onStreamPublished(self, url, error):
        print("onStreamPublished")

    def onStreamUnpublished(self, url):
        print("onStreamUnpublished")

    def onTranscodingUpdated(self):
        print("onTranscodingUpdated")

    def onStreamInjectedStatus(self, url, uid, status):
        print("onStreamInjectedStatus")

    def onAudioRouteChanged(self, routing):
        print("onAudioRouteChanged")

    def onLocalPublishFallbackToAudioOnly(self, isFallbackOrRecover):
        print("onLocalPublishFallbackToAudioOnly")

    def onRemoteSubscribeFallbackToAudioOnly(self, uid, isFallbackOrRecover):
        print("onRemoteSubscribeFallbackToAudioOnly")

    def onRemoteAudioTransportStats(self, uid, delay, lost, rxKBitRate):
        print("onRemoteAudioTransportStats")

    def onRemoteVideoTransportStats(self, uid, delay, lost, rxKBitRate):
        print("onRemoteVideoTransportStats")

    def onMicrophoneEnabled(self, enabled):
        print("onMicrophoneEnabled")

    def onConnectionStateChanged(self, state, reason):
        print("onConnectionStateChanged")

    def onNetworkTypeChanged(self, type):
        print("onNetworkTypeChanged")

    def onLocalUserRegistered(self, uid, userAccount):
        print("onLocalUserRegistered")

    def onUserInfoUpdated(self, uid, info):
        print("onUserInfoUpdated")


localRawDataCounter = 0
remoteRawDataCounter = 0


class MyVideoFrameObserver(agorartc.VideoFrameObserver):

    def onCaptureVideoFrame(self, width, height, ybuffer, ubuffer, vbuffer):
        global localRawDataCounter

        print("onCaptureVideoFrame: width {}, height {}, ybuffer {}, ubuffer {}, vbuffer {}".format(width, height,
                                                                                                    ybuffer, ubuffer,
                                                                                                    vbuffer))

    def onRenderVideoFrame(self, uid, width, height, ybuffer, ubuffer, vbuffer):
        global remoteRawDataCounter

        print("onRenderVideoFrame: uid {}, width {}, height {}, ybuffer {}, ubuffer {}, vbuffer {}".format(uid, width,
                                                                                                           height,
                                                                                                           ybuffer,
                                                                                                           ubuffer,
                                                                                                           vbuffer))

        rgba_array = (ctypes.c_ubyte * (width * height * 4)).from_address(ybuffer)
        im = Image.frombuffer('RGBA', (width, height), rgba_array, 'raw', 'RGBA', 0, 1)
        im_processed = fc.frame_process(im, width, height, adaptive_size=True, gender_age=age_gender_predict)
        data = im_processed.convert("RGBA")
        data = data.tobytes("raw", "RGBA")
        qim = QtGui.QImage(data, im_processed.size[0], im_processed.size[1], QtGui.QImage.Format_RGBA8888)
        pix = QtGui.QPixmap.fromImage(qim)
        img_label.setPixmap(pix)


class MyWindow(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self):
        global eventHandler, context, img_label
        QtWidgets.QMainWindow.__init__(self)
        MainWindow.Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.window1 = GLwindow()
        self.gridLayout.addWidget(self.window1)
        img_label = self.img_label
        self.joinButton.clicked.connect(self.joinChannel)
        self.leaveButton.clicked.connect(self.leaveChannel)
        self.enableButton.clicked.connect(self.enableLocalVideo)
        self.disableButton.clicked.connect(self.disableLocalVideo)
        self.enable_ap_btn.clicked.connect(self.enableAdvancedPredict)
        self.disable_ap_btn.clicked.connect(self.disableAdvancedPredict)
        self.rtc = agorartc.createRtcEngineBridge()
        eventHandler = MyRtcEngineEventHandler(self.rtc)
        self.rtc.initEventHandler(eventHandler)
        self.videoFrameObserver = MyVideoFrameObserver()

    def closeEvent(self, event):
        self.rtc.release(True)
        event.accept()

    def joinChannel(self):
        global localWinId, remoteWinId
        localWinId = self.window1.effectiveWinId().__int__()

        if self.checkAppId() == False:
            QMessageBox.information(self, "Message",
                                    "Please input your App ID of your project.",
                                    QMessageBox.Yes)
            return
        if self.checkChannelName() == False:
            QMessageBox.information(self, "Message",
                                    "The channel name contains illegal character.",
                                    QMessageBox.Yes)
            return
        if len(self.channelEdit.text()) == 0:
            QMessageBox.information(self, "Message",
                                    "Please input the channel name.",
                                    QMessageBox.Yes)
            return
        if len(self.channelEdit.text()) > 64:
            QMessageBox.information(self, "Message",
                                    "The length of the channel name must be less than 64.",
                                    QMessageBox.Yes)
            return

        self.rtc.initialize(self.appIdEdit.text(), None, agorartc.AREA_CODE_GLOB & 0xFFFFFFFF)
        self.rtc.enableVideo()
        localVideoCanvas = agorartc.createVideoCanvas(localWinId)
        ret = self.rtc.setupLocalVideo(localVideoCanvas)
        channelName = self.channelEdit.text()
        self.rtc.joinChannel("", channelName, "", 0)
        self.rtc.startPreview()
        agorartc.registerVideoFrameObserver(self.rtc, self.videoFrameObserver)

    def leaveChannel(self):
        self.rtc.leaveChannel()
        agorartc.unregisterVideoFrameObserver(self.rtc, self.videoFrameObserver)

    def enableLocalVideo(self):
        self.rtc.enableLocalVideo(True)

    def disableLocalVideo(self):
        self.rtc.enableLocalVideo(False)

    def checkAppId(self):
        appId = self.appIdEdit.text()
        if len(appId) == 0:
            return False
        return True

    def enableAdvancedPredict(self):
        global age_gender_predict
        age_gender_predict = True

    def disableAdvancedPredict(self):
        global age_gender_predict
        age_gender_predict = False

    def checkChannelName(self):
        channelName = self.channelEdit.text()
        for char in channelName:
            if ord(char) >= ord('a') and ord(char) <= ord('z'):
                continue
            elif ord(char) >= ord('A') and ord(char) <= ord('Z'):
                continue
            elif ord(char) >= ord('0') and ord(char) <= ord('9'):
                continue
            elif char in ["!", "#", "$", "%", "&", "(", ")", "+", "-", ":",
                          ";", "<", "=", ".", ">", "?", "@", "[", "]", "^",
                          "_", "{", "}", "|", "~", ","] or ord(char) == 32:
                continue
            else:
                return False
        return True


class GLwindow(QtOpenGL.QGLWidget):
    def __init__(self):
        QtOpenGL.QGLWidget.__init__(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
