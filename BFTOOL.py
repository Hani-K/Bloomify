#! /usr/bin/python

#################
#   This is the Base of the code. It works as well as MurMurHash3 algorithm works.
#   Workarounds for hash collisions limitation have been provided.
#################

import mmh3
import bitarray
import math
import datetime
import time
import logger
import os
import wCount
import optimalP
import readline
import bfg
from color import Color
import subprocess

readline.parse_and_bind('tab: complete')

def print_banner():
    Color.pl(r'{R}     ____  ________________  ____  __  {R}')
    Color.pl(r'{R}    / __ )/ ____/_  __/ __ {O}\/ {R}__ {O}\/ {R}/  {G}BFTOOL {W}0.4')
    Color.pl(r'{R}   / __  / /_    / / / / / / / / / /   {W}{D}a list manuplation and bloom filter generation tool{R}')
    Color.pl(r'{R}  / /_/ / __/   / / / /_/ / /_/ / /___ {W}{D}created and maintained by Hani K.{R}')
    Color.pl(r'{R} /_____/_/     /_/  {W}{O}\_{R}___/{O}\_{R}___/_____/ {C}{D}https://github.com/Hani-K/bftool{W}')
    Color.pl('\n')

def menu():
    subprocess.call(['clear'], shell=True)

    main_menu = {
        '1': 'Bloom Filter Generator',
        '2': 'List Manuplator',
        '3': 'File Merger',
        '0': 'Exit'
    }

    bfg_menu = {
        '1': 'Standard (Default)',
        '2': 'K compensator (hash collision workaround)',
        '3': 'Partitioning (for very large file when 2nd option fails)',
        '0': 'Exit'
    }

    # Define the initial menu level
    menu_level = 1

    # Loop until "Exit" is selected
    while True:
        # Display the appropriate menu based on the current level
        if menu_level == 1:
            subprocess.call(['clear'], shell=True)
            print_banner()
            Color.menuHeading("Main Menu")
            for key, value in main_menu.items():
                print(key, value)
        elif menu_level == 2:
            subprocess.call(['clear'], shell=True)
            print_banner()
            print("\nBFG Menu:\n")
#            for key, value in main_menu.items():
#                print(key, value)


        # menu selection
        selection = input("\nEnter selection: ")

        # Main Menu
        if menu_level == 1:
            if selection == '1':
                subprocess.call(['clear'], shell=True)
                print_banner()
                bfg.bfg()
            elif selection == '2':
                menu_level = 2
            elif selection == '3':
                menu_level = 3
            elif selection == '0':
                break
            else:
                print("Invalid selection. Try again!\n")
                input()
        

if __name__ == '__main__':
    print_banner()
    logger.startLogging()
    menu()
    logger.endLogging()