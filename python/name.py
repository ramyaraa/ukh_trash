"""import sys
print("helow, my name is", sys.argv[2])   # aw 2 eane che shtek la command lineaka 3eam nusra awa bnusawa 0 nawe fileakaea 1 nawe eakama 2 nawe 2ama

# agar hech nanuse awa indexError adat"""



"""
import sys
try:
    print("helow, my name is", sys.argv[1])

except IndexError:
    print("no name")"""

import sys

if len(sys.argv)<2:
    print("few arguments")
elif len(sys.argv)>2:
    print("too many arguments")
else:
    print(sys.argv[1])