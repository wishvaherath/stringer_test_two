#!/usr/bin/env python
import sys
f = open(sys.argv[1].strip())
x = int(f.read())
y = x * x



f = open("power.txt","w")
f.write(str(y) + "\n")

f.close()
