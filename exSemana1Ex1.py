import math as m

'''
Um satélite deve ser lançado em uma órbita circular em torno da Terra, 
de forma que complete uma volta ao redor do planeta a cada T segundos.

Mostre que a altitude h do satélite acima da superfície da Terra deve ser 
h=(GMT24π2)1/3−R,
sendo G=6.67×10−11 m2kg−1s−2 a constante gravitacional de Newton, M=5.97×1024 kg 
a massa da Terra e R=6371 m seu raio médio.
Escreva um programa que peça ao usuário para digitar o valor desejado de T e em 
seguida calcule e imprima a altitude correta em metros.
Utilize seu programa para calcular as altitudes de satélites que orbitam a Terra 
uma vez por dia (os chamados "satélites geossíncronos" ), a cada 90 minutos e a 
cada 45 minutos. O que você conclui a partir dos dois últimos cálculos?
Tecnicamente, um satélite geossíncrono orbita a Terra uma vez por dia sideral, 
que corresponde a 23.93 horas, e não a 24 horas. Qual é a razão disso, e que 
diferença isso causa na altitude do satélite?
Forneça um arquivo PDF com suas respostas teóricas e o arquivo do seu programa 
em Python nos campos abaixo.

'''
#Constantes
G=6.67E-11
M=5.97E24
R=6371000 #metros

#Valor inputado T
def h(t):
    return ((G*M*(t**2))/(4.0 * (m.pi**2)) )**(1.0/3.0)-R


T=24*60**2 #float(input("Digite o valor de T em minutos"))

T1=45*60
T2=90*60
print("Para T={} minutos a altura h é : {:.2f} metros (O raio da orbita é menor que o raio da terra o que indica que a orbita geossíncrona nessa velocidade é impossível) ".format(45, h(T1)))
print("Para T={} minutos a altura h é : {:.2f} metros".format(90, h(T2)))
print("Para T=24 horas a altura h é : {:.2f} metros".format(h(T)))

Tinput = float(input("Digite o valor de T em minutos"))

print("Para o valor informado  {:.0f} minutos a altura h é : {:.2f} metros".format(Tinput, h(Tinput*60)))