import numpy as np
import math
import pylab as pl
from numpy import cross, eye, dot
from scipy.linalg import expm3, norm

def M(axis, theta):
    return expm3(cross(eye(3), axis/norm(axis)*theta))

yaxis, theta =  [0,1,0], math.pi*22.5/180

M1 = M(yaxis, theta)
print('M1:', M1)
#t=[0, 0, 300] #C  -1.0249031413081129e+02,    3.8761348456470546e+00, 3.6926921486321095e+02
t=[ -1.0249031413081129e+02,    3.8761348456470546e+00, 3.6926921486321095e+02] #C 
Rinv = np.asarray(M1).tolist() #R
print('Rinv:', Rinv)
tinv = -dot(Rinv,t) #-RC
print('t:', tinv)

#R3=[ -7.9334588075188262e-01, -2.0247727636742888e-02, 7.7139635830836897e-03]
R=[ -7.9334588075188262e-01, -2.0247727636742888e-02, 7.7139635830836897e-03]
Rnew = dot(Rinv,R)	
print('R:', Rnew)
