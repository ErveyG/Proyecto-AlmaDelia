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
    #tablaEmployees = descEmployees.leerDescriptor()
    # Genera Aplicación
    app = wx.App()
    # Genera un el Frame principal y le pasa la tabla de empleados
    ex = VentanaPrincipal(None)#(None, tablaEmployees)
    # Muestra el frame principal
    ex.Show()
    # Pone la aplicacion en loop
    app.MainLoop()
if __name__ == '__main__':
    main()