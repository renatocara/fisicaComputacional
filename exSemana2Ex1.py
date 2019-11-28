from numpy import array, dot

#Definindo as matrizes de pauli
sigma = {
    "x": array([
            [0,1],
            [1,0]
         ], complex),
    "y": array([
            [0,-1j],
            [1j,0]
         ], complex),
    "z":array([
            [1,0],
            [0,-1]
        ], complex)
}

print("Imprimindo as matrizes de Pauli")
for k in sigma:
    print('\n Matriz σ{}:'.format(k))
    for i in range(len(sigma[k])):
        print(sigma[k][i]) #"{} {}".format(sigma[k][i][0], sigma[k][i][1]))


print("Resultados dos produtos das matrizes de Pauli")

r=(1/2j)*array([ sigma['x'], sigma['y']], complex)
r1=(1/2j)*array([ sigma['y'], sigma['z']], complex)
r2=(1/2j)*array([ sigma['z'], sigma['y']], complex)

print(r)
print(r1)
print(r2)