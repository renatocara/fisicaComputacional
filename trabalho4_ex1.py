
from math import tan, sqrt, pi, atan, sin, sinh, cos, cosh
import matplotlib.pyplot as plt
import numpy as np

m=9.1094e-31 #eV
w=1.0e-9 #m
V=20.0 #V
h=4.135667696e-15 #eV
hb=h/(2.0*pi)
'''
Define o conunto de funções

Retorna a função de acordo com o índice e não o valor dela
'''
def F(i):
   
    functions_set = {
        0:lambda E:((V-E)/E)**(1/2),
        1:lambda E:-((E/(V-E))**(1/2)),
    }
    return functions_set[i%2]

def F_geral(Ei):
    return lambda E: abs(complex(tangent(((w**2 * m * Ei(E))/(2*hb**2))**(1.0/2.0))))

def F_e(i):
    return lambda E: F_geral(F(i))(E) - F(i)(E)


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
    '''Approximate solution of f(x)=0 on interval [a,b] by bisection method.

    Parameters
    ----------
    f : function
        The function for which we are trying to approximate a solution f(x)=0.
    a,b : numbers
        The interval in which to search for a solution. The function returns
        None if f(a)*f(b) >= 0 since a solution is not guaranteed.
    N : (positive) integer
        The number of iterations to implement.

    Returns
    -------
    x_N : number
        The midpoint of the Nth interval computed by the bisection method. The
        initial interval [a_0,b_0] is given by [a,b]. If f(m_n) == 0 for some
        midpoint m_n = (a_n + b_n)/2, then the function returns this solution.
        If all signs of values f(a_n), f(b_n) and f(m_n) are the same at any
        iteration, the bisection method fails and return None.

    Examples
    --------
    >>> f = lambda x: x**2 - x - 1
    >>> bisection(f,1,2,25)
    1.618033990263939
    >>> f = lambda x: (2*x - 1)*(x - 3)
    >>> bisection(f,0,1,10)
    0.5
    '''
    if f(a)*f(b) >= 0:
        print("Bisection method fails.")
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
            print("Found exact solution.")
            return m_n
        else:
            print("Bisection method fails.")
            return None
    return (a_n + b_n)/2


E = np.linspace(1, 30, 5000)

for i in range(6):
    y = []
    x = []
    f = F_geral(F(i))
    f_diff = F_e(i)
    for e in E:
        try:
            y.append(f(float(e)))
            #y.append(f_diff(float(e)))
            x.append(float(e))
            e_re = f_diff(float(e))
            if abs(e_re) < 0.001:
                print(e_re, e, i)
        except:
            print("Error")

    plt.plot(x, y , label='E_{}'.format(i))
    plt.ylim(bottom = -0.02, top=0.02)
#plt.plot(E, list(map(F(0), E)) , label='Nivis de energia Pares')
#plt.plot(E, list(map(F(1), E)) , label='Nivis de energia Impares')
#plt.ylim(bottom = -20.0, top=20.0)
plt.xlabel('eV')
plt.ylabel('Qtd')

plt.title("Energias")

plt.legend()

plt.show()


print(str(F(2)(2)))