#! /usr/bin/python

import subprocess

# wc -l has been used to lower strain on memory for large files.
def count_lines():
    filename = input('Enter the file path: \n')
    wc_output = subprocess.check_output(['wc', '-l', filename])
    wc_output_str = wc_output.decode('utf-8')
    num_lines = int(wc_output_str.split()[0])
    return num_lines

def count_lines_file(filename):
    wc_output = subprocess.check_output(['wc', '-l', filename])
    wc_output_str = wc_output.decode('utf-8')
    num_lines = int(wc_output_str.split()[0])
    return num_lines
