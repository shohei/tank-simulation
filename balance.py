from pylab import *
gamma = 1.4
pa = 0.1013*(10**6) #[Pa]
de = 2 #[mm]
Ae = pi*(de*0.001/2)*(de*0.001/2)#[m2]
T0 = (24 + 273.15) # Room temperature
R = 289 # J/(kg dot K)
V = 1/1000.0 #1L as [m3]
sigma = sqrt(gamma*((2/(gamma+1))**((gamma+1)/(gamma-1)))) # critical flow efficient
Vs = 42/60.0*0.001 #[m3] 

a = sqrt((R*T0)**3)
b = (Ae*sigma*Vs*pa) #* (10**-6) #[MPa]
p_tank = a/b
print a,b,p_tank
