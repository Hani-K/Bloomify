#! /usr/bin/python

import logging
import datetime
import time
import math

def format_duration(duration):
    seconds = duration #// 1000000
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f'{int(hours):02}:{int(minutes):02}:{int(seconds):02}'

def startLogging():
    logfile = f"LOG.log"
    logging.basicConfig(filename=logfile, level=logging.INFO)
    now = datetime.datetime.now()
    date_str = now.strftime("%d/%m/%Y")
    logging.info(f"================:{date_str}:================")

def endLogging():
    logging.info(f"================############================\n")

def bfGlog_start(now):
    # Logging
    time_str0 = now.strftime("%H:%M:%S.%f")[:-1]
    date_str = now.strftime("%Y%m%d")
    #logfile = f"BfG_Log_{date_str}.log"
    #logging.basicConfig(filename=logfile, level=logging.INFO)
    return time_str0

def bfGlog_finish(start_time,textFile,binFile,gType,time_str0,num_hashes,num_bits,false_positive_rate,number_of_lines):
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
    logging.info(f"===: BFG Logger:")
    logging.info(f"Input  file: {textFile}")
    logging.info(f"Output file: {binFile}")
    logging.info(f"Total number of passwords: {number_of_lines}")
    logging.info(f"Generation type: {gType}")
    logging.info(f"Started at: {time_str0}")
    logging.info(f"Ended   at: {time_str1}")
    logging.info(f"Number of hashes (k): {num_hashes}")
    logging.info(f"Number of bits   (m): {num_bits}")
    logging.info(f"False positives  (p): {false_positive_rate}")
    logging.info(f"Time it took to Generate: {durationTime}.{microseconds:06}")

def bfChecker_finish(start_time,not_detected_TextFile,binFile,textFile,gType,time_str0,num_hashes,num_bits,num_passwords,num_not_detected,num_detected):
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    microseconds = int((elapsed_time - int(elapsed_time)) * 1000000)
    durationTime = format_duration(elapsed_time)
    print(f"Time it took to check: {durationTime}.{microseconds:06}")
    print()
    print(f"Checked List file: {textFile}")
    print(f"Bloom Filter Binary: {binFile}")

    now = datetime.datetime.now()
    time_str1 = now.strftime("%H:%M:%S.%f")[:-1]
    date_str1 = now.strftime("%d/%m/%Y")
    logging.info(f"===: CHECKER:")
    logging.info(f"Input txt: {textFile}")
    logging.info(f"Input Bin: {binFile}")
    logging.info(f"Check type: {gType}")
    logging.info(f"Total number of items checked: {num_passwords}")
    logging.info(f"Number of items detected: {num_detected}")
    logging.info(f"Number of items NOT detected: {num_not_detected}")
    logging.info(f"Output undetected items file: {not_detected_TextFile}")
    logging.info(f"Started at: {time_str0}")
    logging.info(f"Ended   at: {time_str1}")
    logging.info(f"Number of hashes (k): {num_hashes}")
    logging.info(f"Number of bits   (m): {num_bits}")
    logging.info(f"Time it took to Check: {durationTime}.{microseconds:06}")

def bfgMulti_Log(num_partitions,num_bits_per_partition):
    logging.info(f"===: Extra:")
    logging.info(f"Number of partitions: {num_partitions}")
    logging.info(f"Number of bits per partition: {num_bits_per_partition}")

def dupliMover_Log(start_time,inFile,outFile,original_linesCount,output_linesCount,num_removed_words,time_str0):
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    microseconds = int((elapsed_time - int(elapsed_time)) * 1000000)
    durationTime = format_duration(elapsed_time)
    print(f"Time it took to process: {durationTime}.{microseconds:06}")
    print()
    print(f"Original File: {inFile}")
    print()
    print(f"Original file's word count: {original_linesCount}")
    print(f'Words Removed: {num_removed_words}')
    print(f'Remaining words: {output_linesCount}')
    print(f'Remaining words were generated in {outFile} file')

    now = datetime.datetime.now()
    time_str1 = now.strftime("%H:%M:%S.%f")[:-1]
#    date_str1 = now.strftime("%d/%m/%Y")
    logging.info(f"===:Duplicate Remover:")
    logging.info(f"Input  file: {inFile}")
    logging.info(f"Output file: {outFile}")
    logging.info(f"Started at: {time_str0}")
    logging.info(f"Ended   at: {time_str1}")
    logging.info(f'Original word count: {original_linesCount}')
    logging.info(f"Removed   words: {num_removed_words}")
    logging.info(f'Remaining words: {output_linesCount}')

def lineRemover_Log(start_time,inFile,outFile,original_linesCount,output_linesCount,num_removed_words,time_str0,function_used):
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    microseconds = int((elapsed_time - int(elapsed_time)) * 1000000)
    durationTime = format_duration(elapsed_time)
    print(f"Time it took to process: {durationTime}.{microseconds:06}")
    print()
    print(f"Original File: {inFile}")
    print()
    print(f"Original file's word count: {original_linesCount}")
    print(f'Words Removed: {num_removed_words}')
    print(f'Remaining words: {output_linesCount}')
    print(f'Remaining words were generated in {outFile} file')

    now = datetime.datetime.now()
    time_str1 = now.strftime("%H:%M:%S.%f")[:-1]
    logging.info(f"===: <8 Length Remover:")
    logging.info(f"Function Used: {function_used}")
    logging.info(f"Input  file: {inFile}")
    logging.info(f"Output file: {outFile}")
    logging.info(f'Time started: {time_str0}')
    logging.info(f'Original word count: {original_linesCount}')
    logging.info(f"Removed   words: {num_removed_words}")
    logging.info(f'Remaining words: {output_linesCount}')