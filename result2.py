from pylab import *

##### PARAMETER AREA ############
gamma = 1.4
pa = 0.1013*(10**6) #[Pa]
p0i = 5*pa #[Pa]
#charge
M = 32 * 0.8 + 14 * 0.2 # O2: 80%, N2: 20%
R0 = 8.314 #(J/mol dot K)
T0 = 24 + 273.15 #[K}
R = R0/M
DISCHARGE_AIR = 42 #[l/min], ref:http://www.airbrush.co.jp/shop/products/detail.php?product_id=1296
Vs1 = DISCHARGE_AIR*0.001/60 #[m3/s]
#discharge
de = 2 #[mm]
Ae = pi*(de*0.001/2)*(de*0.001/2)#[m2]
R_kg = 289 # J/(kg dot K)
# V = 1/1000.0 #1L as [m3]
sigma = sqrt(gamma*((2/(gamma+1))**((gamma+1)/(gamma-1)))) # critical flow efficient

t = arange(0,100,0.01)

# V = 1/1000.0 #[m3]: 1L
V_array = [1/1000.0,10/1000.0,20/1000.0,30/1000.0,40/1000.0,50/1000.0]
for V in V_array:
    k1 = ((R*T0)/V) * ((Ae*sigma)/(sqrt(R_kg*T0)))
    k2 = pa * Vs1 / V
    E = e**(-1.0*k1*t)
    pt = ((k2/k1)*(1-E)+p0i)*E
    # pt = (k2/k1)*(0.5*(10**6)-e**(-1.0*k1*t))*(e**(-1.0*k1*t)) #[Pa]
    plot(t,pt*(10**-6))

##### VISUALIZATION AREA #########
title('TANK PRESSURE TRANSITION BY AIR DISCHARGE')
legend(('1L','10L','20L','30L','40L','50L'),'upper right')
xlabel('t [sec]')
ylabel('p0 [MPa]')
savefig('./image/result-2.png')
show()

