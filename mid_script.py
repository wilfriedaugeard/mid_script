#!/usr/bin/env python3

"""
Little Man In the Middle script by Exyos.
"""

import subprocess
import sys

from mid import NetworkScan 
from mid import Utils
from mid import Menu
from mid import Redirection



action_table = ['Scan the network and run MID attack','Quit']
ip_table = []


if __name__ == "__main__":
    
    # Kill all old processus created by this program
    ut = Utils.Utils()
    ut.free()

    # Launch menu
    menu = Menu.Menu(action_table, NetworkScan.NetworkScan())
    menu.launch_menu()
    
    


    

