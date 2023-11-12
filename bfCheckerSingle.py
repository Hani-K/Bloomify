#! /usr/bin/python

import os
import mmh3
import struct
import time
import logger
import bitarray
import readline
import logging
import datetime

readline.parse_and_bind('tab: complete')

# user input
def check():
    while True:
        user_input = input("Do you wanna test (Y/n)? ") or 'y'
        if user_input.lower() == 'n':
            gType = "Real"
            while True:
                try:
                    num_hashes = int(input("Please enter the number of hash functions: "))
                    while True:
                        try:
                            num_bits = int(input("Please enter the number of bits (Size of the Bloom Filter): "))
                            break  # Exit the loop if the input is successfully converted to an integer
                        except ValueError:
                            print("Invalid input. Please enter a valid number.")
                    break  # Exit the loop if the input is successfully converted to an integer
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            textFile = input("Text file path (list to check): ")
            binFile = input("Binary file path (Bloom Filter): ")
            now = datetime.datetime.now()
            break
        elif user_input.lower() == 'y':
            gType = "Test"
            num_hashes = 13
            num_bits = 747
            textFile = "passwords.txt"
            binFile = "results/testBF.bin"
            now = datetime.datetime.now()
            break
        else:
            print("Invalid choice. Try again.")

    # Logging
    start_time = time.perf_counter()
    time_str0 = logger.bfGlog_start(now)

    # Load the Bloom filter from a binary file
    with open(binFile, 'rb') as file:
        # Read the number of elements, false positive probability, and filter data from the binary file
        bit_array = bitarray.bitarray()
        bit_array.fromfile(file)

    # Check if the strings are present in the Bloom filter
    with open(textFile, 'r') as file:
        passwords_to_check = file.read().splitlines()

    results_folder = 'results'
    if not os.path.exists(results_folder):
        os.makedirs(results_folder)

    num_passwords = 0
    num_detected = 0
    num_not_detected = 0
    not_detected_passwords = []
#    detected_passwords = []
    for password in passwords_to_check:
        num_passwords += 1
        is_password_in_filter = True
        for i in range(num_hashes):
            hash_value = mmh3.hash64(password.encode(), i)[0] % num_bits
            if not bit_array[hash_value]:
                is_password_in_filter = False
                break

        if is_password_in_filter:
            num_detected += 1
            print(f'"{password}" is detected')
#            detected_passwords.append(password)
        else:
            num_not_detected += 1
            print(f'"{password}" is NOT detected')
            not_detected_passwords.append(password)
    
    with open(os.path.join(results_folder,f'not_detected_{textFile}'), 'w') as file:
        for not_detected_password in not_detected_passwords:
            file.write(not_detected_password + '\n')

    print("Total number of passwords: {}".format(num_passwords))
    print("Number of passwords detected: {}".format(num_detected))
    print("Number of passwords NOT detected: {}".format(num_not_detected))
    print(f'Not detected passwords are written to not_detected_{textFile}')

    # Logging
    not_detected_TextFile = os.path.join(results_folder,f'not_detected_{textFile}')
    logger.bfChecker_finish(start_time,not_detected_TextFile,binFile,textFile,gType,time_str0,num_hashes,num_bits,num_passwords,num_not_detected,num_detected)

    return not_detected_TextFile

def main():
    not_detected_TextFile = check()
    Continue = input(f"""\n\n
                     Statistics are logged in LOGs file.
                     Click any key to continue.""")