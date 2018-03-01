from irc import *
import time
 
channel = "#testit"
server = "irc.freenode.net"
nickname = "logger_bot"
 
irc = IRC()
irc.connect(server, channel, nickname)
  
while 1:
    text = irc.get_text()
    if "PRIVMSG" in text and channel in text:
        name = text[text.index(':')+1:text.index('!')]
        message = text[text.index(channel):]
        message = message[message.index(':')+1:-1]
        print(time.asctime()+"\t"+name+":\t"+message)
    elif "PART" in text:
        name = text[text.index(':')+1:text.index('!')]
        print(time.asctime()+"\t<-- "+name+" left")
    elif "JOIN" in text:
        name = text[text.index(':')+1:text.index('!')]
        print(time.asctime()+"\t--> "+name+" has joined")
