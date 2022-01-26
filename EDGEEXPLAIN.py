from igraph import *
import numpy as np
from numpy.linalg import inv

alpha = 10
c = 1
D = np.zeros((15,15))
D[0,:]=np.array([0,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
Y = np.zeros((15,4))
Y[0,:] = np.array([1/2,1/2,1/2,1/2])
Y[1:5,:] = np.tile(np.array([1/2,1/2,0,1]), (4,1))
Y[5:11,:] = np.tile(np.array([1,0,0,1]), (6,1))
Y[11:15,:] = np.tile(np.array([1,0,0,1]), (4,1))
print(Y)

label_type=2;

def sigma(x):
     return  1/(1+math.exp(-1*x))

def normalize(fu):
    if np.sum(fu[0:2]) != 0 :
            fu[0:2] = fu[0:2]/np.sum(fu[0:2])
    if np.sum(fu[2:4]) != 0 :
            fu[2:4] = fu[2:4]/np.sum(fu[2:4])
    return fu

def doubleSigma(u,v):
    f = 0
    f += np.dot(Y[u,0:2], Y[v,0:2])
    f += np.dot(Y[u, 2:4], Y[v,2:4])
    return f

def gradient1(j):
    nabla = 0
    for v in range(1,15):
        f_vtl = Y[v, j]
        nabla += alpha*f_vtl*sigma(-alpha*doubleSigma(0,v)-c)
        #print(sigma(-alpha*doubleSigma(0,v)-c))
    return nabla

def gradient2(fu):
    
    for j in range(4):
        fu[j] = gradient1(j)
        fu = normalize(fu)                
        Y[0, :] = fu
        
    return fu

def iterative(ck, k):
    fu = np.array(4)
    fu = np.array([1/2,1/2,1/2,1/2])
    for ite in range(k):
        fu  = normalize(fu)
        fu = fu + ck*gradient2(fu)
        print ('fu', fu)
        
    return fu

ck = 1/1000
fu = iterative(ck, 2000)
print('label of u',fu)