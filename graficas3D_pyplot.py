# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 02:18:18 2022

@author: USER
"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def g3d_1():
    #
    fig = plt.figure()
    ax = Axes3D(fig)
    x = np.linspace(-4, 4,50)
    y = np.linspace(-4, 4,50)
    def z(x,y):
        return np.sin(np.sqrt(x**2 + y**2))
    ax.plot(x, y, z(x,y))
    plt.show()
def g3d_2():
    #
    fig = plt.figure()
    ax = Axes3D(fig)
    x = np.linspace(-4, 4,50)
    y = np.linspace(-4, 4,50)
    X,Y =np.meshgrid(x,y)
    def z(x,y):
        return np.sin(np.sqrt(x**2 + y**2))
    ax.plot_surface(X, Y, z(X,Y))
    plt.show()
def g3d_3():
    #
    fig = plt.figure()
    ax = Axes3D(fig)
    x = np.linspace(-4, 4,50)
    y = np.linspace(-4, 4,50)
    X,Y =np.meshgrid(x,y)
    def z(x,y):
        return np.sin(np.sqrt(x**2 + y**2))
    ax.contour(X, Y, z(X,Y))
    plt.show()
def g3d_4():
    #
    fig = plt.figure()
    ax = Axes3D(fig)
    x = np.linspace(-4, 4,50)
    y = np.linspace(-4, 4,50)
    X,Y =np.meshgrid(x,y)
    def z(x,y):
        return np.sin(np.sqrt(x**2 + y**2))
    ax.contourf(X, Y, z(X,Y))
    plt.show()
g3d_1()
g3d_2()
g3d_3()
g3d_4()