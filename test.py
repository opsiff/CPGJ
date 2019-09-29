
from gui import Ui_MainWindow
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtCore import QThread
from PyQt5 import QtCore
import GITRepo
import check
from  threading import Thread

class Thread(QThread):
    update_Msg=QtCore.pyqtSignal(str)
    def __init__(self,parent=None):
        super(Thread,self).__init__(parent)
        self.url=''
        self.cl=None
        self.mode=0
    def Pro(self,url,cl,mode):
        self.url=url
        self.cl=cl
        self.mode=mode
    def printText(self,text):
        self.update_Msg.emit(text)
    def run(self):
        url=self.url
        self.update_Msg.emit('=============测评开始================')
        try:
            if url == '':
                self.update_Msg.emit('还没输入地址呢!')
                return
            msg, id ,Repo_id= GITRepo.git_clone(url=url, cl=self)
            self.update_Msg.emit(msg)
            if msg == 'clone done' and id:  # 成功
                self.update_Msg.emit('开始测评分数!')
                sum = check.evaluateProcess(id=id, cl=self,mode=self.mode,Repo_id=Repo_id)
                self.update_Msg.emit('最终得分是:' + str(sum))
            else:
                self.update_Msg.emit(msg)
            self.update_Msg.emit('测评结束!')
            print('测评结束!')
        except Exception as e:
            print(e)
class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)
        self.childPro = Thread()
        self.mode=0
        self.initUi()

    def initUi(self):
        self.cBtn.clicked.connect(self.clearInput)
        self.sBtn.clicked.connect(self.run)
        self.modeBox.stateChanged.connect(self.chgMode)
        self.childPro.update_Msg.connect(self.printText)

    def printText(self,text):
        self.outEdt.append(text)
        self.outEdt.moveCursor(self.outEdt.textCursor().End)  # 自动下滑到底部

    def clearInput(self):
        self.inEdt.setText('')
    def chgMode(self):
        #mode=0 快速比对
        if self.modeBox.isChecked():
            self.mode=1
        else:
            self.mode=0
    def run(self):
        url=self.inEdt.text()
        self.childPro.Pro(url,self,self.mode)
        self.childPro.start()

if __name__=="__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())



