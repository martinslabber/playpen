#!/usr/bin/env python

import random
import time

while True:
    space = random.randint(2,10)
    print "\033[9%dm" % (space), " " * space , "la la pooh bear"
    time.sleep(0.2)

