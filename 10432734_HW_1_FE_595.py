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

# Sine and Cosine Graph
sine = np.sin(period )
cosine = np.cos(period )

###bhgh

# Creating plots, X & Y axes and legends
plt.plot(period , sine , period , cosine)

plt.subplot().legend(['Sine','Cosine'])               #

plt.subplot().axhline(y=0, color='k')
plt.subplot().axvline(x=0, color='k')

plt.show()
