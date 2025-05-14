#!/usr/bin/env python3
# Author: Chanho Lee
# Author ID: clee259
# Date Created: 2025/05/13 GMT-4 20:41

import sys

if len(sys.argv) != 2: 
    timer = 3 # Set timer to 3 by default
else:
    timer = int(sys.argv[1])

while timer != 0:
    print(timer)
    timer = timer - 1

print("blast off!")