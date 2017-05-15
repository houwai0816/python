#!/pyhton/usr/bin
from collections import Counter
with open('tcp_output.txt') as tcp:
	print '------------------------------------------------------------------'
	print '               SOURCE TO DESTINATION PORT LISTENING               '
	print '------------------------------------------------------------------'
	for line in tcp:
		
		print line.split()[2],'\t','to','\t',line.split()[4],'\t','listen on',line.split()[5],line.split()[6]
		
	
	print '------------------------------------------------------------------'
	print '                            LISTEN END                            '
	print '------------------------------------------------------------------'



dns_file=open('dns_output.txt')
wc= Counter(dns_file.read().split())
print '\n\n'
print '******************************************************************'
print '*                           Visited DNS                          *'
print '******************************************************************'
for item in wc.items():
	print ("{}\t=\t{}".format(*item))
	print'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'


http_file=open('http_output.txt')
wc= Counter(http_file.read().split())
print '\n\n'
print '******************************************************************'
print '*                           Visited HTTPS                        *'
print '******************************************************************'
for item in wc.items():
	print ("{}\t=\t{}".format(*item))
	print'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
