#! /usr/bin/python

import math
import os
import subprocess

# Function to calculate the optimal false positive rate based on the number of passwords
def calculate_optimal_false_positive_rate(num_passwords):
    return math.pow(0.6185, math.log(num_passwords))

def count_lines():
    filename = input('Enter the file path: \n')
    wc_output = subprocess.check_output(['wc', '-l', filename])
    wc_output_str = wc_output.decode('utf-8')
    num_lines = int(wc_output_str.split()[0])
    return num_lines

