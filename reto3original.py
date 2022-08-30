

from platform import mac_ver


n=int(input())
m=int(input())
while n<1:
 n=int(input())
 m=int(input())

eam=[]


for i in range(1,n+1,1):
    eamesc=int(input())
    while eamesc<0:
        eamesc=int(input())
    eam.append(eamesc)
    i=i+1

eamcopy=eam

    



for j in range(1,m+1,1):
    ns=int(input())
    
    ps=int(input())
    pd=int(input())
    j=j+1
    if ps<83 and pd<48:
        categoria="Hipotension"
        tmed=1
        nd=15
        eam[ns-1]=eam[ns-1]-15

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
        eam[ns-1]=eam[ns-1]-3
    
    elif ps<186 and ps>158 and pd<112 and pd>97:
        categoria="Hipertension grado 1"
        tmed=1
        nd=6
        eam[ns-1]=eam[ns-1]-6
    
    elif ps<197 and ps>186 and pd<128 and pd>112:
        categoria="Hipertension grado 2"
        tmed=1
        nd=18
        eam[ns-1]=eam[ns-1]-18

    elif ps>=197 and pd>=128:
        categoria="Hipertension grado 3"
        tmed=1
        nd=30
        eam[ns-1]=eam[ns-1]-30
    
    elif ps>=159 and pd<94:
        categoria="HTA solo Sistolica"
        tmed=1
        nd=24
        eam[ns-1]=eam[ns-1]-24

minn=int(min(eam))
r=eam.index(minn)
rt=r

maxx=int(max(eam))
y=eam.index(maxx)
yt=y
print(eam)
print(rt , minn)
print(yt , maxx)      


for k in range(1,n+1,1):

    percentage=(eam[k-1]*100/eamcopy[k-1])


    print(f"{k} {(percentage):.2f}%")
    k=k+1

#arreglar [765, 754, 402]

