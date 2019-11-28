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

def gaussQuad(f,a,b, N=4):
    x,w = gaussxwab(N, a, b)
    s = 0.0
    for k in range(N):
        s+= w[k]*f(x[k])
    return s


'''
Interal por Simpson
'''
def simps(f,a,b,N=100):
   
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

def J(m, intMethod=simps):
    return lambda x: (1/math.pi) * intMethod(J_int(m, x), 0.0, math.pi)

def I(r):
    return (J(1)(k(lamb)*r)/(k(lamb)*r))**2

def itemB():
    #Um micrometro são 1000 nanometros, então faço o gráfico em escala de nanometros
    x = linspace(-1000, 1000, 100)
    y = linspace(-1000, 1000, 100)
    mat=zeros((100,100))
    rMax = 0.0
    for _x in range(len(x)):
        for _y in range(len(y)):
            r = sqrt(x[_x]**2 + y[_y]**2)
            if r==0:
                mat[_x][_y] = 1.0/2.0
            else:
                i = I(r)
                mat[_x][_y] = i
                if i > rMax:
                    rMax = i

    #plt.scatter(x, y)
    plt.xlabel('nm')
    plt.ylabel('nm')
    #plt.axis([-1000, 1000])
    plt.ylim(-1000, 1000)
    plt.xlim(-1000, 1000)
    
    plt.imshow(mat, cmap='hot', interpolation='nearest', vmin=0, vmax = rMax, extent=[-1000,1000,-1000,1000])
    plt.show()



itemB()