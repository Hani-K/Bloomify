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
import bfCheckerSingle
import bfCheckerMulti

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
        '2': 'Bloom Filter Checker',
        '3': 'List Manuplator',
        '4': 'File Merger',
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
#        elif menu_level == 2:
 #           subprocess.call(['clear'], shell=True)
  #          print_banner()
 #           print("\nBloom Filter Checker:\n")
 #           print("\nDoes the Bloom Filter consists of a single file or multiple parts?\n")
 #           for key, value in bfgCheck_menu.items():
 #               print(key, value)


        # menu selection
        selection = input("\nEnter selection: ")

        # Main Menu
        if menu_level == 1:
            if selection == '1':
                subprocess.call(['clear'], shell=True)
                print_banner()
                bfg.bfg()
            elif selection == '2':
                menu_level = 1
                subprocess.call(['clear'], shell=True)
                print_banner()
                print("\nBloom Filter Checker:\n")
                print("""How does the Bloom Filter look like?
                    1. A single binary file.
                    2. Multiple binary files (divided into partitions)""")
                while True:
                    bloomCheckType = input("Enter your choice: ")
                    if bloomCheckType == "1":
                        subprocess.call(['clear'], shell=True)
                        print_banner()
                        bfCheckerSingle.main()
                        break
                    elif bloomCheckType == "2":
                        subprocess.call(['clear'], shell=True)
                        print_banner()
                        bfCheckerMulti.check()
                        break
                    else:
                        print("Invalid choice. Try again.")
            elif selection == '3':
                menu_level = 3
            elif selection == '4':
                menu_level = 4
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