import matplotlib.pyplot as plt
import math

time = [n*0.01 for n in range(2000)]

amplitudeX = 1 # amplitude of oscillation
frequencyX = 1.5 # frequency in Hz (undamped)
phaseX = 2 # phase offset in radians
dampingX = 0.01 # damping ratio
amplitudeY = 1 # amplitude of oscillation
frequencyY = 1 # frequency in Hz (undamped)
phaseY = 0 # phase offset in radians
dampingY = 0.01 # damping ratio

omegaX = 2 * math.pi * frequencyX
omegaY = 2 * math.pi * frequencyY

x = [amplitudeX * math.pow(math.e, -dampingX * omegaX * t) * math.sin(math.sqrt(1 - dampingX**2) * omegaX * t + phaseX) for t in time] # a damped sine wave
y = [amplitudeY * math.pow(math.e, -dampingY * omegaY * t) * math.sin(math.sqrt(1 - dampingY**2) * omegaY * t + phaseY) for t in time] # a damped sine wave

# plt.plot(time, x)
# plt.plot(time, y)

plt.plot(x, y)
plt.show()