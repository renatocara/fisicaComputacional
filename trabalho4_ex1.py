
from math import tan, sqrt, pi, atan
import matplotlib.pyplot as plt
import numpy as np

m= 9.1094e-31 #eV
w=1e-9 #m
V=20 #V
h=4.135667696e-15 #eV
hb=h/(2*pi)

def F(i):
    '''
    Define o conunto de funções

    Retorna a função de acordo com o índice e não o valor dela
    '''
    functions_set = {
        0:lambda E:((2*hb**2)/(w**2 *m)) * atan(sqrt((V-E)/E))**2,
        1:lambda E:((2*hb**2)/(w**2 *m)) * atan(-sqrt(E/(V-E)))**2,
    }
    return functions_set[i%2]

def F_geral(E):
    return tan((w**2 * m * E)/(2*hb**2))

E = np.linspace(1, 20, 100)

for i in range(6):
    plt.plot(E, list(map(F(i), E)) , label='E_{}'.format(i))


plt.xlabel('eV')
plt.ylabel('Qtd')

plt.title("Energias")

plt.legend()

plt.show()


print(str(F(2)(2)))