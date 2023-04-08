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

def logging_start(now):
    # Logging
    time_str0 = now.strftime("%H:%M:%S.%f")[:-1]
    date_str = now.strftime("%Y%m%d")
    logfile = f"BfG_Log_{date_str}.log"
    logging.basicConfig(filename=logfile, level=logging.INFO)
    return time_str0

def logging_finish(start_time,textFile,binFile,gType,time_str0,num_hashes,num_bits,false_positive_rate):
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