import numpy as np
import math
import pylab as pl
from numpy import cross, eye, dot
from scipy.linalg import expm3, norm

def M(axis, theta):
    return expm3(cross(eye(3), axis/norm(axis)*theta))

yaxis, theta =  [0,1,0], math.pi*-22.5/180

M1 = M(yaxis, theta)

#t=[0, 0, 300] #C  -7.5365933249672622e+01 1.4813316191554250e+01 3.7399724715265705e+02
t=[ -73.49350707,  -14.81331619, -374.36969589] #C 
Rinv = np.asarray(M1).T.tolist() #R'
tinv = -dot(Rinv,t) #-RC
print('t:', tinv)

#R3=[ -8.3655325142998860e-01,   -1.0435977468136069e-02,  -8.7523917171074862e-03]
R=[ -0.76952505, -0.01043598, -0.32822122]
Rnew = dot(Rinv,R)	
print('R:', Rnew)
