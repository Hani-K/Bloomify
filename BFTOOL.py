#! /usr/bin/python

import mmh3
import bitarray

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
with open('bloom_filter.bin', 'wb') as f:
    bit_array.tofile(f)
