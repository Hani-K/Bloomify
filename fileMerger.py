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

def create_output_folder():
    results_folder = 'results'
    curated_folder = os.path.join(results_folder, 'curated')
    if not os.path.exists(results_folder):
        os.makedirs(results_folder)
    if not os.path.exists(curated_folder):
        os.makedirs(curated_folder)
    return curated_folder

def merge_all_in_one(path):
    # Logging
    now = datetime.datetime.now()
    start_time = time.perf_counter()
    time_str0 = logger.bfGlog_start(now)

    if os.path.exists(path):
        if not path.endswith('/'):
            path += '/'
        merged_file = os.path.join(path,'merged.txt')
        print(f'Merging all files in one file without duplications..')
        files_names = []
        unique_lines = set()
        with open(merged_file, 'w') as outfile:
            for filename in os.listdir(path):
                if filename.endswith('.txt'):
                    files_names.append(filename)
                    with open(os.path.join(path, filename), 'r') as infile:
                        for line in infile:
                            if line not in unique_lines:
                                unique_lines.add(line)
                                outfile.write(line)
        print(f'Merging complete!\n')

        files_merged = ", ".join(files_names)
        merged_line_count = count_lines(merged_file)
        print(f'Result is generated in {merged_file} file')

        logger.dupliMover_Log(start_time,path,files_merged,merged_line_count,merged_file,time_str0)

        input('\nPress Enter...')
    else:
        print(f'The path {path} does not exist!')