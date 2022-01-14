import sys

import matplotlib
from PyQt5 import QtWidgets


from Camera_Thread_class import Camera_Thread_class

matplotlib.use("Qt5Agg")  # 声明使用QT5

import  mainwindow2 as uiWindow
ui=0

class FaceMain:

    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        ui = uiWindow.Ui_MainWindow()
        ui.setupUi(self.MainWindow)
        self.ui=ui
        self.initfunc()
        self.MainWindow.show()
        sys.exit(app.exec_())
    def initfunc(self):
        self.camera_thread=Camera_Thread_class(self.ui)
        self.camera_thread.start()
        # 初始化按键信号
        self.initsignal()


    def initsignal(self):
        # 信号绑定的是控制子线程的启动和停止
        self.ui.DetectOnBtn.clicked.connect(self.camera_thread.startRunning)
        self.ui.DetectOffBtn.clicked.connect(self.camera_thread.stopRunning)



if __name__ == '__main__':
    FaceMain()
