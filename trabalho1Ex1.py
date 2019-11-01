from functools import reduce
import math 

'''
Escreva um programa para calcular e imprimir a constante de Madelung para o 
cloreto de sódio. Utilize um valor de L tão grande quanto possível, 
com o vínculo de que seu programa seja executado em um tempo razoável --- 
digamos em não mais que um minuto.
'''


L = int(1E2)#Valor máximo para executar em menos de um minuto
s=0.0
for i in range(-L,L):
    for j in range(-L,L):
        for k in range(-L,L):
            if i==0 and j==0 and k==0:
                continue
            s+=((-1)**(i+j+k))/math.sqrt(i**2 + j**2 + k**2)

print(s)

