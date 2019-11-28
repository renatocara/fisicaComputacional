from math import tan, sqrt, pi, nan
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.style
import numpy as np

mpl.style.use('seaborn-bright')




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


def F_e(i, E):
    return fEnergia(E) - f_energia_par_impar(i,E)



E = np.linspace(0, E_max, 1000)


x = []
y = []
par_x = []
par_y = []
impar_x = []
impar_y = []


for e in E:
    _x = float(e)
    if _x != V and _x != 0.0:
        _y = fEnergia(_x)

        _y_par = f_energia_par(_x)
        _y_impar = f_energia_impar(_x)
        
        par_y.append(_y_par)
        par_x.append(_x)
        
        impar_y.append(_y_impar)
        impar_x.append(_x)
        
        if abs(_y) < MAX:
            y.append(_y)
        else:
            y.append(nan)

        x.append(_x)
                

    
plt.plot(par_x, par_y , label='Par')
plt.plot(impar_x, impar_y , label='Impar')
plt.plot(x, y , label='Tangente')
plt.ylim(bottom = MAX*-1, top=MAX)
plt.xlabel('eV')
plt.ylabel('')
plt.grid()

plt.title('')

plt.legend()
plt.show()


