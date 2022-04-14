#!/usr/bin/env python
# coding: utf-8

# In[77]:


import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.animation as anim
from IPython.display import HTML
from pathlib import Path


def f(x):
   
    if x >-20 and x<-20/2:
        return 20
    if x >-20/2 and x<20/2:
        return 20/2
    if x>20/2 and x<20:
        return 20
    else :
        return 0
x = np.linspace(-20,50,20)
t = np.linspace(0,50,40)
# Compute initial shape of string

y = []
for i in range(len(x)):
    y.append(f(x[i]))

k = np.vectorize(f)
# Plot initial shape
fig, (ax0, ax1) = plt.subplots(figsize = (5,10), nrows = 2, 
                               sharex = "all", sharey = "all")
plt.subplots_adjust(hspace = 0.3)
rwave,  = ax0.plot(x, y, "-", color = "C2", label = r"$f(x - ct)$")
lwave,  = ax0.plot(x, y, "-", color = "C1", label = r"$f(x + ct)$")
string, = ax1.plot(x, y, "-", color = "C0", lw = 2)

ax0.set_title(r"Traveling waves")
ax0.legend(loc = "lower right")
ax1.set_title(r"Superposition:  $[f(x + ct) + f(x - ct)]/2$")
ax1.set_xticks([-20,-10,10,20])

for ax in (ax0, ax1):
    ax.set_ylim([0,20])
    ax.set_yticks((0, 10,20, 30))
    ax.grid(True)

# Compute traveling wave solution
def shift(t, c = 1):
    # Transpose each traveling wave
    new_r, new_l = k(x - c*t), k(x + c*t)
    new_y = (new_l + new_r)/2
    rwave.set_ydata(new_r)
    lwave.set_ydata(new_l)
    string.set_ydata(new_y)
    return(lwave, rwave, string)
#contour
[X, T] = np.meshgrid(x,t)
fig1, ax = plt.subplots(1,1)
Z=0.5*(k(X-T)+k(X+T))

  
 # plots contour lines
plt.contourf(Z)
plt.colorbar()
plt.title('Contour Plot')
plt.xlabel('x')
plt.ylabel('t')
  


# Animate
ani = anim.FuncAnimation(fig, shift, frames = 10,
                         interval = 2, blit = True)
plt.show()

new = plt.figure() 
axes = new.gca(projection ='3d') 
axes.plot_surface(X,T,Z)   


anima=anim.FuncAnimation(new,shift,frames=10,interval=2,blit=True)
plt.show()


# In[ ]:




