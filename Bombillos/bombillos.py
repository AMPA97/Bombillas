def habitacion_iluminada(habitacion_ob,renglon,columnas):
#adelante
    for k in range(0,renglon):
        i=0
        while i<columnas:
            if habitacion_ob[k][i]=="B":
                j=i+1
                while j<columnas and (habitacion_ob[k][j]==0 or habitacion_ob[k][j]=="i"):
                    habitacion_ob[k][j]="i"
                    j=j+1                
            i=i+1

#atraz i=1,j=i-1,j=j-1
    for k in range(0,renglon):#rellenar atraz
        i=1
        while i<columnas:
            if habitacion_ob[k][i]=="B": 
                j=i-1
                while j>-1 and (habitacion_ob[k][j]==0 or habitacion_ob[k][j]=="i"):
                    habitacion_ob[k][j]="i"
                    j=j-1
            i=i+1

#abajo
    for k in range(0,columnas):
        i=0
        while i<renglon:
            if habitacion_ob[i][k]=="B": 
                j=i+1
                while (j<renglon) and (habitacion_ob[j][k]==0 or habitacion_ob[j][k]=="i"):
                    habitacion_ob[j][k]="i"
                    j=j+1
            i=i+1

#arriba
    for k in range(0,columnas):
        i=1
        while i<renglon:
            if habitacion_ob[i][k]=="B": 
                j=i-1
                while j>-1 and (habitacion_ob[j][k]==0 or habitacion_ob[j][k]=="i"):
                    habitacion_ob[j][k]="i"
                    j=j-1
            i=i+1

def default(habitacion_ob,a,b):
     if habitacion_ob[a][b]==0:
        habitacion_ob[a][b]="B"

def mapeo(habitacion_ob, renglon,columnas,a,b,c):
    j=0
    while j<renglon-a:
        i=0
        while i<columnas-a:
            if habitacion_ob[j][i]==b and habitacion_ob[j+c][i+c]==0:
                habitacion_ob[j+c][i+c]="B"
                habitacion_iluminada(habitacion_ob=habitacion_ob, renglon=renglon,columnas=columnas)
            i=i+1
        j=j+1

def mostrar_hab(habitacion_ob,renglon,columnas):
    k=0
    while k<renglon:
        l=0
        while l<columnas:
            if habitacion_ob[k][l]==1:
                habitacion_ob[k][l]="P"
            l=l+1
        k=k+1
    i=0    
    while i<renglon:
        print(habitacion_ob[i])
        i=i+1

def nbombillas(habitacion_ob, renglon):
    i=0    
    c=0
    while i<renglon:
        a=habitacion_ob[i].count("B")
        c=a+c
        i=i+1
    
    print("\n El numero de bombillas que necesitaremos es: "+ str(c))

def bombillas(habitacion_ob, renglon,columnas):
    
    default(habitacion_ob=habitacion_ob,a=0,b=0)
    default(habitacion_ob=habitacion_ob,a=renglon-1,b=columnas-1)
    habitacion_iluminada(habitacion_ob=habitacion_ob, renglon=renglon,columnas=columnas)
    mapeo(habitacion_ob=habitacion_ob,renglon=renglon,columnas=columnas,a=1,b=1,c=1)
    mapeo(habitacion_ob=habitacion_ob,renglon=renglon,columnas=columnas,a=0,b=0,c=0)
    mostrar_hab(habitacion_ob=habitacion_ob,renglon=renglon,columnas=columnas)
    nbombillas(habitacion_ob=habitacion_ob, renglon=renglon)
    

def run():
    
    lectura=[]
    with open("./archivos/matriz.txt", "r",encoding="utf-8") as f:
            
       for linea in f:
            lectura.append(linea)

    renglones=len(lectura)
    
    dict_lectura={i:lectura[i] for i in range(0,renglones)}

    print("Numero de renglones: "+ str(renglones))

    columnas=len(lectura[1])-1
    print("Numero de columnas: "+str(columnas))
    habitacion_obscura=[]
    
    print("Aqui se muestra la habitacion obscura")
    j=0
    while j<renglones:
        renglon=[]
        i=0
        nrenglon=dict_lectura[j]
        while i<columnas:
            renglon.append(int(nrenglon[i]))
            i=i+1
        print(renglon)
        habitacion_obscura.append(renglon)
        j=j+1

    print("\n Podemos observar la habitacion iluminada\n Donde B es el bombillo \n i es el espacio iluminado\n y P las paredes\n")
    bombillas(habitacion_ob=habitacion_obscura, renglon=renglones,columnas=columnas)


if __name__=="__main__":
    run()