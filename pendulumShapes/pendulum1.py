import matplotlib.pyplot as plt
import math

time = [n*0.01 for n in range(2000)]

amplitude = 1 # amplitude of oscillation
frequency = 1 # frequency in Hz (undamped)
phase = 0 # phase offset in radians
damping = 0.1 # damping ratio

omega = 2 * math.pi * frequency

# y = [math.sin(omega*t) for t in time] # a simple sine wave
y = [amplitude * math.pow(math.e, -damping * omega * t) * math.sin(math.sqrt(1 - damping**2) * omega * t) for t in time] # a damped sine wave

plt.plot(time, y)
plt.show()