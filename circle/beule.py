import sys
import math

if len(sys.argv) != 3:
    exit("Usage: {} LENGTH RADIUS".format(sys.argv[0]))

length = float(sys.argv[1])
radius = float(sys.argv[2])

alpha = math.asin((length/2)/radius)*2
a = math.cos(alpha/2)*radius
b = radius-a

print(b)
