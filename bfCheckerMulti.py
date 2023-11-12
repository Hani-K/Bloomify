#! /usr/bin/python

import os
import mmh3
import struct
import bitarray
import readline
import logging
import datetime
import time
import logger

readline.parse_and_bind('tab: complete')

#num_partitions = 8


def remove_numeric_suffix_from_filename(file_path):
    # Bin partition name editor
    directory, filename = os.path.split(file_path)
    name, extension = os.path.splitext(filename)
    # if filename ends with a numeric suffix + ".bin" then remove them
    if name[:-1].isdigit() and extension == ".bin":
        new_filename = name[:-1]
        # Reconstruct the full path
        new_path = os.path.join(directory, new_filename)
        return new_path
    else:
        return file_path

def check():
    # user input
    while True:
        user_input = input("Do you wanna test (Y/n)? ") or 'y'

        if user_input.lower() == 'n':
            gType = "Real"
            while True:
                try:
                    num_partitions = int(input("Please enter the number of partitions: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            while True:
                try:
                    num_hashes = int(input("Please enter the number of hash functions: "))
                    while True:
                        try:
                            num_bits = int(input("Please enter the TOTAL number of bits (Size of the whole Bloom Filter): "))
                            while True:
                                try:
                                    num_bits_per_partition = int(input("Please enter the number of bits per partition: "))
                                    break  # Exit the loop if the input is successfully converted to an integer
                                except ValueError:
                                    print("Invalid input. Please enter a valid number.")
                            break  # Exit the loop if the input is successfully converted to an integer
                        except ValueError:
                            print("Invalid input. Please enter a valid number.")
                    break  # Exit the loop if the input is successfully converted to an integer
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            textFile = input("Text file path (list to check): ")
            binPartition = input("""Note: Make sure that all partitions are in the same folder and 
                                 their names end in a numeric scequence, starting from zero.
                                (Example: BloomFilter_pt0.bin.. BloomFilter_pt1.bin.. BloomFilter_pt2.bin...etc.)\n
                                Path to any of the partitions (e.g. BloomFilter_pt0.bin): """)
            binFile = remove_numeric_suffix_from_filename(binPartition)
            now = datetime.datetime.now()
            break
        elif user_input.lower() == 'y':
            num_partitions = 8
            gType = "Test"
            num_hashes = 2
            num_bits = 1308
            num_bits_per_partition = 163
            textFile = "passwords.txt"
            binFile = "results/testBF"
            now = datetime.datetime.now()
            break
        else:
            print("Invalid choice. Try again.")

    # Logging
    start_time = time.perf_counter()
    time_str0 = logger.bfGlog_start(now)

    # Load the Bloom filter bit arrays from the binary files
    bit_arrays = []
    for i in range(num_partitions):
        with open(f'{binFile}{i}.bin', 'rb') as f:
            print(f"{binFile}{i}.bin")
            bit_array = bitarray.bitarray()
            bit_array.fromfile(f)
            bit_arrays.append(bit_array)

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
    for password in passwords_to_check:
        num_passwords += 1
        is_password_in_filter = True
        for i in range(num_partitions):
            hash_values = [mmh3.hash64(password.encode(), j, True)[0] % num_bits_per_partition for j in range(num_hashes)]
            for index in hash_values:
                if not bit_arrays[i][index]:
                    is_password_in_filter = False
                    break

        if is_password_in_filter:
            num_detected += 1
            #print(f'"{password}" is detected')
        else:
            num_not_detected += 1
            #print(f'"{password}" is NOT detected')
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
                     Statistics are logged in LOG file.
                     Click any key to continue.""")

