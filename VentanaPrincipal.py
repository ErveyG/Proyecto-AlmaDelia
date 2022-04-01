import wx
class VentanaPrincipal(wx.Frame):
    def __init__(self, parent, est_temp):
        super().__init__(parent, wx.ID_ANY, "Alma Deliciosa",
                         style=wx.DEFAULT_FRAME_STYLE | wx.MAXIMIZE | wx.STAY_ON_TOP | wx.NO_BORDER | wx.TAB_TRAVERSAL)
        #AQUI DEBES DE PASAR LA TABLA DE EMPLEADOS
        #self.tablaEmployees = tablaEmployees
        self.consulta = ""
        # Estructura para mostrar páginas
        #DEFINIMOS UN ESTILO DE PAGINAS, ESTILO LIBRETA PARA PODER TENER MAS ORGANIZADO NUESTRO PROYECTO
        notebook = wx.Notebook(self,style=wx.NB_BOTTOM)
        #DEFINIMOS LOS PANELES QUE VAMOS A USAR
        self.panelInicio = wx.Panel(notebook)
        self.panelTabla = wx.Panel(notebook)
        self.panelSeleccion = wx.Panel(notebook)
        self.panelProyeccion = wx.Panel(notebook)
        #AGREGAMOS LOS PANELES A LAS PAGINAS
        notebook.AddPage(self.panelInicio, "Gestor de consultas")
        notebook.AddPage(self.panelTabla, "Tablas completas")
        notebook.AddPage(self.panelSeleccion, u"Selección")
        notebook.AddPage(self.panelProyeccion, u"Proyección")
        # ELEMENTOS PARA POSICIONAMIENTO EN EL RESTO DE LAS HOJAS
        # CAJAS ESTATICAS DONDE SE MOSTRARA EL CONTENIDO DE LOS QUERIES
        self.contenedorTabla = wx.StaticBox(self.panelTabla,wx.ID_ANY,label="Tablas completas",size=(1200, -1))
        self.contenedorSeleccion = wx.StaticBox(self.panelSeleccion,wx.ID_ANY,label=u" Selección",size=(1200, -1))
        self.contenedorProyeccion = wx.StaticBox(self.panelProyeccion,wx.ID_ANY,label=u" Proyección",size=(1200, -1))
        # SIZERS
        self.szTablaPrincipal = wx.BoxSizer(wx.VERTICAL)
        self.szSeleccionPrincipal = wx.BoxSizer(wx.VERTICAL)
        self.szProyeccionPrincipal = wx.BoxSizer(wx.VERTICAL)
        #CONFIGURAMOS EL SIZER PRINCIPAL
        sizerPrincipal = wx.BoxSizer()
        sizerPrincipal.Add(notebook, 1, wx.EXPAND, 5)
        self.SetSizer(sizerPrincipal)
        #INICIALIZAMOS CADA PAGINA DE LA INTERFAZ CON SUS ATRIBUTOS CORRESPONDIENTES
        self.paginaInicio(self.panelInicio)
        self.inicializarPaginas(self.panelTabla, self.contenedorTabla, self.szTablaPrincipal,
                                u"\tMuestra todas las tuplas y columnas de la tabla cargada, cuya información es la siguiente:")
        self.inicializarPaginas(self.panelSeleccion, self.contenedorSeleccion, self.szSeleccionPrincipal,
                                u"\tMuestra todas las tuplas que cumplen la condición de consulta, cuya información es la siguiente:")
        self.inicializarPaginas(self.panelProyeccion, self.contenedorProyeccion, self.szProyeccionPrincipal,
                                u"\tMuestra todas las columnas que se solicitan en la consulta, cuya información es la siguiente:")

    ################################################################################################################################

    #PAGINA DE INICIO
    def paginaInicio(self, panelInicio):
        #PANELES DE LA PESTAÑA DE INICIO
        self.panelInicio = panelInicio
        #LE ASIGNAMOS UN COLOR DE FONDO
        panelInicio.SetBackgroundColour("#5D6D7E")
        #GENERAMOS LOS CONTENEDORES
        contenedorInferior = wx.StaticBox(panelInicio, wx.ID_ANY, label="Consultas disponibles", pos=(50, 10),size=(720, 100))
        contenedorInferior.SetBackgroundColour("#5D6D7E")
        # GENERAMOS LOS SIZER
        szInicioPrincipal = wx.BoxSizer(wx.VERTICAL)
        szBoton = wx.BoxSizer(wx.VERTICAL)
        #INICIAMOS CON LA PARTE GRAFICA
        informacion = wx.StaticText(panelInicio, -1,u"Sistema Manejador de Bases de Datos",
                                    wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE)
        imagen = wx.StaticBitmap(panelInicio, wx.ID_ANY, wx.Bitmap('presentacion1.jpg', wx.BITMAP_TYPE_ANY),size=(520, 520))
        #DATOS PARA EL TEXTAREA
        consultas = u""
        self.listaConsultas = wx.TextCtrl(contenedorInferior, style=wx.TE_MULTILINE, pos=(10, 15), size=(538, 70))
        self.aceptarConsulta = wx.Button(contenedorInferior, label="CALLATE PUTA", size=(120, 25), pos=(560, 35))
        szBoton.Add(self.aceptarConsulta)
        # AGREGAMOS LOS ELEMENTOS A LOS SIZERS
        szInicioPrincipal.Add(informacion, 1, wx.EXPAND | wx.ALL, 20)
        szInicioPrincipal.Add(imagen, 1, wx.EXPAND | wx.ALL)
        szInicioPrincipal.Add(contenedorInferior, 2, wx.ALIGN_CENTRE | wx.ALL, 10)
        # CONFIGURAMOS LOS SIZERS
        panelInicio.SetSizer(szInicioPrincipal)
        self.listaConsultas.Bind(wx.EVT_BUTTON, self.realizarConsulta)#ESTA PARTE NO SE SI ES DE AHUEVO NECESARIA


    def inicializarPaginas(self, panelActual, contenedorActual, sizerActual, informacion):
        #PANELES DE PESTAÑA DE INICIO
        #LES ASIGNAMOS PROPIEDADES A LOS CONTENEDORES
        panel = panelActual
        contenedor = contenedorActual
        sizer = sizerActual
        panel.SetBackgroundColour("#5D6D7E")
        contenedor.SetBackgroundColour("#5D6D7E")
        #ELEMENTOS GRAFICOS
        informacion = wx.StaticText(contenedor, wx.ID_ANY, informacion, pos=(25, 25), size=(1000, 50))
        #AGREGAMOS LOS ELEMENTOS A LOS SIZERS Y LO CONFIGURAMOS
        sizer.Add(contenedor, 1, wx.TOP | wx.BOTTOM | wx.ALIGN_CENTRE, 30)
        panel.SetSizer(sizer)

    def seleccionConsulta(self, event):
        #Consulta es el valor que le debes de pasar
        #CONSULTA ES LA CADENA QUE TE PASO PARA HACER EL QUERY
        self.consulta = self.listaConsultas.GetValue()
        print("Consulta seleccionada: " + self.consulta)
        self.aceptarConsulta.Show(True)
    ####################################################################################################################
    def mostrarSeleccion(self,  est_temp):
        orden = self.consultas
        where = orden.split(" ", 1)
        seleccion = []
        seleccion.append(est_temp[0])
        if len(where) >= 2:
            k = 1
            if where[k].find(">=") != -1:
                kaux = where[k].replace(" ", "")
                var = kaux.split(">=")
                j = 0
                while j < len(est_temp[0]):
                    if est_temp[0][j] == var[0]:
                        i = 0
                        while i < len(est_temp)-1:
                            if est_temp[i][j] >= var[1]:
                                seleccion.append(est_temp[i])
                            i = i + 1
                    j = j + 1
            elif where[k].find('<=') != -1:
                kaux = where[k].replace(" ", "")
                var = kaux.split("<=")
                j = 0
                while j < len(est_temp[0]):
                    if est_temp[0][j] == var[0]:
                        i = 0
                        while i < len(est_temp)-1:
                            if est_temp[i][j] <= var[1]:
                                seleccion.append(est_temp[i])
                            i = i + 1
                    j = j + 1
            elif where[k].find('<>') != -1:
                kaux = where[k].replace(" ", "")
                var = kaux.split("<>")
                j = 0
                while j < len(est_temp[0]):
                    if est_temp[0][j] == var[0]:
                        i = 0
                        while i < len(est_temp)-1:
                            if est_temp[i][j] != var[1]:
                                seleccion.append(est_temp[i])
                            i = i + 1
                    j = j + 1
            elif where[k].find('!=') != -1:
                kaux = where[k].replace(" ", "")
                var = kaux.split("!=")
                j = 0
                while j < len(est_temp[0]):
                    if est_temp[0][j] == var[0]:
                        i = 0
                        while i < len(est_temp)-1:
                            if est_temp[i][j] != var[1]:
                                seleccion.append(est_temp[i])
                            i = i + 1
                    j = j + 1
            elif where[k].find('=') != -1:
                kaux = where[k].replace(" ", "")
                var = kaux.split("=")
                j = 0
                while j < len(est_temp[0]):
                    if est_temp[0][j] == var[0]:
                        i = 0
                        while i < len(est_temp)-1:
                            if est_temp[i][j] == var[1]:
                                seleccion.append(est_temp[i])
                            i = i + 1
                    j = j + 1
            elif where[k].find('<') != -1:
                kaux = where[k].replace(" ", "")
                var = kaux.split("<")
                j = 0
                while j < len(est_temp[0]):
                    if est_temp[0][j] == var[0]:
                        i = 0
                        while i < len(est_temp)-1:
                            if est_temp[i][j] < var[1]:
                                seleccion.append(est_temp[i])
                            i = i + 1
                    j = j + 1
            elif where[k].find('>') != -1:
                kaux = where[k].replace(" ", "")
                var = kaux.split(">")
                j = 0
                while j < len(est_temp[0]):
                    if est_temp[0][j] == var[0]:
                        i = 0
                        while i < len(est_temp)-1:
                            if est_temp[i][j] > var[1]:
                                seleccion.append(est_temp[i])
                            i = i + 1
                    j = j + 1
            elif where[k].find('BETWEEN') != -1:
                kaux = where[k].replace(" ", "")
                var = kaux.split("BETWEEN")
                num = var[1].split("AND")
                j = 0
                while j < len(est_temp[0]):
                    if est_temp[0][j] == var[0]:
                        i = 0
                        while i < len(est_temp)-1:
                            if est_temp[i][j] >= num[0] and est_temp[i][j] <= num[1]:
                                seleccion.append(est_temp[i])
                            i = i + 1
                    j = j + 1
            elif where[k].find('IS NULL') != -1:
                kaux = where[k].replace(" ", "")
                var = kaux.split("ISNULL")
                j = 0
                while j < len(est_temp[0]):
                    if est_temp[0][j] == var[0]:
                        i = 0
                        while i < len(est_temp)-1:
                            if est_temp[i][j] == "":
                                seleccion.append(est_temp[i])
                            i = i + 1
                    j = j + 1
            elif where[k].find('NOT IN') != -1:
                kaux = where[k].replace(" ", "")
                var = kaux.split("NOTIN")
                var[1] = var[1].replace(",", " ")
                var[1] = var[1].replace("(", "")
                var[1] = var[1].replace(")", "")
                num = var[1].split(" ")
                print(num)
                j = 0
                while j < len(est_temp[0]):
                    if est_temp[0][j] == var[0]:
                        i = 0
                        while i < len(est_temp)-1:
                            h = 0
                            band = 0
                            while h < len(num):
                                if est_temp[i][j] == num[h]:
                                    band = 1
                                h = h + 1
                            if band == 0:
                                seleccion.append(est_temp[i])
                            i = i + 1
                    j = j + 1
            elif where[k].find('IN') != -1:
                kaux = where[k].replace(" ", "")
                var = kaux.split("IN")
                var[1] = var[1].replace(",", " ")
                var[1] = var[1].replace("(", "")
                var[1] = var[1].replace(")", "")
                num = var[1].split(" ")
                j = 0
                while j < len(est_temp[0]):
                    if est_temp[0][j] == var[0]:
                        i = 0
                        while i < len(est_temp)-1:
                            h = 0
                            while h < len(num):
                                if est_temp[i][j] == num[h]:
                                    seleccion.append(est_temp[i])
                                h = h + 1
                            i = i + 1
                    j = j + 1
            k = k + 1
            i = 0
            while i < len(seleccion):
                j = 0
                while j < len(seleccion[0]):
                    if (seleccion[i][j] == ""):
                        print("NULL", end=" ")
                    else:
                        print(seleccion[i][j], end=" ")
                        j = j + 1
                    print("")
                    i = i + 1
    def mostrarProyeccion(self,est_temp):
        orden=self.consultas
        orden_sin_comas = orden.replace(",", "")
        select = orden_sin_comas.split(" ")
        i = 0
        proyeccion = []
        if len(select) >= 2:
            if select[1] == "*":
                while i < len(est_temp):
                    j = 0
                    while j < len(est_temp[i]):
                        if (est_temp[i][j] == ""):
                            print("NULL", end=" ")
                        else:
                            print(est_temp[i][j], end=" ")
                        j = j + 1
                    print("")
                    i = i + 1
            else:
                k = 1
                while k < len(est_temp):
                    i = 1
                    j = 0
                    while j < len(est_temp[0]):
                        if est_temp[0][j] == select[k]:
                            proyeccion.append([])
                            proyeccion[0].append(est_temp[0][j])
                            while i < len(est_temp):
                                proyeccion.append([])
                                proyeccion[i].append(est_temp[i][j])
                                i = i + 1
                        j = j + 1
                    k = k + 1
                i = 0
                while i < len(est_temp):
                    j = 0
                    while j < len(proyeccion[0]):
                        if (proyeccion[i][j] == ""):
                            print("NULL", end=" ")
                        else:
                            print(proyeccion[i][j], end=" ")
                        j = j + 1
                    print("")
                    i = i + 1
        else:
            print("Faltan argumentos")
    def realizarConsulta(self,event):
        event.Skip()
        print("HOLA")
        if self.consultas.find("SELECT"):
            consultas_sin_comas = self.consultas.replace(",", "")
            select = consultas_sin_comas.split(" ")
            self.mostrarProyeccion()
        elif self.consultas.find("WHERE"):
            where = self.consultas.split(" ", 1)
            self.mostrarSeleccion()