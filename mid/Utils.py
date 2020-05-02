import subprocess
import re

class bcolors:
    def __init__(self):
        self.HEADER = '\033[95m'
        self.OKBLUE = '\033[94m'
        self.OKGREEN = '\033[92m'
        self.WARNING = '\033[93m'
        self.FAIL = '\033[91m'
        self.ENDC = '\033[0m'
        self.BOLD = '\033[1m'
        self.UNDERLINE = '\033[4m'
        self.CLEAR = '\033c'
        self.BULLET = '\u2022'


class Utils:
    def __init__(self):
        self.c = bcolors()

    def clean(self):
        print(self.c.CLEAR)

    '''
    Kill processus created
    '''
    def free(self):
        cmd = 'ps aux'
        output = subprocess.check_output(cmd.split(' ')).decode()
        pid_to_kill = []
        lines = output.splitlines()
        for seq in lines:
            proc = re.search('(python dns2proxy.py)|(sudo python dns2proxy.py)|(sslstrip -l)|(arpspoof)',seq)
            if(proc):
                proc = seq.split(' ')
                proc = list(filter(None, proc))
                pid_to_kill.append(proc[1])
        for pid in pid_to_kill:
            cmd = 'sudo kill -9 '+pid
            subprocess.check_output(cmd.split(' '))

    
    def logo(self):
        print(" _______ _____ ______       _______ _______  ______ _____  _____  _______\n |  |  |   |   |     \      |______ |       |_____/   |   |_____]    |\n |  |  | __|__ |_____/      ______| |_____  |    \_ __|__ |          |\n                                                                     \n")

            


