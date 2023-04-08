#! /usr/bin/python

import mmh3
import bitarray

# Open the text file containing the list of passwords
with open('passwords.txt', 'r') as f:
    passwords = f.read().splitlines()

# Define the size of the Bloom filter and the number of hash functions to use
num_bits = 1000000
num_hashes = 5

# Create a bit array of the specified size, initialized to all 0s
bit_array = bitarray.bitarray(num_bits)
bit_array.setall(False)

# For each password in the list, generate num_hashes hash values using MurmurHash3 and set the corresponding bits in the bit array to 1
for password in passwords:
    for i in range(num_hashes):
        hash_value = mmh3.hash64(password, i) % num_bits
        bit_array[hash_value] = True

# Write the Bloom filter to a binary file
with open('bloom_filter.bin', 'wb') as f:
    bit_array.tofile(f)
