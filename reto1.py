
ayunas=str(input())
glucosa=float(input())
if  ayunas=="si":
    if glucosa<0.44:
        Categoria=("hipoglusemia")
        print(Categoria)
    elif glucosa>0.44 and glucosa<0.61:
        Categoria=("normal")
        print(Categoria)
    elif glucosa>0.61 and glucosa<0.7:
         Categoria=("elevado")
         print(Categoria)
    else:
        Categoria=("diabetes")
        print(Categoria)
elif ayunas=="no":
    if glucosa<0.78:
       Categoria=("normal") 
       print(Categoria)
    elif glucosa>0.78 and glucosa<1.1:
        Categoria=("elevado")
        print(Categoria)
    elif glucosa>1.1:
        Categoria=("diabetes")
        print(Categoria)
    else:
        print("error en los datos")
else:
  print("error en los datos")
