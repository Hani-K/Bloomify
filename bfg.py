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

readline.parse_and_bind('tab: complete')

def bits_to_gigabyte(bits):
    bytes = bits / 8
    gigabytes = bytes / 1024 / 1024 / 1024
    return gigabytes

def bfg():
    # user input
    while True:
        print("""Perform Real or Test?
            1. Real
            2. Test""")
        choice = input("Enter your choice: ")

        if choice == "1":
            gType = "Real"
            number_of_lines = wCount.count_lines()
            false_positive_rate = optimalP.p_Select(number_of_lines)
            textFile = "pwnedpasswords.txt"
            now = datetime.datetime.now()
            binFile = "finalBF_" + now.strftime("%H%M")
            break
        elif choice == "2":
            gType = "Test"
            textFile = "testList.txt"
            number_of_lines = wCount.count_lines_file(textFile)
            false_positive_rate = optimalP.p_Select(number_of_lines)
            now = datetime.datetime.now()
            binFile = "testBF"
            break
        else:
            print("Invalid choice. Try again.")
    
    # Calculate the required size of the bit array and the number of hash functions
    while True:
        print("""\nWhich method to use?
        1. Standard (Default)
        2. K compensator (hash collision workaround)
        3. Partitioning (for very large file when 2nd option fails)""")
        method = input("Select: ")

        if method == "1":
            # Standard Method
            num_bits = int(-(number_of_lines * math.log(false_positive_rate)) / (math.log(2) ** 2))
            num_hashes = int((num_bits / number_of_lines) * math.log(2))
            break
        if method == "2":
            # calculation is tuned to a bigger database, in an attempt to limit hash collisions
            num_bits_i = int(-(number_of_lines * math.log(false_positive_rate)) / (math.log(2) ** 2))
            num_hashes = int(4 * math.log(num_bits_i))
            num_bits = int(math.ceil(num_bits_i / num_hashes) * num_hashes)
            break
        if method == "3":
            # hash collisions workaround by partitioning the file into sigments
            num_partitions = 8

            num_bits = int(-(number_of_lines * math.log(false_positive_rate)) / (math.log(2) ** 2))
            num_bits_per_partition = (num_bits + 1) // num_partitions

            num_hashes = int((num_bits_per_partition / number_of_lines) * math.log(2))
            break
        else:
            print("Invalid choice. Try again.")

    # Logging
    start_time = time.perf_counter()
    time_str0 = logger.bfGlog_start(now)

    numbit_in_gigabytes = bits_to_gigabyte(num_bits)
    print("num_hashes (k): ", num_hashes)
    print("num_bits   (m): ", num_bits)
    print(f"Number of bits in GBs: {numbit_in_gigabytes} GB")
    print("False Positives (p): ", false_positive_rate)
    
    results_folder = 'results'
    if not os.path.exists(results_folder):
        os.makedirs(results_folder)

    if method == "3":
        print(f"number of bits per partition:   {num_bits_per_partition}")

        bit_arrays = [bitarray.bitarray(num_bits_per_partition) for _ in range(num_partitions)]
        for bit_array in bit_arrays:
            bit_array.setall(False)

        with open(textFile, 'r') as f:
            for line in f:
                password = line.strip()
                for i in range(num_partitions):
                    hash_values = [mmh3.hash64(password.encode(), j, True)[0] % num_bits_per_partition for j in range(num_hashes)]
                    for index in hash_values:
                        bit_arrays[i][index] = True

        for i in range(num_partitions):
            with open(os.path.join(results_folder, f'{binFile}{i}.bin'), 'wb') as f:
                bit_arrays[i].tofile(f)

        # Logging
        FinalBinFile = os.path.join(results_folder, f'{binFile}.bin')
        logger.bfGlog_finish(start_time,textFile,FinalBinFile,gType,time_str0,num_hashes,num_bits,false_positive_rate,number_of_lines)
        logger.bfgMulti_Log(num_partitions,num_bits_per_partition)

    else:
        # Create a bit array of the specified size.
        bit_array = bitarray.bitarray(num_bits)
        bit_array.setall(False)

        # For each password in the list, generate num_hashes
        with open(textFile, 'r') as f:
            for line in f:
                password = line.strip()
                for i in range(num_hashes):
                    hash_value = mmh3.hash64(password.encode(), i)[0] % num_bits
                    bit_array[hash_value] = True

        with open(os.path.join(results_folder, f'{binFile}.bin'), 'wb') as f:
            bit_array.tofile(f)

        # Logging
        FinalBinFile = os.path.join(results_folder, f'{binFile}.bin')
        logger.bfGlog_finish(start_time,textFile,FinalBinFile,gType,time_str0,num_hashes,num_bits,false_positive_rate)

def main():
    bfg()
    input = input("\nClick enter to continue...")