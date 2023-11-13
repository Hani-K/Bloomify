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
import dupliMover

readline.parse_and_bind('tab: complete')

def print_banner():
    Color.pl(r'{R}    ____  __                      _ ____     {R}')
    Color.pl(r'{R}   / __ )/ /___  ____  ____ ___  (_) __/_  __')
    Color.pl(r'{R}  / __  / / __ {O}\/{R} __ {O}\/{R} __ `__ {O}\/{W}{R} / /{D}_{W}{R}/ / / /')
    Color.pl(r'{R} / /_/ / / /_/ / /_/ / / / / / / / __/ /_/ / ')
    Color.pl(r'{R}/_____/_/{W}{O}\_{D}{R}___/{W}{O}\_{D}{R}___/_/ /_/ /_/_/_/  {W}{O}\_{D}{R}_, /  ')
    Color.pl(r'{R}                                    /____/   ')
    Color.pl(r'{G}Bloomify {W}0.5')
    Color.pl(r'{W}{D}a list manuplation and bloom filter generation tool')
    Color.pl(r'{W}{D}created and maintained by Hani K.')
    Color.pl(r'{C}{D}https://github.com/Hani-K/bloomify{W}')
    Color.pl('\n')



def menu():
    subprocess.call(['clear'], shell=True)

    main_menu = {
        '1': 'Bloom Filter Generator',
        '2': 'Bloom Filter Checker',
        '3': 'Duplicates Remover',
        '4': 'List Manuplator',
        '5': 'File Merger',
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
                menu_level = 1
                inFile = dupliMover.extension_check(input("Enter the path of the file you want to remove duplicates from: "))
                curated_path = dupliMover.create_output_folder()
                outFile = os.path.join(curated_path, inFile)
                print(f'\nOriginal word count: {dupliMover.count_lines(inFile)}')
                dupliMover.duplicate_remover(inFile, outFile)
            elif selection == '4':
                menu_level = 4
            elif selection == '5':
                menu_level = 5
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