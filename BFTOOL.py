#! /usr/bin/python

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

# Logging
start_time = time.perf_counter()
now = datetime.datetime.now()
time_str0 = now.strftime("%H:%M:%S.%f")[:-1]
date_str = now.strftime("%Y%m%d")
logfile = f"BfG_Log_{date_str}.log"
logging.basicConfig(filename=logfile, level=logging.INFO)


# Open the text file containing the list of passwords
passwords = []
with open('pwnedpasswords.txt', 'r') as f:
    for line in f:
        passwords.append(line.strip())

# If the file is small, open it as a whole
#with open('pwnedpasswords.txt', 'r') as f:
#    passwords = f.read().splitlines()

# Define the desired false positive rate
false_positive_rate = 0.0000001

# Calculate the required size of the bit array and the number of hash functions
#num_bits = 34359738368 # 4 Gb
num_bits = int(-(len(passwords) * math.log(false_positive_rate)) / (math.log(2) ** 2))
num_hashes = int((num_bits / len(passwords)) * math.log(2))

# Create a bit array of the specified size, initialized to all 0s
bit_array = bitarray.bitarray(num_bits)
bit_array.setall(False)

# For each password in the list, generate num_hashes hash values using MurmurHash3 and set the corresponding bits in the bit array to 1
for password in passwords:
    for i in range(num_hashes):
        hash_value = mmh3.hash64(password.encode(), i)[0] % num_bits
        bit_array[hash_value] = True

# Write the Bloom filter to a binary file
with open('finalfinalBF.bin', 'wb') as f:
    bit_array.tofile(f)

end_time = time.perf_counter()
elapsed_time = end_time - start_time
print("num_hashes (k): ", num_hashes)
print("num_bits   (m): ", num_bits)
print("False +ves (p): ", false_positive_rate)
print(f"Time it took to Generate: {elapsed_time:.6f}")


now = datetime.datetime.now()
time_str1 = now.strftime("%H:%M:%S.%f")[:-1]
date_str1 = now.strftime("%d/%m/%Y")
logging.info(f"================:{date_str1}:================")
logging.info(f"Started at: {time_str0}")
logging.info(f"Ended   at: {time_str1}")
logging.info(f"number of hashes (k): {num_hashes}")
logging.info(f"number of bits   (m): {num_bits}")
logging.info(f"False positives  (p): {false_positive_rate}")
logging.info(f"Time it took to Generate: {elapsed_time:.6f}")
logging.info(f"")
