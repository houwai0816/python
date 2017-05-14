#!/usr/bin/python
import os


cmd = 'tshark -i enp0s3 -Y http.request -T fields -e http.host -e http.user_agent -a duration:20> http_output.txt'
os.system(cmd)
print "HTTP information is captured"

#!/usr/bin/python
import os

cmd ='tshark -i enp0s3 -f "src port 53" -n -T fields -e dns.qry.name -e frame.time -a duration:20 > dns_output.txt'

os.system(cmd)
print "DNS information is captured"

#!/usr/bin/python
import os

cmd = 'tshark -i enp0s3 -a duration:20 -c100 -Y tcp.analysis > tcp_output.txt'
os.system(cmd)

print "TCP information is captured"
