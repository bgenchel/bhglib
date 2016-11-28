import socket
import logging 
import time

class TCPClient:

    def __init__(self):
        self.connection = None

    def sendMessage(self, message):
        if self.connection:
            bytes_sent = self.connection.send(message)
            logging.info("bytes_sent: %d"%bytes_sent)
        else:
            print 'No open connection.'
   
    def getResponse(self, buffer_size=1024):
        response = ""

        start_time = time.time()
        curr_time = time.time()
        frombuff = 1
        while frombuff and ((curr_time - start_time) < 5):
            curr_time = time.time()
            try:
                frombuff = self.connection.recv(buffer_size)
            except:
                frombuff = ''
            response = response + frombuff

        return response

    def openConnection(self, IP, PORT, timeout=2):
        if self.connection:
            self.connection.close()

        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((IP, PORT))
        self.connection.settimeout(timeout)
            
    def closeConnection(self):
        if self.connection:
            self.connection.close()
            self.connection = None
        else:
            print 'No open connection.'
