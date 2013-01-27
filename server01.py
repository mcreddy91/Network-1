import socket, time
import threading
import SocketServer
from chatUI import *

class recvThread(QThread):
    def __init__(self,conn,parent = None):
        QThread.__init__(self,parent)
        print("recv thread init")
        self.conn = conn
        self.message = ''
    
    def run(self):
        print("run threading")
        while 1:
            self.message = self.conn.recv(1024)
            if not self.message == '': 
                self.emit(SIGNAL("getmessage(QString)"),self.message)
                self.message = ''
                print "Singal is emitted"
            

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
        #self.connect(self,SIGNAL("getmessage(QString)"),self.getmessage)
        
    def initConnection(self):
        try:
            server = ThreadedTCPServer((self.host,self.port),ThreadedTCPRequestHandler)
            server_thread = threading.Thread(target=server.serve_forever)
            server_thread.daemon = True
            server_thread.start()
            print "Connect"
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
