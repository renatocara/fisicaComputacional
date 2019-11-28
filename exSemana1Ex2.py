'''
Um problema bem conhecido em mecânica quântica envolve uma partícula de massa m 
que encontra uma barreira unidimensional como a mostrada na figura abaixo.



A partícula, com energia cinética inicial E e vetor de onda k1=2mE−−−−√/ℏ 
(que se relaciona ao momento da partícula, e em que ℏ corresponde à 
constante de Planck dividida por 2π), incide a partir da esquerda e 
encontra um degrau súbito na energia potencial, de altura V, na 
posição x=0. Resolvendo a equação de Schrödinger, pode-se mostrar que 
quando E>V a partícula pode (a) ultrapassar o degrau, seguindo adiante, 
caso em que sua energia cinética diminui para E−V e seu vetor de onda 
diminui para k2=2m(E−V)−−−−−−−−−√/ℏ, ou (b) ser refletida de volta, mantendo 
sua energia cinética e a magnitude de seu vetor de onda. As probabilidades 
T e R para transmissão e reflexão são dadas por 
T=4k1k2(k1+k2)2,R=(k1−k2k1+k2)2.

Suponha que a partícula tenha massa igual à massa do elétron, m=9.11×10−31 kg, 
e energia E=10 eV, encontrando uma barreira de potencial de altura V=9 eV. 
Escreva um programa em Python para calcular e imprimir as probabilidades de 
transmissão e reflexão utilizando as fórmulas acima.


'''
import math as m

J=1.6022e-19
eV=1.0 #assumindo unidade de medida em eV
E=10.0*eV
V=9.0*eV
M=9.11E-31
h=4.135E-15 * eV
h_r=h/(m.pi * 2.0)
k1=m.sqrt(2*M*E)/h_r
k2=m.sqrt(2*M*(E-V))/h_r
T=(4*k1*k2)/(k1+k2)**2

R=((k1-k2)/(k1+k2))**2

print("Para E={:.2f}eV  e V={:.2f}eV é : T={:.2f} (probabilidade de transmissão) e R={:.2f} (Probabilidae de reflexão)".format(E, V, T, R))
