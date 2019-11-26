
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


def bisection(f,a,b,N):
  
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

#Pontos para busca binária obtidos através do gráfico gerado por trabalho4_ep1.py
raizes = [
5.1e-21
,1.21e-19
,3.0e-19
,5.8e-19
,9.8e-19
,1.4e-18
,2.0e-18
,2.8e-18
,3.3e-18
,4.0e-18,
]


a = 0.0
b = raizes[0]
n = 1
print(80*"-")
print("Usando busca binária achamos as seguintes raízes")
print(80*"-")
print("N\tEnergia (J)\t\tEnergia (eV)")
for i in range(len(raizes) - 2):
    a = raizes[i]
    
    b = (raizes[i+1])
    r = bisection(lambda x: F_e(0)(x).real,a,b, 8000)
    if r is None:
        r = bisection(lambda x: F_e(1)(x).real,a,b, 8000)
    
    if r is not None:
        
        print("n= {}\t{}\t\t{:.2f}eV ".format(n, r, r/eV))
        n = n+1
    #print(raizes_originais[i], "{:.3}".format(raizes_originais[i]/eV),  r, "{:.3}".format(r/eV))
    a = raizes[i]
    b = raizes[i+1]

