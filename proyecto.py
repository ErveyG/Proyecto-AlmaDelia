#Proyecto para la materia bases de datos
#Programa con la funcionalidad de descriptor de archivos


#Función encargada de manejar el archivo de texto
f = open("DB.txt", "r")
num_linea=0
est_temp=[]
while(True):
    linea = f.readline()
#Verifica que estemos leyendo la primer linea del archivo y obtiene una lista que maneja los datos del descriptor
    if num_linea==0:
        descriptor = linea.split(",")
        print(descriptor)
        tam_lista=len(descriptor)
        i=1
        while i<tam_lista:
            est_temp.append([descriptor[i]])
            i=i+3
    else:
        i=1
        j=0
        while i<tam_lista:
            atr=linea[int(descriptor[i+1]):int(descriptor[i+2])]
            est_temp[j].append(atr.strip())
            i=i+3
            j=j+1
    num_linea=num_linea+1
    if not linea:
        break
f.close()
orden=input("|")
orden_sin_comas=orden.replace(",","")
select=orden_sin_comas.split(" ")
if len(select)<1:
    if select[1]=="*":
        i=0
        while i<len(est_temp):
            j=0
            while j<len(est_temp[i]): 
                if(est_temp[i][j]==""):
                    print("NULL")
                else:
                    print(est_temp[i][j])
                j=j+1
            i=i+1
    else:
        k=1
        while k < len(select):
            i=0
            while i<len(est_temp):
                if est_temp[i][0]==select[k]:
                    j=0
                    while j<len(est_temp[i]): 
                        if(est_temp[i][j]==""):
                            print("NULL")
                        else:
                            print(est_temp[i][j])
                        j=j+1

                i=i+1
            k=k+1