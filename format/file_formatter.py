#!/usr/bin/env python

import os
import functools
import operator
import sys

PRINT_FORMAT = "%-30s%s"

with open(sys.argv[1],"r") as file:
    for line in file:
        if line.strip():
            words = line.strip().split(" ")
            formatted_line = PRINT_FORMAT % (words[0], functools.reduce(lambda x,y:x+" "+y, words[1:]).lstrip())
            print(formatted_line)
