#!/usr/bin/env python

import sys
sys.path.insert(0, 'usr/local/lib/python2.7/site-packages/')
import mraa

print (mraa.getVersion())
x = mraa.Gpio(14)
x.dir(mraa.DIR_OUT)
x.write(1)
