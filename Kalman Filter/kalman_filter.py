# Source: https://scipy-cookbook.readthedocs.io/items/KalmanFiltering.html
# Kalman filter example demo in Python

# A Python implementation of the example given in pages 11-15 of "An
# Introduction to the Kalman Filter" by Greg Welch and Gary Bishop,
# University of North Carolina at Chapel Hill, Department of Computer
# Science, TR 95-041,
# https://www.cs.unc.edu/~welch/media/pdf/kalman_intro.pdf

# by Andrew D. Straw

# Changes to original code given above: added sin/cos to see effect. 
# Just multiple state estimations, no information fusion

from math import pi

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (10, 8)


# intial parameters
n_iter = 500
states = [np.sin, np.cos]
num_states = len(states)
sz = (num_states,n_iter) # size of array
x = 0 # truth value (typo in example at top of p. 13 calls this z)

# prior1 = np.sin(np.linspace(0, 4*pi, num=n_iter))        # mathematical model
# prior2 = np.cos(np.linspace(0, 4*pi, num=n_iter))        # mathematical model

z = np.random.normal(x,0.15,size=sz)             # observations (normal about x, sigma=0.1)
t = []                                           # True values
for i, state in enumerate(states):
    t.append(state(np.linspace(0, 4*pi, num=n_iter)))   # Add mathematical model parameters)
    z[i,:] += t[i]

min_val = np.min(np.min(z))
max_val = np.min(np.max(z))

Q = 1e-3 # process variance ... [-5 -> worst. -3 -> better. So increasing exponent is good? But truth value is more noisy]

# allocate space for arrays
xhat=np.zeros(sz)               # a posteri estimate of x
P=np.zeros(sz)                  # a posteri error estimate
xhatminus=np.zeros(sz)        # a priori estimate of x
Pminus=np.zeros(sz)             # a priori error estimate
K=np.zeros(sz)                  # gain or blending factor

R = 0.15**2 # estimate of measurement variance, change to see effect

# intial guesses
xhat[:,0] = 1.0
P[:,0] = 1.0

for k in range(1,n_iter):
    # time update
    xhatminus[:,k] = xhat[:,k-1]
    Pminus[:,k] = P[:,k-1]+Q

    # measurement update
    K[:,k] = Pminus[:,k]/( Pminus[:,k]+R )
    xhat[:,k] = xhatminus[:,k]+K[:,k]*(z[:,k]-xhatminus[:,k])
    P[:,k] = (1-K[:,k])*Pminus[:,k]


valid_iter = range(1,n_iter) # Pminus not valid at step 0
# print(Pminus[0,valid_iter].shape)
# print(Pminus[0,valid_iter])

for s, state in enumerate(states):
    plt.figure()
    plt.plot(z[s,:],'k+',label='noisy measurements')
    plt.plot(xhat[s,:],'b-',label='a posteri estimate')
    plt.plot(t[s],color='g',label='truth value')
    plt.legend()
    plt.title('Estimate vs. iteration step for state %s' % (s,), fontweight='bold')
    plt.xlabel('Iteration')
    plt.ylabel('State value')

# plt.figure()
# plt.plot(valid_iter,Pminus[0,valid_iter],label='a priori error estimate')
# plt.title('Estimated $\it{\mathbf{a \ priori}}$ error vs. iteration step', fontweight='bold')
# plt.xlabel('Iteration')
# plt.ylabel('$(Voltage)^2$')
# plt.setp(plt.gca(),'ylim',[min_val, max_val])

plt.show()