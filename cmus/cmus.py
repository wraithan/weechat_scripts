#!/usr/bin/python
import socket

class cmus(object):
    """ Python bindings for C* Music Player
    
    Does not support remote connections, only local sockets in the file 
    system.
    
    """
    def __init__(self, socketLocation):
        """Takes the socket location and does initial setup but does not 
        connect.
        
        socketLocation the full path to the unix socket that cmus creates.
        
        """
        self.cmusLocation = socketLocation
        self.cmusSocket = socket.socket(socket.AF_UNIX,socket.SOCK_STREAM)
        self.connected = False
    
    def connect(self):
        """Connects to cmus, throws socket.error upon failure. Should
        be called before any other methods.
        
        """
        if not self.connected:
            try:
                self.cmusSocket.connect(self.cmusLocation)
            except socket.error:
                pass
            else:
                self.connceted = True
    
    def pause(self):
        if self.connected:
            self.cmusSocket.send("player-pause\n")
        else:
            print("Error, not connected")

