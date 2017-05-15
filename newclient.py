#!/usr/bin/python
import socket
import os
import sys
from progressbar import *
import time
from termcolor import colored
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = raw_input(colored('Please enter server address to connect : ','cyan'))
port = 12347
x=0

args = ['client.py','tcp.py','dns.py','http.py']
file_list= ['tcp_output.txt','dns_output.txt','http_output.txt']

time.sleep(2)
print colored('Ready to capture...','green')
try:
	forkpid1 = os.fork()
except OSError as err:
	print "Can't fork the process!\n",err

if forkpid1 != 0:
	forkpid2 = os.fork()
	if forkpid2 != 0:
		forkpid3 = os.fork()
		if forkpid3 != 0:
			child1 = os.wait()[0]
			child2 = os.wait()[0]
			child3 = os.wait()[0]
		elif forkpid3 == 0:
			os.execl("/usr/bin/python",args[0],args[2])
	elif forkpid2 == 0:
		os.execl("/usr/bin/python",args[0],args[3])
elif forkpid1 == 0:
	os.execl("/usr/bin/python",args[0],args[1])

print 'Please wait checking connection with ',host,'...'
cmd = 'ping -w 5 192.168.0.9 > ping.txt'
os.system(cmd)
files = open('ping.txt','rb')
lines = files.readlines()
if lines:
	last_l = lines[-2]	
print '\n'
pbar=ProgressBar()
pbar.start()
for i in pbar(range(100)):
	time.sleep(0.04)
print colored(last_l,'green')
print colored("Connecting to the server",'yellow')
s.connect((host,port))
print s.recv(1024)
while x<3:
	f=open(file_list[x],'rb')
	l=f.read(1024)
	while(l):
		s.send(l)
		if not l:break
		l=f.read(1024)
	f.close()
	x=x+1
print colored('The file is transferred','green')



#s.recv(1024)
#decision=raw_input('')
#s.send(decision)
#while(1):
	#with open('filtered.txt','wb') as u:
		#print "file opened"
		#w=s.recv(1024)
		#print w
		#while (w):
			#u.write(w)
			#if not w:break
			#w=s.recv(1024)
		#print 'The result had been saved to filtered.txt'
		#u.close()
s.close()
print colored('Connection terminate','red')
