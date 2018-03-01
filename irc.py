import socket
import sys
 
class IRC:
 
    irc = socket.socket()
  
    def __init__(self):  
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
    def send(self, chan, msg):
        self._send("PRIVMSG " + chan + " " + msg + "\n")
 
    def connect(self, server, channel, botnick):
        #defines the socket
        print("connecting to:"+server)
        #connects to the server
        self.irc.connect((server, 6667))
        #user authentication
        self._send("USER " + botnick + " " + botnick +" " + botnick + " :This is a fun bot!\n")
        self._send("NICK " + botnick + "\n")
        self._send("JOIN " + channel + "\n")
        #join the chan
 
    def _send(self, text):
        self.irc.send(text.encode())

    def get_text(self):
        text=self.irc.recv(2040).decode()  #receive the text
 
        if text.find('PING') != -1:                      
            self._send('PONG ' + text.split() [1] + 'rn') 
 
        return text

