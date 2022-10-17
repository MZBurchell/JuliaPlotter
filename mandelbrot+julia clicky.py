# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backend_bases import MouseButton
from matplotlib.offsetbox import (OffsetImage, AnnotationBbox)
import matplotlib.image as image



def matrix(xmin, xmax, ymin, ymax, values):
    re = np.linspace(xmin, xmax, values)
    im = np.linspace(ymin, ymax, values)
    return re[np.newaxis, :] + (im[:, np.newaxis] * 1j)
#creates a matrix of complex points

def is_stable(c, num_iterations):
    z = 0
    for _ in range(num_iterations):
        z = z**2 + c
    return abs(z) <= 2
#checks if a complex number is stable (i.e. belongs in the Mandelbrot set)

def julia_gen(c_val, im_width, im_height, xmin, ymin, xwidth, yheight, zabs_max, nit_max):
    julia = np.zeros((im_width, im_height))
    for ix in range(500):
        for iy in range(500):
            nit = 0
            z = complex(ix / im_width * xwidth + xmin,
                        iy / im_height * yheight + ymin)
            while abs(z) <= zabs_max and nit < nit_max:
                z = z**2 + c_val
                nit += 1
            ratio = nit / nit_max
            julia[ix,iy] = ratio
    return julia
#generates a julia set for given values of c, image height and width, xmin, ymin, xwidth, ywidth, absolute z_max and max nit.

def on_click(event):

    if event.button is MouseButton.LEFT and event.inaxes == ax1:
        ax1.clear()
        ax2.clear()
        #clears all subplots
        ax1.imshow(data, cmap='Greys')
        #replots mandelbrot set
        ab = AnnotationBbox(imagebox, (event.xdata, event.ydata), frameon = False)
        ax1.add_artist(ab)
        #adds a crosshair on the mandelbrot set to show where the user has clicked
        axesHandle.set
        ax2.imshow(julia_gen(complex(-2.0 + ((2.5/3000) * event.xdata), -1.5 + event.ydata/1000), 500, 500, -1.5, -1.5, 3.0, 3.0, 10, 100), cmap='hot')
        fig.canvas.draw_idle()
        #plots the julia set for the selecteed value of c using previously defined julia_gen function




crosshair = image.imread('crosshair.png')
imagebox = OffsetImage(crosshair, zoom = 0.05)
#defines the crosshair image to be used in the on_click function


fig= plt.figure()
ax1 = plt.subplot(121)
plt.tick_params(
    axis='both',          
    which='both',      
    bottom=False,      
    top=False,
    left=False,
    labelleft=False,         
    labelbottom=False)
#creates a figure and the first subplot (for the mandelbrot set), clears axis ticks for this subplot

c = matrix(-2, 0.5, -1.5, 1.5, values=3000)
data = is_stable(c, num_iterations=25)
plt.imshow(data, cmap='Greys')
#plots the mandelbrot set using previously defined functions matrix and is_stable
plt.gca().set_aspect('equal')
plt.rcParams['figure.dpi'] = 600
plt.rcParams['savefig.dpi'] = 600


ax2 = plt.subplot(122)
plt.tick_params(
    axis='both',          
    which='both',      
    bottom=False,      
    top=False,
    left=False,
    labelleft=False,         
    labelbottom=False)
axesHandle = ax2.imshow(julia_gen(complex(-0.1, 0.65), 500, 500, -1.5, -1.5, 3.0, 3.0, 10, 100), cmap='hot')
#creates a subplot for the julia set, clears axis ticks for this subplot, and plots an initial julia set for c = -0.1 + 0.65i

plt.tight_layout()
plt.connect('button_press_event', on_click)
#connects the button_press_event to the previously defined on_click function

plt.show()

