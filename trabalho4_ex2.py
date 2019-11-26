
from math import tan, sqrt, pi, atan, sin, sinh, cos, cosh
import matplotlib.pyplot as plt
import numpy as np

eV=1.6022e-19 #joules
nm = 1.0e-9 #metros
c=3e8
m=9.1094e-31 #kg
w= 1.0 * nm 
V=20.0 * eV 
E_max = 30 * eV 
h=6.626e-34 #4.135667696e-15 #eV
hb=h/(2.0*pi)

#Solução paleativa de baixo custo alternativa para lidar com os pontos onde E>V e a curva fica complexa
treshold_niveis =  3.5e-18 #Ponto a partir do qual não é necessário mais contar os niveis 
def F(i):
    '''
    Define o conjunto de funções

    Retorna a função adequada de acordo com o índice e não o valor dela

    ⎰ f(x) =  √(V-E)/E   se i par
    ⎱ f(x) = -√E/(V-E)    se i impar

    '''
    functions_set = {
        0:lambda E:((V-E)/E)**(1.0/2.0),
        1:lambda E:-((E/(V-E))**(1.0/2.0)),
    }
    return functions_set[i%2]


def F_geral(Ei):
    '''
        tan√w²mEᵢ/2ℏ²
    '''
    return lambda E: complex(tangent((((w**2) * m * Ei(E))/(2*(hb**2)))**(1.0/2.0)))


def F_e(i):
    '''
    ⎰ f(x) = tan√w²mEᵢ/2ℏ² - √(V-E)/E       se i par
    ⎱ f(x) = tan√w²mEᵢ/2ℏ² + √E/(V-E)       se i impar
    '''
    return lambda E: F_geral(lambda x: x)(E) - F(i)(E)


def tangent(c):
    '''
    Calcula a tangente de um número complexo se aproveitando da identidade
    https://proofwiki.org/wiki/Tangent_of_Complex_Number 
    '''
    if isinstance(c, complex):
        a = c.real
        b = c.imag
        res = (sin(a) *cosh(b) + 1j * cos(a) * sinh(b))/(cos(a) *cosh(b) - 1j * sin(a) * sinh(b))
        return res
    else:
        return tan(c)


def bisection2(f,a,b,N):

    v = (b-a)/2.0
    y = f(v).real
    if abs(y) <= 0.001 :
        return v
    else:
        if y > 0:
            return bisection(f, a, v, N)
        else :
            return bisection(f, v, b, N)

def bisection(f, a, b, tol):
    c = (a+b)/2.0
    while (b-a)/2.0 > tol:
        if abs(f(c)) < 0.001:
            return c
        elif f(a)*f(c) < 0:
            b = c
        else :
            a = c
        c = (a+b)/2.0
        
    return c

raizes = [0.0,
 5.08379754599182e-20
,5.096615188717296e-20
,2.0336792389307965e-19
,4.567566985223284e-19
,8.089694985649952e-19
,1.257538927796426e-18
,1.796665002883343e-18
,2.4142350514501716e-18
,3.065643676812256e-18
]
a = 0.0
b = raizes[0]
for i in range(len(raizes) - 1):
    a = raizes[i]* 1.5
    b = (raizes[i+1])* 1.5
    r = bisection(lambda x: F_e(i)(x).real,a,b, 0.00001)
    print(raizes[i], "{:.3}".format(raizes[i]/eV),  r, "{:.3}".format(r/eV))
    a = raizes[i]
    b = raizes[i+1]

