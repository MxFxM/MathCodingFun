import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import math

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.5)

# slider positions for every parameter
axcolor = 'lightgoldenrodyellow'
#                      x,    y,   length, height
axduration = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor=axcolor)
axamplitudex = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
axamplitudey = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)
axfrequencyx = plt.axes([0.25, 0.2, 0.65, 0.03], facecolor=axcolor)
axfrequencyy = plt.axes([0.25, 0.25, 0.65, 0.03], facecolor=axcolor)
axphasex = plt.axes([0.25, 0.3, 0.65, 0.03], facecolor=axcolor)
axphasey = plt.axes([0.25, 0.35, 0.65, 0.03], facecolor=axcolor)
axdampingx = plt.axes([0.25, 0.4, 0.65, 0.03], facecolor=axcolor)
axdampingy = plt.axes([0.25, 0.45, 0.65, 0.03], facecolor=axcolor)

# sliders for every parameter
#                       position,   name,       min,  max,   start,        stepsize
sliderduration = Slider(axduration, "Duration", 1000, 10000, valinit=2000, valstep=1000)
slideramplitudex = Slider(axamplitudex, "Amplitude X", 1, 10, valinit=1, valstep=1)
slideramplitudey = Slider(axamplitudey, "Amplitude Y", 1, 10, valinit=1, valstep=1)
sliderfreuquencyx = Slider(axfrequencyx, "Frequency X", 1.5, 10, valinit=1, valstep=0.01)
sliderfreuquencyy = Slider(axfrequencyy, "Frequency Y", 1, 10, valinit=1, valstep=0.01)
sliderphasex = Slider(axphasex, "Phase X", 0, 2 * math.pi, valinit=1, valstep=0.01)
sliderphasey = Slider(axphasey, "Phase Y", 0, 2 * math.pi, valinit=0, valstep=0.01)
sliderdampingx = Slider(axdampingx, "Damping X", 0, 1, valinit=0.01, valstep=0.01)
sliderdampingy = Slider(axdampingy, "Damping Y", 0, 1, valinit=0.01, valstep=0.01)

def update(val):
    ax.cla()

    duration = int(sliderduration.val)
    amplitudeX = slideramplitudex.val
    frequencyX = sliderfreuquencyx.val
    phaseX = sliderphasex.val
    dampingX = sliderdampingx.val
    amplitudeY = slideramplitudey.val
    frequencyY = sliderfreuquencyy.val
    phaseY = sliderphasey.val
    dampingY = sliderdampingy.val

    time = [n*0.01 for n in range(duration)]
    omegaX = 2 * math.pi * frequencyX
    omegaY = 2 * math.pi * frequencyY

    x = [amplitudeX * math.pow(math.e, -dampingX * omegaX * t) * math.sin(math.sqrt(1 - dampingX**2) * omegaX * t + phaseX) for t in time] # a damped sine wave
    y = [amplitudeY * math.pow(math.e, -dampingY * omegaY * t) * math.sin(math.sqrt(1 - dampingY**2) * omegaY * t + phaseY) for t in time] # a damped sine wave

    ax.plot(x, y)

sliderduration.on_changed(update)
slideramplitudex.on_changed(update)
slideramplitudey.on_changed(update)
sliderfreuquencyx.on_changed(update)
sliderfreuquencyy.on_changed(update)
sliderphasex.on_changed(update)
sliderphasey.on_changed(update)
sliderdampingx.on_changed(update)
sliderdampingy.on_changed(update)

update(0) # initial drawing
plt.show()