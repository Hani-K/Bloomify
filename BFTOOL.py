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
import logging
import datetime
import time
import resource

# Limit RAM usage to 5GB
#memory_limit_bytes = 5 * 1024 * 1024 * 1024
#resource.setrlimit(resource.RLIMIT_AS, (memory_limit_bytes,memory_limit_bytes))

# Add number of lines extracter using wc -l {name of the file}
# grip the numbers value and put it in a variable

def bits_to_gigabyte(bits):
    bytes = bits / 8
    gigabytes = bytes / 1024 / 1024 / 1024
    return gigabytes

def format_duration(duration):
    seconds = duration #// 1000000
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f'{int(hours):02}:{int(minutes):02}:{int(seconds):02}'

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
            number_of_lines = 851082816
            textFile = "pwnedpasswords.txt"
            now = datetime.datetime.now()
            binFile = "finalBF_" + now.strftime("%H%M") + ".bin"
            break
        elif choice == "2":
            gType = "Teal"
            number_of_lines = 39
            textFile = "testList.txt"
            now = datetime.datetime.now()
            binFile = "testBF.bin"
            break
        else:
            print("Invalid choice. Try again.")
    
    # Calculate the required size of the bit array and the number of hash functions
    while True:
        method = input("""\nWhich method to use?
        1. Standard (Default)
        2. K compensator (hash collision workaround)""")
        
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
        else:
            print("Invalid choice. Try again.")

    # Logging
    start_time = time.perf_counter()
    time_str0 = now.strftime("%H:%M:%S.%f")[:-1]
    date_str = now.strftime("%Y%m%d")
    logfile = f"BfG_Log_{date_str}.log"
    logging.basicConfig(filename=logfile, level=logging.INFO)

    numbit_in_gigabytes = bits_to_gigabyte(num_bits)
    print("num_hashes (k): ", num_hashes)
    print("num_bits   (m): ", num_bits)
    print(f"Number of bits in GBs: {numbit_in_gigabytes} GB")
    print("False Positives (p): ", false_positive_rate)

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
    with open(binFile, 'wb') as f:
        bit_array.tofile(f)

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    microseconds = int((elapsed_time - int(elapsed_time)) * 1000000)
    durationTime = format_duration(elapsed_time)
    print(f"Time it took to Generate: {durationTime}.{microseconds:06}")
    print()
    print(f"Input  file: {textFile}")
    print(f"Output file: {binFile}")

    now = datetime.datetime.now()
    time_str1 = now.strftime("%H:%M:%S.%f")[:-1]
    date_str1 = now.strftime("%d/%m/%Y")
    logging.info(f"================:{date_str1}:================")
    logging.info(f"Input  file: {textFile}")
    logging.info(f"Output file: {binFile}")
    logging.info(f"Generation type: {gType}")
    logging.info(f"Started at: {time_str0}")
    logging.info(f"Ended   at: {time_str1}")
    logging.info(f"number of hashes (k): {num_hashes}")
    logging.info(f"number of bits   (m): {num_bits}")
    logging.info(f"False positives  (p): {false_positive_rate}")
    logging.info(f"Time it took to Generate: {durationTime}.{microseconds:06}")
    logging.info(f"")

if __name__ == '__main__':
    main()