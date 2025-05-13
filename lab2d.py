#!/usr/bin/env python3

import sys

if len(sys.argv) != 3: #'''! = not equal (3 arguments has to be present for print statement to work; otherwise run error script)'''
    print("Usage: " + sys.argv[0] + " name age")
    sys.exit(0)

name = sys.argv[1]
age = sys.argv[2]

print("Hi " + name + ", you are " + str(age) + " years old.")