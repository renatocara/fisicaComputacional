import math as m
import json

#Constantes
G=6.67E-11
Ms=1.9891E30

def calculaPropriedadesOrbita(v1, l1):

    K=(2*G*Ms)/l1
    #v2²-(1/v1)*K*v2- (v1²-K)=0
    #Baskara 
    A=1.0
    B=-(1.0/v1)*K
    C=-(v1**2-K)
    solucoes=[(-B + m.sqrt(B**2-4*A*C))/(2*A), (-B - m.sqrt(B**2-4*A*C))/(2*A)]
    v2= min(solucoes)
    print("Soluções: ", solucoes)
    
    l2=(l1*v1)/v2

    #Semi eixo maior
    a=(1/2)*(l1+l2)

    #Semi eixo menor
    b=m.sqrt(l1*l2)

    #Período orbital
    t=(2*m.pi*a*b)/(l1*v1)

    #excentricidade orbital
    e=(l2-l1)/(l2+l1)

    return {'l2':l2, 'v2':v2, 'T':t , 'e':e}

def printDic(d):
    acc = ""
    for var in d:
        acc+= "\n\t{}={:.4}".format(var, d[var])  
    return acc

def calculaEImprimeDadosDaOrbitaParaObjeto(dicDados):
    _v1=dicDados['v1']
    _l1=dicDados['l1']
    print("Para o objeto {} com v1= {:.2} l1={:.2} obtemos as propriedades: {}".format(dicDados['name'], _v1,_l1, printDic(calculaPropriedadesOrbita(_v1,_l1 ))))


calculaEImprimeDadosDaOrbitaParaObjeto({'v1':3.0287E4, 'l1':1.4710E11, 'name':'Terra'})
calculaEImprimeDadosDaOrbitaParaObjeto({'v1':5.4529E4, 'l1':8.7830E10, 'name':'Cometa Halley'})