from vpython import vector, sphere, rate, cylinder, color, label, scene
from math import cos, sin, pi, sqrt
from numpy import arange
import time


#Constantes
R_esfera =1.
R_fio = 0.1
L_fio_base = 10
g=9.8

tmax=60*10 #60 segundos
#dt=T/100

cores_disponiveis = [color.red, color.orange, color.yellow, color.green, color.blue, color.purple]
espaco_enrtre_pendulos = 0.3 #Na direção Z

#Objetos
A=10*pi/180 #Amplitude inicial
theta=A
current_milli_time = lambda: int(round(time.time() * 1000))

class Pendulo:
    def __init__(self, R_fio, L, R_esfera,z_inicial, color):
        self.R_fio = R_fio
        self.L = L
        self.R_esfera = R_esfera
        self.x = L*sin(theta)
        self.y = -L*cos(theta)
        self.z = z_inicial
        self.esfera = sphere(radius=self.R_esfera, color=color, pos=vector(self.x,self.y,self.z))
        self.fio=cylinder(radius=self.R_fio, axis=self.esfera.pos)

#Ultimo pendulo
#T_u=tmax/51
#g*(T_u/(2*pi))**(2) = L_u
    #T=tmax/51

#Cria os pendulos
pendulos=[]
N = 15
Noc = 51
for i in range(N):
    
    T=tmax/(Noc + (N - i))
    L = g*(T/(2*pi))**(2)
    _z = -(2 *R_esfera + espaco_enrtre_pendulos)*(N-i)
    color = cores_disponiveis[i%len(cores_disponiveis)]
    print("Pendulo {} : _z= {:.2f} color {} Numero de ocilações {} Tamanho do pendulo L={} período T={}".format(i, _z, str(color), (Noc + (N - i)), L, T))
    pendulos.append(Pendulo(R_fio, L, R_esfera, _z,color ))

scene.forward = vector(0,0,1)
scene.center = vector(0,-20,0)
scene.range = 40
print("Myscene forward {}".format(scene.forward))
lab=label(pos=vector(-20,10,0), text='Tempo decorrido')
#laço da animação
initTime=current_milli_time()
for t in arange(0,tmax, 0.01):
    rate(1000)
    lab.text = 'Tempo decorrido {:.1f}/{:.1f} segundos'.format(t/10, tmax/10)
    for pend in pendulos:
        T=2*pi*sqrt(pend.L/g)
        omega=2*pi/T
        theta = A*cos(omega*t)
        pend.x = pend.L*sin(theta) 
        pend.y = -pend.L*cos(theta)
        pend.esfera.pos = vector(pend.x,pend.y,pend.z)
        pend.fio.axis = pend.esfera.pos

label(pos=vector(0,0,0), text='Processo concluido \n Todos os pendulos voltaram a sua posição inicial em {:.1f} segundos  '.format(tmax/10))