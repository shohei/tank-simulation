from pylab import *
import numpy as np

##### BEGIN PARAMETER AREA ############
gamma = 1.4
pa = 0.1013*(10**6) #[Pa]
p0i = 5*pa #[Pa]
#CHARGE
M = 32 * 0.8 + 14 * 0.2 # O2: 80%, N2: 20%
R0 = 8.314 #(J/mol dot K)
T0 = 24 + 273.15 #[K}
R = R0/M
DISCHARGE_AIR = 42 #[l/min], ref:http://www.airbrush.co.jp/shop/products/detail.php?product_id=1296
Vs1 = DISCHARGE_AIR*0.001/60.0 #[m3/s]
#DISCHARGE
# de = 2 #[mm]
de = 1.7 #[mm]
# de = 6 #[mm]
Ae = pi*(de*0.001/2)*(de*0.001/2)#[m2]
R_kg = 289 # J/(kg dot K)
# V = 1/1000.0 #1L as [m3]
sigma = sqrt(gamma*((2/(gamma+1))**((gamma+1)/(gamma-1)))) # critical flow efficient
##### PARAMETER AREA END ############

dt = 0.01 #[sec]
tTotal = 300 #[sec]
# V = 1/1000.0 #[m3]: 1L
V_array = [1/1000.0,10/1000.0,20/1000.0,30/1000.0,40/1000.0,50/1000.0]
# V_array = [1/1000.0,20/1000.0,50/1000.0]
# V_array = [1/1000.0,50/1000.0]

# V = 1/1000.0
for V in V_array:
    pt = np.array([])
    pt = np.append(pt,p0i) 
    ts = np.array([0])
    k1 = ((R*T0)/V) * ((Ae*sigma)/(sqrt(R_kg*T0))) *1000 # x1000 is because of mass unit: kgram or gram
    # k1 = ((R*T0)/V) * ((Ae*sigma)/(sqrt(R_kg*T0))) #working bad, this is default 
    k2 = pa * Vs1 / V
    for i in xrange(int(tTotal/dt)):
        p_n = pt[-1]
        if p_n >= p0i:
            p_n_dot =  (-1.0)*k1*p_n
            p_n_dot_dot =  (-1.0)*k1*p_n_dot
            print 'compressor halted: ',i
        else:
            p_n_dot =  (-1.0)*k1*p_n + k2
            p_n_dot_dot =  (-1.0)*k1*p_n_dot
        p_n_1 = p_n + p_n_dot * dt + p_n_dot_dot*dt*dt
        pt = np.append(pt,p_n_1)
        ts = np.append(ts,dt*i)
    
    plot(ts,pt*(10**-6))

##### VISUALIZATION AREA #########
title('TANK PRESSURE TRANSITION BY AIR DISCHARGE')
legend(('1L','10L','20L','30L','40L','50L'),'upper right')
xlabel('t [sec]')
ylabel('p0 [MPa]')
ylim([0,0.6])
savefig('./image/final_pressure_depends_on_discharge_hole_size.pdf')
show()

