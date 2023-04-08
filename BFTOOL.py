#! /usr/bin/python

#################
#   This is the Base of the code. It works as well as MurMurHash3 algorithm works.
#   Limitations: Large databases have a probability of hash collisions, which in 
#   practice, shows all tested words as not detected.
#   Added a workaround by increaing number of hash functions.
#################

import mmh3
import bitarray
import math
import datetime
import time
import logger
import os
import wCount

# Limit RAM usage to 5GB
#memory_limit_bytes = 5 * 1024 * 1024 * 1024
#resource.setrlimit(resource.RLIMIT_AS, (memory_limit_bytes,memory_limit_bytes))

# Add number of lines extracter using wc -l {name of the file}
# grip the numbers value and put it in a variable

def bits_to_gigabyte(bits):
    bytes = bits / 8
    gigabytes = bytes / 1024 / 1024 / 1024
    return gigabytes

def main():
    # Define the desired false positive rate
    false_positive_rate = 0.001
    
    # user input
    while True:
        print("""Perform Real or Test?
            1. Real
            2. Test""")
        choice = input("Enter your choice: ")

        if choice == "1":
            gType = "Real"
            number_of_lines = wCount.count_lines()
            textFile = "pwnedpasswords.txt"
            now = datetime.datetime.now()
            binFile = "finalBF_" + now.strftime("%H%M")
            break
        elif choice == "2":
            gType = "Teal"
            number_of_lines = 39
            textFile = "testList.txt"
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
            num_partitions = 8

            # Calculate the required size of the bit array and the number of hash functions
            num_bits = int(-(number_of_lines * math.log(false_positive_rate)) / (math.log(2) ** 2))
            num_bits_per_partition = (num_bits + 1) // num_partitions

            # Calculate hashes for each partition
            num_hashes = int((num_bits_per_partition / number_of_lines) * math.log(2))
            break
        else:
            print("Invalid choice. Try again.")

    # Logging
    start_time = time.perf_counter()
    time_str0 = logger.logging_start(now)

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

        # Write the Bloom filter to a binary file
        for i in range(num_partitions):
            with open(os.path.join(results_folder, f'{binFile}{i}.bin'), 'wb') as f:
                bit_arrays[i].tofile(f)
    else:
        # Create a bit array of the specified size, initialized to all 0s
        bit_array = bitarray.bitarray(num_bits)
        bit_array.setall(False)

        # For each password in the list, generate num_hashes hash values using MurmurHash3 and set the corresponding bits in the bit array to 1
        # Open the text file containing the list of passwords
        with open(textFile, 'r') as f:
            for line in f:
                password = line.strip()
                for i in range(num_hashes):
                    hash_value = mmh3.hash64(password.encode(), i)[0] % num_bits
                    bit_array[hash_value] = True

        # Write the Bloom filter to a binary file
        with open(os.path.join(results_folder, f'{binFile}.bin'), 'wb') as f:
            bit_array.tofile(f)

    # Logging
    FinalBinFile = os.path.join(results_folder, f'{binFile}.bin')
    logger.logging_finish(start_time,textFile,FinalBinFile,gType,time_str0,num_hashes,num_bits,false_positive_rate)
    
if __name__ == '__main__':
    main()