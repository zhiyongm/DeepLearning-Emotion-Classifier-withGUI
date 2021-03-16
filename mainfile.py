import sys #line:1
import matplotlib #line:3
from PyQt5 import QtWidgets #line:4
from Camera_Thread_class import Camera_Thread_class #line:7
matplotlib.use ("Qt5Agg")#line:10
import mainwindow2 as uiWindow #line:12
ui =0 #line:13
class FaceMain :#line:15
    def __init__ (O00O0O00O00OO0OOO ):#line:17
        OOO0O0O0O000O00OO =QtWidgets .QApplication (sys .argv )#line:18
        O00O0O00O00OO0OOO .MainWindow =QtWidgets .QMainWindow ()#line:19
        O00O0O00O00OO0OOO.MainWindow.setStyleSheet("#MainWindow{border-image:url(./ktj_background.png);}")
        O0OO00OOOOO00O00O =uiWindow .Ui_MainWindow ()#line:20
        O0OO00OOOOO00O00O .setupUi (O00O0O00O00OO0OOO .MainWindow )#line:21
        O00O0O00O00OO0OOO .ui =O0OO00OOOOO00O00O #line:22
        O00O0O00O00OO0OOO .initfunc ()#line:23
        O00O0O00O00OO0OOO .MainWindow .show ()#line:24
        sys .exit (OOO0O0O0O000O00OO .exec_ ())#line:25
    def initfunc (OO00OO000OO000OOO ):#line:26
        OO00OO000OO000OOO .camera_thread =Camera_Thread_class (OO00OO000OO000OOO .ui )#line:27
        OO00OO000OO000OOO .camera_thread .start ()#line:28
        OO00OO000OO000OOO .initsignal ()#line:32
    def initsignal (O00O0OO0OOOO0OO0O ):#line:35
        O00O0OO0OOOO0OO0O .ui .DetectOnBtn .clicked .connect (O00O0OO0OOOO0OO0O .camera_thread .startRunning )#line:37
        O00O0OO0OOOO0OO0O .ui .DetectOffBtn .clicked .connect (O00O0OO0OOOO0OO0O .camera_thread .stopRunning )#line:38
if __name__ =='__main__':#line:42
    FaceMain ()