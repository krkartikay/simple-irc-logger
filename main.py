from irc import *
import time
 
channel = "#testit"
server = "irc.freenode.net"
nickname = "logger_bot"
filename = "log.txt"

irc = IRC()
irc.connect(server, channel, nickname)

with open(filename,'w') as f:
    while 1:
        text = irc.get_text()
        if "PRIVMSG" in text and channel in text:
            name = text[text.index(':')+1:text.index('!')]
            message = text[text.index(channel):]
            message = message[message.index(':')+1:-1]
            f.write(time.asctime()+"\t"+name+":\t"+message+'\n')
        elif "PART" in text:
            name = text[text.index(':')+1:text.index('!')]
            f.write(time.asctime()+"\t<-- "+name+" left"+'\n')
        elif "JOIN" in text:
            name = text[text.index(':')+1:text.index('!')]
            f.write(time.asctime()+"\t--> "+name+" has joined"+'\n')
