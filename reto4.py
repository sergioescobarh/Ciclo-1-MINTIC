




n=int(input())  #sucursales
k=int(input())     #tipos de medicamentos
m=int(input())  #Cantidad de pacientes

while n<1 or k<1:  #si cantidad sucursales es menor a 1 o si número de tipos de medicamento es menor a 1 se debe leer nuevamente 
 n=int(input())
 k=int(input())

exmed=[]  # creación Matriz de existencias de medicamentos

i=0
j=0

for i in range(0,n,1):     #para n sucursales leer cantidad existencias de tipos de medicamentos    *(revisar n+1) *(falta el i=i+1)
 fila=[]                   #creción filas de la matriz exmed
 for j in range(0,k,1):

    existencias=int(input())

    fila.append(existencias)
   
 exmed.append(fila)




   


for u in range(0,m,1):                                   #preguntas a los m pacientes
    nsucursalint=int(input())
    tmedicamento=int(input())
    cantmed=int(input())
    ps=int(input())
    pd=int(input())

    
    
    if ps<83 and pd<48:
        categoria="Hipotension"
        
        entrega="si"
        

    elif ps<124 and ps>83 and pd<66 and pd>48:
        categoria="Optima"
        
        entrega="no"
        

    elif ps<141 and ps>124 and pd<83 and pd>66:
         categoria="Normal"
         
         entrega="no"

    elif  ps<158 and ps>141 and pd<97 and pd>83:
        categoria="Pre HTA"
        
        entrega="si"
        
    
    elif ps<186 and ps>158 and pd<112 and pd>97:
        categoria="Hipertension grado 1"
        
        entrega="si"
    
    elif ps<197 and ps>186 and pd<128 and pd>112:
        categoria="Hipertension grado 2"
       
        entrega="si"
        

    elif ps>=197 and pd>=128:
        categoria="Hipertension grado 3"
        
        entrega="si"
        
    
    elif ps>=159 and pd<94:
        categoria="HTA solo Sistolica"
        
        entrega="si"
 
    if entrega=="si":
       exmed[nsucursalint-1][tmedicamento-1]=exmed[nsucursalint-1][tmedicamento-1]-cantmed
  



#outcomes

for t in range(0,n,1):
   print(t+1)                #•	El número de la sucursal
   h=[]
   for y in range(0,k,1):

      l=exmed[t][y]
      h.append(l)

   rm=int(min(h))
   cc=h.index(rm)
   print(cc+1 , rm)                # tipmed menor y min

   RM=int(max(h))
   CC=h.index(RM)
   print(CC+1 , RM)                #tipmed mayor y max
   print("0.00" , "0.00" , "0.00")
   print("0.00")






 