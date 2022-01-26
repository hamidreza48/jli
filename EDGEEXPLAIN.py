from igraph import *
import numpy as np
from numpy.linalg import inv

alpha = 1
c = 0
D = np.zeros((15,15))
D[0,:]=np.array([0,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
Y = np.zeros((15,4))
Y[0,:] = np.array([0,0,0,0])
Y[1:5,:] = np.tile(np.array([0,0,1,0]), (4,1))
Y[5:11,:] = np.tile(np.array([1,0,0,1]), (6,1))
Y[11:15,:] = np.tile(np.array([1,0,0,0]), (4,1))
print(Y)

label_type=2;

def sigma(x):
     return  1/(1+math.exp(-x))
       

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
        Y[0, j] = fu[j]
    return fu

def iterative(ck, k):
    fu = np.array(4)
    fu = np.array([0,0,0,0])
    for ite in range(k):
        fu = fu + ck*gradient2(fu)
        print (fu)
    return fu

ck = 1/1000
fu = iterative(ck, 200)
print('label of u',fu)
    