from numpy import array, dot

#Escreva um programa que utilize um laço while para criar uma lista 
# de todos os números inteiros de 1 a 100 que não sejam múltiplos de 4.
m=[]
z=1
while z <= 100: #Era mais simples fazer for z in  range([1:100]) mas o exercicio especificou o while
        if z%4!=0:
                m.append(z)
        z=z+1

#converta essa lista para um vetor (um objeto array) de 
# elementos reais e imprima o resultado;

a=array(m, int)

#imprima o tamanho desse vetor;
print("Tamanho do array {}".format(len(a)))
#produza, com um único comando, um segundo vetor que 
# corresponda à raiz quadrada de cada elemento do primeiro vetor;

a2=a**2

#defina um terceiro vetor igual à soma dos dois primeiros;
a3=a2+a

#determine, com um único comando, a soma dos elementos desse terceiro vetor;
s=a3.sum()

#imprima o resultado dessa soma.
print(s)