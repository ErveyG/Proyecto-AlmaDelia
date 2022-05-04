import os

try:
    import wx
except ImportError:
    print("Instalando la libreria wx...\n")
    os.system('pip install -U wxPython')
    try:
        import wx
    except ImportError:
        print("Se tiene que instalar la libreria wxpython\n")
        print("Copie este comando en el simbolo del sistema     pip install -U wxPython")
        os._exit(-1)

from VentanaPrincipal import VentanaPrincipal

###########################################################################
## Main Program
###########################################################################
def main():
    # Obtiene la tabla Employees del descriptor
   # descEmployees = Descriptor("Employees.txt")
    est_temp = []
    f = open("DB.txt", "r")
    num_linea = 0
    k = 1
    while (True):
        linea = f.readline()
        # Verifica que estemos leyendo la primer linea del archivo y obtiene una lista que maneja los datos del descriptor
        if num_linea == 0:
            descriptor = linea.split(",")
            tam_lista = len(descriptor)
            i = 1
            est_temp.append([])
            while i < tam_lista:
                est_temp[0].append(descriptor[i])
                i = i + 3
        else:
            est_temp.append([])
            i = 1
            j = 0
            while i < tam_lista:
                atr = linea[int(descriptor[i + 1]):int(descriptor[i + 2])]
                est_temp[k].append(atr.strip())
                i = i + 3
                j = j + 1
            k = k + 1
        num_linea = num_linea + 1
        if not linea:
            break
    est_temp2 = []
    f = open("departments.txt", "r")
    num_linea2 = 0
    k = 1
    while (True):
        linea = f.readline()
        # Verifica que estemos leyendo la primer linea del archivo y obtiene una lista que maneja los datos del descriptor
        if num_linea2 == 0:
            descriptor = linea.split(",")
            tam_lista = len(descriptor)
            i = 1
            est_temp2.append([])
            while i < tam_lista:
                est_temp2[0].append(descriptor[i])
                i = i + 3
        else:
            est_temp2.append([])
            i = 1
            j = 0
            while i < tam_lista:
                atr = linea[int(descriptor[i + 1]):int(descriptor[i + 2])]
                est_temp2[k].append(atr.strip())
                i = i + 3
                j = j + 1
            k = k + 1
        num_linea2 = num_linea2 + 1
        if not linea:
            break
    est_temp.pop()
    f.close()
    #tablaEmployees = descEmployees.leerDescriptor()
    # Genera Aplicación
    app = wx.App()
    # Genera un el Frame principal y le pasa la tabla de empleados
    ex = VentanaPrincipal(None, est_temp, est_temp2,num_linea, num_linea2)#(None, tablaEmployees)
    # Muestra el frame principal
    ex.Show()
    # Pone la aplicacion en loop
    app.MainLoop()
if __name__ == '__main__':
    main()