# this class for creating GUI
# using Qt

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class MyClass(QWidget):
    def __init__(self,userName = 'username',recvName = 'recname'):
        super(MyClass,self).__init__()
        self.username = userName
        self.recvname = recvName
        self.initUI()
        
    def initUI(self):
        print "a7a b2a"
        # set text browser
        self.textBrower = QTextBrowser(self)
        self.textBrower.resize(500, 200)
        self.textBrower.move(10,10)
        
        # set line edit 
        self.textEdit = QLineEdit(self)
        self.textEdit.resize(500, 50)
        self.textEdit.move(10, 220)
        self.textEdit.setFocus()
        
        # set send button 
        self.btn = QPushButton('&Send',self)
        self.btn.resize(100,50)
        self.btn.move(510,220)
        
        # connection between lineEdit and textbrowser if press enter or bush putton
        # call update function 
        self.connect(self.textEdit, SIGNAL("returnPressed()"), self.sendMessage)
        self.connect(self.btn, SIGNAL('clicked()'), self.sendMessage)
        self.setWindowTitle(self.recvname)
        self.show()
        
    def  sendMessage(self):
        try :
            message = self.textEdit.text()                                  # get string written in lineEdit
            self.textBrower.append("%s : %s" % (self.username, message) )   # set string to user
            self.textEdit.clear()                                           # clear line editor from contant 
            self.textEdit.setFocus()                                        # set line editor to focus
            self.emit(SIGNAL('sendMessage(QString)'),message)
            print "signal is emitted"
        except :
            print "can't send message !!"
            
    def getmessage(self,message = "testing 101"):
        try:
            self.textBrower.append("%s : %s" % (self.recvname,message))
        except:
            print "can't get message !!"