
from math import tan, sqrt, pi, atan, sin, sinh, cos, cosh
import matplotlib.pyplot as plt
import numpy as np


hb=4.135667696e-15/(2.0*pi)
w= 1.0e-9 
m=9.1094e-31/1.6022e-19
E_max = 20 
V=20.0 
MAX=8.0
def f_energia_par(E):
    return ((V-E)/E)**(1/2)

def f_energia_impar(E):
    return -((E/(V-E))**(1/2))

def f_energia_par_impar(i, E):
    if i%2==0:
        return f_energia_par(E)
    else:
        return f_energia_impar(E)



def fEnergia(Ei):
    return tan(complex((((w**2) * m * Ei)/(2*(hb**2)))**(1.0/2.0)).real)


def F_par(E):
    return fEnergia(E) - f_energia_par(E)

def F_impar(E):
    return fEnergia(E) - f_energia_impar(E)

def biseccao(f,a,b,N):
  
    if f(a)*f(b) >= 0:
        return None
    a_n = a
    b_n = b
    for n in range(1,N+1):
        m_n = (a_n + b_n)/2
        f_m_n = f(m_n)
        if f(a_n)*f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n)*f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            return m_n
        elif abs(f_m_n) <= 0.001:
            return m_n
        else:
            return None
    return (a_n + b_n)/2


limites = [
    0.04,
    0.7,
    2.0,
    3.8,
    6.7,
    9.33,
    13.0,
    17.0
    ]
a = 0.0
b = limites[0]
n = 1

print("Níveis de Energia")
for i in range(len(limites) - 1):
    a = limites[i]
    
    b = (limites[i+1])

    r = biseccao(F_par,a,b, 10000)
    if r is None:
        r = biseccao(F_impar,a,b, 10000)
    
    if r is not None:
        print(n, r)
        n = n+1

