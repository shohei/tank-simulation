#!/usr/bin/env python
#-*- coding:utf-8 -*-

#*** TANK PRESSURE SIMULATION ***
#*** AUTHOR: SHOHEI AOKI ********
#*** PROGRAMMED: 22 JUL 2015 ****

from pylab import *

##### PARAMETER AREA ############
gamma = 1.4
de = 2 #[mm]
Ae = pi*(de*0.001/2)*(de*0.001/2)#[m2]
T0i = (24 + 273.15) # Room temperature
R = 289 # J/(kg dot K)
V = 1/1000.0 #1L as [m3]
sigma = sqrt(gamma*((2/(gamma+1))**((gamma+1)/(gamma-1)))) # critical flow efficient

##### SIMULATION FOR 10 SECONDS ##
t = arange(0.01,10,0.01) # 10 sec 
pi = 0.1013*5*(10**6) # 5[MPa]
p0 = (1 + (((gamma - 1)/2)*(Ae*sigma*sqrt(R * T0i))/V)*t)**((-1)*2*gamma/(gamma-1))*pi

##### VISUALIZATION AREA #########
plot(t,p0*(10**-6))
show()

