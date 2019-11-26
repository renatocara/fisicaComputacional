
from math import tan, sqrt, pi, atan, sin, sinh, cos, cosh, nan
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



E = np.linspace(0, E_max, 300000)

f_par = F(0)
f_impar = F(1)
F_geral(lambda x: x)

x = []
y = []
par_x = []
par_y = []
impar_x = []
impar_y = []
roots_x = []
roots_y = []

for e in E:
    _x = float(e)
    try:
        _y = F_geral(lambda x: x)(_x)

        _y_par = complex(f_par(_x)).real
        _t_impar = complex(f_impar(_x)).real
        
        par_y.append(_y_par)
        par_x.append(_x)
        
        impar_y.append(_t_impar)
        impar_x.append(_x)
        
        #Remove a descontinuidade
        if abs(_y) < 1000:
            y.append(_y.real)
        else:
            y.append(nan)

        x.append(_x)
        epsilon = 0.1
        
        if _x > 3.7e-20 and _x < 0.1e-18:
            epsilon = 0.1
        else :
            epsilon = 0.001

        #Acha as raizes da eq
        if _x < treshold_niveis and (abs(_y - _y_par) <= epsilon or abs(_y - _t_impar) <= epsilon) :
            
            if len(roots_y) < 1 or abs(_y - roots_y[-1]) > 0.1:
                roots_y.append(_y.real)
                roots_x.append(_x)
                

    except:
        #Remove a descontinuidade
        x.append(_x)
        y.append(nan)
    
plt.plot(par_x, par_y , label='√V-E/E')
plt.plot(impar_x, impar_y , label='√E/V-E')
plt.plot(x, y , label='tan√w²mEᵢ/2ℏ²')
plt.ylim(bottom = -7.0, top=14.0)
plt.scatter(roots_x, roots_y, label="Níveis de energia")
plt.xlabel('Joules')
plt.ylabel('Joules')
plt.grid( linewidth=0.2)
plt.title("Energias")

plt.legend()

print("*"*80)
print("Níveis de energia")
print("")
print("{:3}\t{:5}".format("Nível", "Energia"))
for n in range(len(roots_y)):
    print("{}\t{:.2f}eV".format(format(n+1, '03'), roots_x[n]/eV))
print("*"*80)
plt.show()


for n in roots_x:
    print(n)