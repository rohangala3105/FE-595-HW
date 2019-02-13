# -*- coding: utf-8 -*-

'''
Name:       Poojan Gajera
Stevens ID: 10432734
Course:     FE 595
HW:         01
Title:      Python Refresher
'''

import numpy as np
import matplotlib.pyplot as plt

# Taking values from 0 to 360 for the cycle of sine/cosine.
period = np.arange(0,2*np.pi,0.01)

# Sine, Cosine and tangent Graph
sine = np.sin(period )
cosine = np.cos(period )
tan = np.tan(period)

#plotting sin and cosine on the same axis
plt.plot(period,sine,period,cosine,period,tan)

##creating legends
plt.subplot().legend(['Sine','Cosine','Tangent'])

plt.subplot().axhline(y=0, color='k')
plt.subplot().axvline(x=0, color='k')
plt.savefig("graph.png")
plt.show()
