cmed1=int(input())
cmed2=int(input())
pacientes=0
pacientes1=0
pacientes2=0
while cmed1>0 and cmed2>0:
   ayunas=str(input())
   glucosa=float(input())
   pacientes=pacientes+1
   if  ayunas=="si":
    if glucosa<0.44:
        Categoria=("hipoglusemia")
        
        tmed=2
        cmed2=cmed2-5
        pacientes2=pacientes2+1
    
    elif glucosa>0.44 and glucosa<0.61:
        Categoria=("normal")
        
        tmed=0


    elif glucosa>0.61 and glucosa<0.7:
         Categoria=("elevado")
         
         tmed=1
         cmed1=cmed1-4
         pacientes1=pacientes1+1
    else:
        Categoria=("diabetes")
        
        tmed=1 
        cmed1=cmed1-9
        pacientes1=pacientes1+1

   elif ayunas=="no":
    if glucosa<0.78:
       Categoria=("normal") 
       
       tmed=0

    elif glucosa>0.78 and glucosa<1.1:
        Categoria=("elevado")
        
        tmed=1
        cmed1=cmed1-10
        pacientes1=pacientes1+1

    elif glucosa>1.1:
        Categoria=("diabetes")
        
        tmed=1
        cmed1=cmed1-15
        pacientes1=pacientes1+1
        
    else:
        r=0
   else:


     r=1


   per1=pacientes1*100/pacientes
   
   per2=pacientes2*100/pacientes

   

print(pacientes)
print(pacientes1)
print(float('{0:.2f}'.format(per1)))
print(pacientes2)
print(float('{0:.2f}'.format(per2)))
   