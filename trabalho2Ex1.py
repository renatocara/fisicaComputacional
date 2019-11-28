import numpy as np
from pylab import plot, show, scatter, xlabel, ylabel, xlim, ylim


''''
Para um dado valor complexo de c, parta de z=0 e itere a equação. 
Se o módulo |z| do valor resultante tornar-se em algum momento 
maior do que 2, então o ponto no plano complexo na posição c 
não está no conjunto de Mandelbrot; caso contrário, 
o ponto está no conjunto de Mandelbrot. 
'''
def mandelbrot(c,N):
    z = c
    for n in range(N):
        if abs(z) > 2: #n não está no conjunto de Mandelbrot
            return n #Retorna para plotar 
        z = z*z + c
    return 0 # Zero indica que não é um


def conjunto_maldebrot():
    N = 1000
    maxN = 0
    S_x = np.linspace(-2, 2, N)
    S_y = np.linspace(-2, 2, N)
    resultX = []
    resultY = []
    resultN = []
    for i in range(N):
        for j in range(N):
            n=mandelbrot(S_x[i] + 1j*S_y[j],N)
            resultX.append(S_x[i])
            resultY.append(S_y[j])
            resultN.append(n)
            if n > maxN:
                maxN = n
    return (resultX,resultY, resultN, maxN)

#colors = ['k','m', 'r', 'b', 'c', 'g', , , ] #Paleta de cores
#colors = ['k','tab:brown', 'tab:red', 'tab:orange', 'y', 'tab:green',"tab:cyan" , "b" , "tab:purple" ] #Paleta de cores
colors = ['k','m', "tab:purple", "b","tab:cyan",'tab:green','y', 'tab:orange' , 'tab:red',   'tab:brown'] #Paleta de cores
mset = conjunto_maldebrot()
c = 0
maxN = mset[3] #N máximo encontrado
while len(colors) > 0 and c < maxN:
    x = []
    y = []
    
    for i in range(len(mset[2])):
        #plotando com n ao invés de log de n pois o número de cores é limitado e no final não faz diferença
        if (c == mset[2][i] and len(colors) > 1 ) or (len(colors)==1 and mset[2][i] > c) :
            x.append(mset[0][i])
            y.append(mset[1][i])
    if len(x)> 0:
        color = colors.pop(0)   
        scatter(x,y, c=color,edgecolor=color, s=0.1)
    c += 1 # python >= 3 ?
show()
print(mset)