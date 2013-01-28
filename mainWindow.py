import time
from PyQt4 import QtCore, QtGui
from clientChat import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s
    
class recvThread(QThread):
    def __init__(self,parent = None):
        QThread.__init__(self,parent)
        print("recv thread init")
    
    def run(self):
        print("run threading")
        serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        serverSocket.bind(('',8888))
        serverSocket.listen(1)
        print 'Ther Server is ready to receive'
        connectionSocket, addr = serverSocket.accept()
        sentence = connectionSocket.recv(1024)
        print (sentence)
                
    def __del__(self):
        self.quit()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(474, 381)
        
        # Layout
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 451, 291))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        
        # listWidget
        self.listWidget = QtGui.QListWidget(self.verticalLayoutWidget)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.verticalLayout.addWidget(self.listWidget)
        
        # host Label then lineEdit
        self.HostLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.HostLabel.setObjectName(_fromUtf8("HostLabel"))
        self.gridLayout.addWidget(self.HostLabel, 1, 0, 1, 1)
        
        self.hostLedit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.hostLedit.setObjectName(_fromUtf8("hostLedit"))
        self.gridLayout.addWidget(self.hostLedit, 1, 1, 1, 1)
        self.hostLedit.setText("newHost")

        # IP Label then lineEdit        
        self.IPLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.IPLabel.setObjectName(_fromUtf8("IPLabel"))
        self.gridLayout.addWidget(self.IPLabel, 0, 0, 1, 1)
        
        self.IpLedit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.IpLedit.setObjectName(_fromUtf8("IpLedit"))
        self.gridLayout.addWidget(self.IpLedit, 0, 1, 1, 1)
        self.IpLedit.setText("localhost")
        
        # other layout
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        
        # button
        self.pushButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.setFocus()
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 474, 27))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.HostLabel.setText(QtGui.QApplication.translate("MainWindow", "Host", None, QtGui.QApplication.UnicodeUTF8))
        self.IPLabel.setText(QtGui.QApplication.translate("MainWindow", "IP", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Add Host", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.clicked.connect(self.updateUI)
        self.listWidget.doubleClicked.connect(self.openChat)
        
    def updateUI(self):
        self.listWidget.addItem(self.hostLedit.text() + " " + self.IpLedit.text())
        
    def openChat(self):
        start = ClientConnection(self.IpLedit.text())
        self.close()
        



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    #bGthread = recvThread()
    #bGthread.start()
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

