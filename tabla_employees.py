#Proyecto para la materia bases de datos
#Programa con la funcionalidad de descriptor de archivos
#Función encargada de manejar el archivo de texto
from numpy import append

est_temp=[]
def leerArchivo():
    f = open("DB.txt", "r")
    num_linea=0
    k=1
    while(True):
        linea = f.readline()
    #Verifica que estemos leyendo la primer linea del archivo y obtiene una lista que maneja los datos del descriptor
        if num_linea==0:
            descriptor = linea.split(",")
            tam_lista=len(descriptor)
            i=1
            est_temp.append([])
            while i<tam_lista:
                est_temp[0].append(descriptor[i])
                i=i+3
        else:
            est_temp.append([])
            i=1
            j=0
            while i<tam_lista:
                atr=linea[int(descriptor[i+1]):int(descriptor[i+2])]
                est_temp[k].append(atr.strip())
                i=i+3
                j=j+1
            k=k+1
        num_linea=num_linea+1
        if not linea:
            break
    est_temp.pop()
    f.close()
    return(num_linea)

#lee el archivo
num_linea=leerArchivo()
#parte del where
orden=input("|")
orden_sin_comas=orden.replace(",","")
select=orden_sin_comas.split(" ")
orden=input("|")
where=orden.split(" ",1)
seleccion=[]
seleccion.append(est_temp[0])

#verifica que pida una selección, en caso contrario da solo la proyección
if len(where)>=2:
    k=1
    if where[k].find(">=")!=-1:
        kaux=where[k].replace(" ","")
        var=kaux.split(">=")
        j=0
        while j<len(est_temp[0]):
            if est_temp[0][j]==var[0]:
                i=0
                while i<num_linea-1:
                    if est_temp[i][j]>=var[1]:
                        seleccion.append(est_temp[i])
                    i=i+1
            j=j+1
    elif where[k].find('<=')!=-1:
        kaux=where[k].replace(" ","")
        var=kaux.split("<=")
        j=0
        while j<len(est_temp[0]):
            if est_temp[0][j]==var[0]:
                i=0
                while i<num_linea-1:
                    if est_temp[i][j]<=var[1]:
                        seleccion.append(est_temp[i])
                    i=i+1
            j=j+1
    elif where[k].find('<>')!=-1:
        kaux=where[k].replace(" ","")
        var=kaux.split("<>")
        j=0
        while j<len(est_temp[0]):
            if est_temp[0][j]==var[0]:
                i=0
                while i<num_linea-1:
                    if est_temp[i][j]!=var[1]:
                        seleccion.append(est_temp[i])
                    i=i+1
            j=j+1
    elif where[k].find('!=')!=-1:
        kaux=where[k].replace(" ","")
        var=kaux.split("!=")
        j=0
        while j<len(est_temp[0]):
            if est_temp[0][j]==var[0]:
                i=0
                while i<num_linea-1:
                    if est_temp[i][j]!=var[1]:
                        seleccion.append(est_temp[i])
                    i=i+1
            j=j+1
    elif where[k].find('=')!=-1:
        kaux=where[k].replace(" ","")
        var=kaux.split("=")
        j=0
        while j<len(est_temp[0]):
            if est_temp[0][j]==var[0]:
                i=0
                while i<num_linea-1:
                    if est_temp[i][j]==var[1]:
                        seleccion.append(est_temp[i])
                    i=i+1
            j=j+1
    elif where[k].find('<')!=-1:
        kaux=where[k].replace(" ","")
        var=kaux.split("<")
        j=0
        while j<len(est_temp[0]):
            if est_temp[0][j]==var[0]:
                i=0
                while i<num_linea-1:
                    if est_temp[i][j]<var[1]:
                        seleccion.append(est_temp[i])
                    i=i+1
            j=j+1
    elif where[k].find('>')!=-1:
        kaux=where[k].replace(" ","")
        var=kaux.split(">")
        j=0
        while j<len(est_temp[0]):
            if est_temp[0][j]==var[0]:
                i=0
                while i<num_linea-1:
                    if est_temp[i][j]>var[1]:
                        seleccion.append(est_temp[i])
                    i=i+1
            j=j+1
    elif where[k].find('BETWEEN')!=-1:
        kaux=where[k].replace(" ","")
        var=kaux.split("BETWEEN")
        num=var[1].split("AND")
        j=0
        while j<len(est_temp[0]):
            if est_temp[0][j]==var[0]:
                i=0
                while i<num_linea-1:
                    if est_temp[i][j]>=num[0] and est_temp[i][j]<=num[1]:
                        seleccion.append(est_temp[i])
                    i=i+1
            j=j+1
    elif where[k].find('IS NULL')!=-1:
        kaux=where[k].replace(" ","")
        var=kaux.split("ISNULL")
        j=0
        while j<len(est_temp[0]):
            if est_temp[0][j]==var[0]:
                i=0
                while i<num_linea-1:
                    if est_temp[i][j]=="":
                        seleccion.append(est_temp[i])
                    i=i+1
            j=j+1
    elif where[k].find('NOT IN')!=-1:
        kaux=where[k].replace(" ","")
        var=kaux.split("NOTIN")
        var[1]=var[1].replace(",", " ")
        var[1]=var[1].replace("(", "")
        var[1]=var[1].replace(")", "")
        num=var[1].split(" ")
        print(num)
        j=0
        while j<len(est_temp[0]):
            if est_temp[0][j]==var[0]:
                i=0
                while i<num_linea-1:
                    h=0
                    band=0
                    while h<len(num):
                        if est_temp[i][j]==num[h]:
                            band=1
                        h=h+1
                    if band==0:
                        seleccion.append(est_temp[i])
                    i=i+1
            j=j+1
    elif where[k].find('IN')!=-1:
        kaux=where[k].replace(" ","")
        var=kaux.split("IN")
        var[1]=var[1].replace(",", " ")
        var[1]=var[1].replace("(", "")
        var[1]=var[1].replace(")", "")
        num=var[1].split(" ")
        j=0
        while j<len(est_temp[0]):
            if est_temp[0][j]==var[0]:
                i=0
                while i<num_linea-1:
                    h=0
                    while h<len(num):
                        if est_temp[i][j]==num[h]:
                            seleccion.append(est_temp[i])
                        h=h+1
                    i=i+1
            j=j+1
    k=k+1
else:
    seleccion=est_temp
#Parte del select
i=0
proyeccion=[]
if len(select)>=2:
    if select[1]=="*":
        while i<len(seleccion):
            j=0
            while j<len(seleccion[i]):
                if(seleccion[i][j]==""):
                    print("NULL", end=" ")
                else:
                    print(seleccion[i][j], end=" ")
                j=j+1
            print("")
            i=i+1
    else:
        k=1
        while k < len(select):
            i=1
            j=0
            while j<len(seleccion[0]):
                if seleccion[0][j]==select[k]:
                    proyeccion.append([])
                    proyeccion[0].append(seleccion[0][j])
                    while i < len(seleccion):
                        proyeccion.append([])
                        proyeccion[i].append(seleccion[i][j])
                        i=i+1
                j=j+1
            k=k+1
        i=0
        while i<len(seleccion):
            j=0
            while j<len(proyeccion[0]):
                if(proyeccion[i][j]==""):
                    print("NULL", end=" ")
                else:
                    print(proyeccion[i][j], end=" ")
                j=j+1
            print("")
            i=i+1
else:
    print("Faltan argumentos")

