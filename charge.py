#!/usr/bin/env python
#-*- coding:utf-8 -*-

#*** TANK PRESSURE SIMULATION ***
#*** AUTHOR: SHOHEI AOKI ********
#*** PROGRAMMED: 22 JUL 2015 ****

from pylab import *

##### PARAMETER AREA ############
gamma = 1.4
M = 32 * 0.8 + 14 * 0.2 # O2: 80%, N2: 20%
R0 = 8.314 #(J/mol dot K)
T0 = 24 + 273.15 #[K}
pa = 0.1013*(10**6) #[Pa]: Atmospheric pressure
R = R0/M
DISCHARGE_AIR = 42 #[l/min], ref:http://www.airbrush.co.jp/shop/products/detail.php?product_id=1296
dVs1 = DISCHARGE_AIR*0.001/60 #[m3/s]
V = 1/1000.0 #[m3]: tank volume, 1L
pi = pa

##### SIMULATION TO CHARGE TANK ##
t = arange(0.01,100,0.01) # 10 sec 
dmt = ((pa*dVs1)/(R*T0))       # [kg/s]: mass flow rate at atmospheric pressure 
V_array = [1/1000.0, 10/1000.0, 20/1000.0]
for V in V_array:
    mi = (pi*V)/(R*T0)
    p0 = (((R* T0)/V) * (mi + dmt*t)) * (10**-6) #[MPa]
    p0 = [p if p < 0.5 else 0.5 for p in p0]  # Max 5[MPa]
    plot(t,p0)

##### VISUALIZATION AREA #########
title('TANK CHARGING BY COMPRESSOR')
legend(('1L', '5L', '10L'), 'upper right')
xlabel('t [sec]')
ylabel('p0 [MPa]')
ylim([0,0.6])
savefig('./image/tank-charge.png')
show()

