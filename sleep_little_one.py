#!/usr/bin/env python

import random

while True:
    space = random.randint(2,10)
    print "\033[9%dm" % (space), " " * space , "la la"

