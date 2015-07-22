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

##### PARAMETER AREA ############
M = 32 * 0.8 + 14 * 0.2 # O2: 80%, N2: 20%
R0 = 8.314 #(J/mol dot K)
T0 = 24 + 273.15 #[K}
pa = 0.1013*(10**6) #[Pa]: Atmospheric pressure
R_g = R0/M
DISCHARGE_AIR = 42 #[l/min], ref:http://www.airbrush.co.jp/shop/products/detail.php?product_id=1296
dVs1 = DISCHARGE_AIR*0.001/60 #[m3/s]
V = 1/1000.0 #[m3]: tank volume, 1L
pi = pa
dmt = ((pa*dVs1)/(R_g*T0))       # [kg/s]: mass flow rate at atmospheric pressure 


##### SIMULATION FOR AIR DISCHARGE FROM TANK ##
t = arange(0.01,100,0.01) # 100 sec 
p0i = 0.1013*5*(10**6) # 5[MPa]
V_array = [1/1000.0,10/1000.0,20/1000.0]
for V in V_array:
    # charge
    mi = (pi*V)/(R_g*T0)
    p0c = (((R_g* T0)/V) * (mi + dmt*t)) * (10**-6) #[MPa]
    p0c = [p if p < 0.5 else 0.5 for p in p0c]  # Max 5[MPa]
    # discharge
    p0d =( (1 + (((gamma - 1)/2)*(Ae*sigma*sqrt(R * T0i))/V)*t)**((-1)*2*gamma/(gamma-1))*p0i ) * (10**-6)
    # total pressure
    p0 = p0c + p0d
    plot(t,p0)

        
##### VISUALIZATION AREA #########
title('TANK PRESSURE TRANSITION BY AIR DISCHARGE')
legend(('1L','10L','20L'),'upper right')
xlabel('t [sec]')
ylabel('p0 [MPa]')
savefig('./image/result-1.png')
show()

