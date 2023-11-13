#! /usr/bin/python

import subprocess
import os
import readline
import signal
import logging
import datetime
import time
import logger

readline.parse_and_bind('tab: complete')

def count_lines(file):
    output = subprocess.check_output(['wc', '-l', file])
    return int(output.strip().split()[0])

def extension_check(file):
    if not file.endswith('.txt'):
        file += '.txt'
    return file

def create_output_folder():
    results_folder = 'results'
    curated_folder = os.path.join(results_folder, 'curated')
    if not os.path.exists(results_folder):
        os.makedirs(results_folder)
    if not os.path.exists(curated_folder):
        os.makedirs(curated_folder)
    return curated_folder

def less_than_8_remover(inFile, outFile):
    # Logging
    now = datetime.datetime.now()
    start_time = time.perf_counter()
    time_str0 = logger.bfGlog_start(now)

    print('Removing words less than 8 characters long...')
    with open(outFile, 'w') as output_file:
        subprocess.call(['awk', 'length >= 8', inFile], stdout=output_file)

    num_removed_words = count_lines(inFile) - count_lines(outFile)
    output_linesCount = count_lines(outFile)
    orig_num_lines = count_lines(inFile)
    
    logger.dupliMover_Log(start_time,inFile,outFile,orig_num_lines,output_linesCount,num_removed_words,time_str0)

    input('\nPress Enter...')