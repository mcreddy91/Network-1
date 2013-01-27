import socket, time
import threading
import SocketServer
from chatUI import *

class recvThread(QThread):
    def __init__(self,conn,parent = None):
        QThread.__init__(self,parent)
        self.message = ''
        print("recv thread init")
        self.conn = conn

    def run(self):
        print("run threading")
        while 1:
            time.sleep(1)
            self.message = self.conn.recv(1024)
            if not self.message == '':
                self.emit(SIGNAL("getmessage(QString)"),self.message)
                self.message = ''
                print "Singal is emitted"

    def __del__(self):
        self.quit()
            

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
    
    def handle(self):
        print "handler start"
        data = self.request.recv(1024)
        #cur_thread = threading.current_thread()
        print "...." + data + "...."
        self.request.sendall("Send back")
        print "Sent"

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

class serverConncetion(QObject):
    def __init__(self,host,port = 8888):
        self.host = host
        self.port = port
        self.initConnection()
        self.initGUI = MyClass("Hussein","Ahmed")
        self.connect(self.initGUI,SIGNAL("sendMessage(QString)"),self.sendmessage)
        self.connect(self.recThread,SIGNAL("getmessage(QString)"),self.getmessage)
        
    def initConnection(self):
        try:
            serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            serverSocket.bind(('',self.port))
            serverSocket.listen(1)
            print 'Ther Server is ready to receive'
            self.connectionSocket, addr = serverSocket.accept()
            print "Connect"
            self.recThread = recvThread(self.connectionSocket)
            self.recThread.start()
        except socket.error:
            print 'Failed to create socket'
            sys.exit()
            
    def sendmessage(self,message):
        print "sending message 001 " + message
        # send message
        print "message send"
        
    def getmessage(self,message):
        self.initGUI.getmessage(message)
        
    def __del__(self):
        print "colse connection"
        self.connectionSocket.close()
        
def main():
    app = QApplication(sys.argv)
    start = serverConncetion('localhost')
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
