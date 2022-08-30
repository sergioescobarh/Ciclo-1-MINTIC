Azona=float(input())
Av=int(input())
tn=str(input())
Adeseada=Azona-(26600*Av)



if tn=="a":
    Cn=47800
elif tn=="b":
    Cn=60600
elif tn=="c":
    Cn=1800
elif tn=="d":
     Cn=33100
elif tn=="e":
    Cn=24000
else:
    print("error en los datos")

An=Adeseada/Cn


if An<0:
    Anr=0
else:
   Anr=int(An) +1


if Av<0:
   print("error en los datos")
else:
  print(Anr)
