#! /usr/bin/python

#################
#   This is the Base of the code. It works as well as MurMurHash3 algorithm works.
#   Workarounds for hash collisions limitation have been provided.
#################

import mmh3
import bitarray
import math
import datetime
import time
import logger
import os
import wCount
import optimalP
import readline
import bfg

readline.parse_and_bind('tab: complete')


    
if __name__ == '__main__':
    logger.startLogging()
    bfg.bfg()
    logger.endLogging()