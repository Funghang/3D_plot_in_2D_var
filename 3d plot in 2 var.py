# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 02:19:32 2021

@author: DELL
"""

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

def fun(x, t):
  return x+t #Any equation
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = np.arange(-20.0, 20.0, 0.05)
t = np.arange(0.0,50.0,1)
X, Y = np.meshgrid(x, t)
zs = np.array([fun(x,t) for x,t in zip(np.ravel(X), np.ravel(Y))])
Z = zs.reshape(X.shape)

ax.plot_surface(X, Y, Z)

ax.set_xlabel('X Position')
ax.set_ylabel('Time')
ax.set_zlabel('Concentration')

plt.show()