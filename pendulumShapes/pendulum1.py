import matplotlib.pyplot as plt
import math

time = [n*0.01 for n in range(2000)]

frequency = 1 # frequency in Hz
omega = 2 * math.pi * frequency

y = [math.sin(omega*t) for t in time] # a simple sine wave

plt.plot(time, y)
plt.show()