from functools import reduce
import math 
import matplotlib.pyplot as plt
from numpy import *

nm=1e-9
lamb= 400 #*nm #em metros


'''
Integrais 
'''

def trapezoidal(f, a, b, n):
    h = float(b - a) / n
    s = 0.0
    s += f(a)/2.0
    for i in range(1, n):
        s += f(a + i*h)
    s += f(b)/2.0
    return s * h



def gaussxw(N):

    # Initial approximation to roots of the Legendre polynomial
    a = linspace(3,4*N-1,N)/(4*N+2)
    x = cos(pi*a+1/(8*N*N*tan(a)))

    # Find roots using Newton's method
    epsilon = 1e-15
    delta = 1.0
    while delta>epsilon:
        p0 = ones(N,float)
        p1 = copy(x)
        for k in range(1,N):
            p0,p1 = p1,((2*k+1)*x*p1-k*p0)/(k+1)
        dp = (N+1)*(p0-x*p1)/(1-x*x)
        dx = p1/dp
        x -= dx
        delta = max(abs(dx))

    # Calculate the weights
    w = 2*(N+1)*(N+1)/(N*N*(1-x*x)*dp*dp)

    return x,w

def gaussxwab(N,a,b):
    x,w = gaussxw(N)
    return 0.5*(b-a)*x+0.5*(b+a),0.5*(b-a)*w




'''
Interal por Gauss
'''

def gaussQuad(f,a,b, N=8):
    x,w = gaussxwab(N, a, b)
    s = 0.0
    for k in range(N):
        s+= w[k]*f(x[k])
    return s


'''
Interal por Simpson
'''
def simps(f,a,b,N=200):
   
    if N % 2 == 1:
        raise ValueError("N deve ser par.")
    dx = (b-a)/N
    x = linspace(a,b,N+1)
    y = f(x)
    S = dx/3 * sum(y[0:-1:2] + 4*y[1::2] + y[2::2])
    return S


'''
Principal
'''

def k(lbda):
    return 2*math.pi/lbda

def J_int(m, x ):
    return lambda th: cos(m*th - x*sin(th))

def J(m, intMethod=simps, N=200):
    return lambda x: (1/math.pi) * intMethod(J_int(m, x), 0.0, math.pi, N)

def I(r):
    return (J(1)(k(lamb)*r)/(k(lamb)*r))**2

def itemA():
    for m in range(3):
        x = linspace(0, 20, 100)
        J_m_simp = J(m, simps, 1000)
        J_m_qg = J(m, gaussQuad, 100)
        y_Simp = list(map(J_m_simp, x))
        y_GQ = list(map(J_m_qg, x))
        plt.plot(x,y_Simp, label='J_{} Simpson'.format(m))
        plt.plot(x, y_GQ, label='J_{} Quad. Gauss '.format(m))

    plt.xlabel('X')
    plt.ylabel('Jₘ(x)')

    plt.title("Funções de Bessel por duas diferentes formas de integração")

    plt.legend()

    plt.show()

itemA()
