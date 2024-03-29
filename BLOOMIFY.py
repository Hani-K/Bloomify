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
import lineRemover
import fileMerger

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

    # Define the second-level menu options
    lines_remover_menu = {
        '1': 'Remove every line below 8 char long',
        '2': 'Remove duplicates and every line below 8 char long',
        '3': 'Remove all lines of a certain length.',
        '4': 'Remove all lines below a certain length.',
        '5': 'Remove all lines above a certain length',
        '6': 'Back'
    }

    # Define the third-level menu options
    file_merger_menu = {
        '1': 'Merge all files in a specific path.',
        '2': 'Merge specific files',
        '3': 'Merge all files in curated folder.',
        '4': 'Back'
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
            Color.menuHeading("Lines Remover")
            for key, value in lines_remover_menu.items():
                print(key, value)
        elif menu_level == 3:
            subprocess.call(['clear'], shell=True)
            print_banner()
            Color.menuHeading("File Merger")
            for key, value in file_merger_menu.items():
                print(key, value)


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
                while True:
                    inFile = dupliMover.extension_check(input("Enter the path of the file you want to remove duplicates from: "))
                    if os.path.exists(inFile):
                        break 
                    else:
                        print("Invalid file path. Please try again.")
                curated_path = dupliMover.create_output_folder()
                outFile = os.path.join(curated_path, inFile)
                print(f'\nOriginal word count: {dupliMover.count_lines(inFile)}')
                dupliMover.duplicate_remover(inFile, outFile)
            elif selection == '4':
                menu_level = 2
            elif selection == '5':
                menu_level = 3
            elif selection == '0':
                break
            else:
                print("Invalid selection. Try again!\n")
                input()

        #lines_remover_menu
        elif menu_level == 2:
            if selection == '1':
                while True:
                    inFile = lineRemover.extension_check(input("Enter the path of the file to be processed: "))
                    if os.path.exists(inFile):
                        break 
                    else:
                        print("Invalid file path. Please try again.")
                curated_path = lineRemover.create_output_folder()
                outFile = os.path.join(curated_path, inFile)
                print(f'\nOriginal word count: {lineRemover.count_lines(inFile)}')
                lineRemover.less_than_8_remover(inFile, outFile)
            elif selection == '2':
                while True:
                    inFile = lineRemover.extension_check(input("Enter the path of the file to be processed: "))
                    if os.path.exists(inFile):
                        break 
                    else:
                        print("Invalid file path. Please try again.")
                curated_path = lineRemover.create_output_folder()
                outFile = os.path.join(curated_path, inFile)
                print(f'\nOriginal word count: {lineRemover.count_lines(inFile)}')
                lineRemover.allInOne(inFile, outFile)
            elif selection == '3':
                while True:
                    inFile = lineRemover.extension_check(input("Enter the path of the file to be processed: "))
                    if os.path.exists(inFile):
                        break 
                    else:
                        print("Invalid file path. Please try again.")
                curated_path = lineRemover.create_output_folder()
                outFile = os.path.join(curated_path, inFile)
                while True:
                    try:
                        length = int(input('Enter the length at which each line will be removed (e.g. 7): '))
                        break
                    except ValueError:
                        print('Invalid Value, Try again!\n')
                print(f'\nOriginal word count: {lineRemover.count_lines(inFile)}')
                lineRemover.length_select_remover(inFile, outFile, length)
            elif selection == '4':
                while True:
                    inFile = lineRemover.extension_check(input("Enter the path of the file to be processed: "))
                    if os.path.exists(inFile):
                        break 
                    else:
                        print("Invalid file path. Please try again.")
                curated_path = lineRemover.create_output_folder()
                outFile = os.path.join(curated_path, inFile)
                while True:
                    try:
                        length = int(input('Enter the minimum length (words less than that length will be removed): '))
                        break
                    except ValueError:
                        print('Invalid Value, Try again!\n')
                print(f'\nOriginal word count: {lineRemover.count_lines(inFile)}')
                lineRemover.less_than_length_remover(inFile, outFile, length)
            elif selection == '5':
                while True:
                    inFile = lineRemover.extension_check(input("Enter the path of the file to be processed: "))
                    if os.path.exists(inFile):
                        break 
                    else:
                        print("Invalid file path. Please try again.")
                curated_path = lineRemover.create_output_folder()
                outFile = os.path.join(curated_path, inFile)
                while True:
                    try:
                        length = int(input('Enter the maximum length (words bigger than that length will be removed): '))
                        break
                    except ValueError:
                        print('Invalid Value, Try again!\n')
                print(f'\nOriginal word count: {lineRemover.count_lines(inFile)}')
                lineRemover.more_than_length_remover(inFile, outFile, length)
            elif selection == '6':
                menu_level = 1
            else:
                print("Invalid selection. Try again!\n")
                input()

        #file_merger_menu
        elif menu_level == 3:
            if selection == '1':
                while True:
                    path_directory = input('\nEnter the path within which you want to merge all files:\n')
                    if os.path.isdir(path_directory):
                        break
                    else:
                        print("Invalid directory path. Please try again.")
                fileMerger.merge_all_in_one(path_directory)
            elif selection == '2':
                #loop taking inputs until done is written
                #Merge specific files
                print('\nUnder construction...')
                input()
            elif selection == '3':
                pwd = subprocess.run(['pwd'], stdout=subprocess.PIPE, universal_newlines=True)
                curated_path = fileMerger.create_output_folder()
                path_to_process = os.path.join(pwd.stdout.strip(), curated_path)
                fileMerger.merge_all_in_one(path_to_process)
            elif selection == '4':
                menu_level = 1
            else:
                print("Invalid selection. Try again!\n")
                input()
        

if __name__ == '__main__':
    try:
        print_banner()
        logger.startLogging()
        menu()
        logger.endLogging()
    except KeyboardInterrupt:
        print('\nCTRL + C is Detected\nExiting...')
        exit(0)