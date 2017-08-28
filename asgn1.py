# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np

print ("hi")
x = [-2.23,-1.30,-0.42, 0.30, 0.33, 0.52, 0.87, 1.80, 2.74, 3.62]
y = [1.01, 0.69, -0.66, -1.34, -1.75, -0.98, 0.25, 1.57, 1.65, 1.51]
k=3
x_mat=(np.matrix(x)).T
y_mat=(np.matrix(y)).T
z_mat=np.hstack((x_mat.T,y_mat.T))
#print(z_mat.T.shape)
phi_k=(np.matrix(np.ones(10))).T
#print(phi_k)

for i in range(1,k+1):
    phi_k=np.hstack((phi_k,np.power(x_mat,i)))

