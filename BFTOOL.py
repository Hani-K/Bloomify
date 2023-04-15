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
from color import Color

readline.parse_and_bind('tab: complete')

def print_banner():
    Color.pl(r'{R}     ____  ________________  ____  __  {R}')
    Color.pl(r'{R}    / __ )/ ____/_  __/ __ {O}\/ {R}__ {O}\/ {R}/  {G}BFTOOL {W}0.4')
    Color.pl(r'{R}   / __  / /_    / / / / / / / / / /   {W}{D}a list manuplation and bloom filter generation tool{R}')
    Color.pl(r'{R}  / /_/ / __/   / / / /_/ / /_/ / /___ {W}{D}created and maintained by Hani K.{R}')
    Color.pl(r'{R} /_____/_/     /_/  {W}{O}\_{R}___/{O}\_{R}___/_____/ {C}{D}https://github.com/Hani-K/bftool{W}')
    Color.pl('\n')


if __name__ == '__main__':
    print_banner()
    logger.startLogging()
    bfg.bfg()
    logger.endLogging()