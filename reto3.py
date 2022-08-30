

from sys import ps1
from turtle import Vec2D


n=int(input())  #sucursales

m=int(input())  #Cantidad de pacientes

while n<1:  #si cantidad sucursales es menor a 1 se debe leer nuevamente 
 n=int(input())
 m=int(input())

vector_exictenciasmedicamentos=[]            #creacion vector existencias

for i in range(0,n,1):                       #leer existencias por cada sucursal
    existenciasmedicamento=int(input())

    while existenciasmedicamento<1:          #asegurar existencias mayores o iguales a 1
        existenciasmedicamento=int(input())

    vector_exictenciasmedicamentos.append(existenciasmedicamento)   #llenado de vector de existencias



for j in range (0,m,1):                    #sucursal en que se atendera,presion sis y dias de cada paciente # resta de existencias entregadas

    sucursal_atencion=int(input())
    ps=int(input())
    pd=int(input())

  # aqui poner ciclo para sucursal ingresada q no exista

    if ps<83 and pd<48:
        categoria="Hipotension"
        tmed=1
        nd=15
        vector_exictenciasmedicamentos[sucursal_atencion-1]=vector_exictenciasmedicamentos[sucursal_atencion-1]-15

    elif ps<124 and ps>83 and pd<66 and pd>48:
        categoria="Optima"
        tmed="ninguno"
        nd=0

    elif ps<141 and ps>124 and pd<83 and pd>66:
         categoria="Normal"
         tmed="ninguno"
         nd=0

    elif  ps<158 and ps>141 and pd<97 and pd>83:
        categoria="Pre HTA"
        tmed=1
        nd=3
        vector_exictenciasmedicamentos[sucursal_atencion-1]=vector_exictenciasmedicamentos[sucursal_atencion-1]-3
    
    elif ps<186 and ps>158 and pd<112 and pd>97:
        categoria="Hipertension grado 1"
        tmed=1
        nd=6
        vector_exictenciasmedicamentos[sucursal_atencion-1]=vector_exictenciasmedicamentos[sucursal_atencion-1]-6
    
    elif ps<197 and ps>186 and pd<128 and pd>112:
        categoria="Hipertension grado 2"
        tmed=1
        nd=18
        vector_exictenciasmedicamentos[sucursal_atencion-1]=vector_exictenciasmedicamentos[sucursal_atencion-1]-18

    elif ps>=197 and pd>=128:
        categoria="Hipertension grado 3"
        tmed=1
        nd=30
        vector_exictenciasmedicamentos[sucursal_atencion-1]=vector_exictenciasmedicamentos[sucursal_atencion-1]-30
    
    elif ps>=159 and pd<94:
        categoria="HTA solo Sistolica"
        tmed=1
        nd=24
        vector_exictenciasmedicamentos[sucursal_atencion-1]=vector_exictenciasmedicamentos[sucursal_atencion-1]-24

   
  
###faltan outputs
                                                  
    

