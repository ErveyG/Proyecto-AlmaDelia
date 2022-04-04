import wx
class VentanaPrincipal(wx.Frame):
    def __init__(self, parent, est_temp1, num_linea1):
        super().__init__(parent, wx.ID_ANY, "DBMS",
                         style=wx.DEFAULT_FRAME_STYLE | wx.MAXIMIZE | wx.STAY_ON_TOP | wx.NO_BORDER | wx.TAB_TRAVERSAL)
        self.consulta = ""
        self.est_temp=est_temp1
        self.num_linea=num_linea1
        # Estructura para mostrar páginas
        #DEFINIMOS UN ESTILO DE PAGINAS, ESTILO LIBRETA PARA PODER TENER MAS ORGANIZADO NUESTRO PROYECTO
        notebook = wx.Notebook(self,style=wx.NB_BOTTOM)
        #DEFINIMOS LOS PANELES QUE VAMOS A USAR
        self.panelInicio = wx.Panel(notebook)
        self.panelTabla = wx.Panel(notebook)
        self.panelSeleccion = wx.Panel(notebook)
        self.panelProyeccion = wx.Panel(notebook)
        #AGREGAMOS LOS PANELES A LAS PAGINAS
        notebook.AddPage(self.panelInicio, "CONSULTAS")
        notebook.AddPage(self.panelTabla, "TABLA COMPLETA")
        notebook.AddPage(self.panelSeleccion, u"SELECCION")
        notebook.AddPage(self.panelProyeccion, u"PROYECCION")
        # ELEMENTOS PARA POSICIONAMIENTO EN EL RESTO DE LAS HOJAS
        # CAJAS ESTATICAS DONDE SE MOSTRARA EL CONTENIDO DE LOS QUERIES
        self.contenedorTabla = wx.StaticBox(self.panelTabla,wx.ID_ANY,size=(1200, -1))
        self.contenedorSeleccion = wx.StaticBox(self.panelSeleccion,wx.ID_ANY,size=(1200, -1))
        self.contenedorProyeccion = wx.StaticBox(self.panelProyeccion,wx.ID_ANY,size=(1200, -1))
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
        self.inicializarPaginas(self.panelTabla, self.contenedorTabla, self.szTablaPrincipal,u"")
        self.inicializarPaginas(self.panelSeleccion, self.contenedorSeleccion, self.szSeleccionPrincipal,u"")
        self.inicializarPaginas(self.panelProyeccion, self.contenedorProyeccion, self.szProyeccionPrincipal,u"")

    ################################################################################################################################

    #PAGINA DE INICIO
    def paginaInicio(self, panelInicio):
        #PANELES DE LA PESTAÑA DE INICIO
        self.panelInicio = panelInicio
        #LE ASIGNAMOS UN COLOR DE FONDO
        panelInicio.SetBackgroundColour("#C84734")#main
        #GENERAMOS LOS CONTENEDORES
        contenedorInferior = wx.StaticBox(panelInicio, wx.ID_ANY, pos=(50, 10),size=(700, 100))
        contenedorInferior.SetBackgroundColour("#C84734")
        # GENERAMOS LOS SIZER
        szInicioPrincipal = wx.BoxSizer(wx.VERTICAL)
        szBoton = wx.BoxSizer(wx.VERTICAL)
        #INICIAMOS CON LA PARTE GRAFICA
        informacion = wx.StaticText(panelInicio, -1,u"",wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE)
        imagen = wx.StaticBitmap(panelInicio, wx.ID_ANY, wx.Bitmap('prueba.jpg', wx.BITMAP_TYPE_ANY),size=(400,400))
        #DATOS PARA EL TEXTAREA
        self.consulta = u""
        self.listaConsultas = wx.TextCtrl(contenedorInferior, style=wx.TE_MULTILINE, pos=(15, 15), size=(538, 70))
        self.aceptarConsulta = wx.Button(contenedorInferior, label="ACEPTAR", size=(120, 25), pos=(560, 35))
        szBoton.Add(self.aceptarConsulta)
        # AGREGAMOS LOS ELEMENTOS A LOS SIZERS
        szInicioPrincipal.Add(informacion, 1, wx.EXPAND | wx.ALL, 20)
        szInicioPrincipal.Add(imagen, 1, wx.EXPAND | wx.ALL)
        szInicioPrincipal.Add(contenedorInferior, 2, wx.ALIGN_CENTRE | wx.ALL, 10)
        # CONFIGURAMOS LOS SIZERS
        panelInicio.SetSizer(szInicioPrincipal)
        self.aceptarConsulta.Bind(wx.EVT_BUTTON, self.realizarConsulta)#ESTA PARTE NO SE SI ES DE AHUEVO NECESARIA


    def inicializarPaginas(self, panelActual, contenedorActual, sizerActual, informacion):
        #PANELES DE PESTAÑA DE INICIO
        #LES ASIGNAMOS PROPIEDADES A LOS CONTENEDORES
        panel = panelActual
        contenedor = contenedorActual
        sizer = sizerActual
        panel.SetBackgroundColour("#C84734")#rojo
        contenedor.SetBackgroundColour("#F1E0DD")#blanco
        #ELEMENTOS GRAFICOS
        informacion = wx.StaticText(contenedor, wx.ID_ANY, informacion, pos=(25, 25), size=(1000, 50))
        #AGREGAMOS LOS ELEMENTOS A LOS SIZERS Y LO CONFIGURAMOS
        sizer.Add(contenedor, 1, wx.TOP | wx.BOTTOM | wx.ALIGN_CENTRE, 30)
        panel.SetSizer(sizer)
    ####################################################################################################################
    def mostrarSeleccion(self, orden):
        where = orden.split(" ", 1)
        seleccion = []
        seleccion.append(self.est_temp[0])
        if len(where) >= 2:
            k = 1
            if where[k].find(">=") != -1:
                kaux = where[k].replace(" ", "")
                var = kaux.split(">=")
                j = 0
                while j < len(self.est_temp[0]):
                    if self.est_temp[0][j] == var[0]:
                        i = 1
                        while i < self.num_linea - 1:
                            if self.est_temp[i][j] >= var[1]:
                                seleccion.append(self.est_temp[i])
                            i = i + 1
                    j = j + 1
            elif where[k].find('<=') != -1:
                kaux = where[k].replace(" ", "")
                var = kaux.split("<=")
                j = 0
                while j < len(self.est_temp[0]):
                    if self.est_temp[0][j] == var[0]:
                        i = 1
                        while i < self.num_linea - 1:
                            if self.est_temp[i][j] <= var[1]:
                                seleccion.append(self.est_temp[i])
                            i = i + 1
                    j = j + 1
            elif where[k].find('<>') != -1:
                kaux = where[k].replace(" ", "")
                var = kaux.split("<>")
                j = 0
                while j < len(self.est_temp[0]):
                    if self.est_temp[0][j] == var[0]:
                        i = 1
                        while i < self.num_linea - 1:
                            if self.est_temp[i][j] != var[1]:
                                seleccion.append(self.est_temp[i])
                            i = i + 1
                    j = j + 1
            elif where[k].find('!=') != -1:
                kaux = where[k].replace(" ", "")
                var = kaux.split("!=")
                j = 0
                while j < len(self.est_temp[0]):
                    if self.est_temp[0][j] == var[0]:
                        i = 1
                        while i < self.num_linea - 1:
                            if self.est_temp[i][j] != var[1]:
                                seleccion.append(self.est_temp[i])
                            i = i + 1
                    j = j + 1
            elif where[k].find('=') != -1:
                kaux = where[k].replace(" ", "")
                var = kaux.split("=")
                j = 0
                while j < len(self.est_temp[0]):
                    if self.est_temp[0][j] == var[0]:
                        i = 1
                        while i < self.num_linea - 1:
                            if self.est_temp[i][j] == var[1]:
                                seleccion.append(self.est_temp[i])
                            i = i + 1
                    j = j + 1
            elif where[k].find('<') != -1:
                kaux = where[k].replace(" ", "")
                var = kaux.split("<")
                j = 0
                while j < len(self.est_temp[0]):
                    if self.est_temp[0][j] == var[0]:
                        i = 1
                        while i < self.num_linea - 1:
                            if self.est_temp[i][j] < var[1]:
                                seleccion.append(self.est_temp[i])
                            i = i + 1
                    j = j + 1
            elif where[k].find('>') != -1:
                kaux = where[k].replace(" ", "")
                var = kaux.split(">")
                j = 0
                while j < len(self.est_temp[0]):
                    if self.est_temp[0][j] == var[0]:
                        i = 1
                        while i < self.num_linea - 1:
                            if self.est_temp[i][j] > var[1]:
                                seleccion.append(self.est_temp[i])
                            i = i + 1
                    j = j + 1
            elif where[k].find('BETWEEN') != -1:
                kaux = where[k].replace(" ", "")
                var = kaux.split("BETWEEN")
                num = var[1].split("AND")
                j = 0
                while j < len(self.est_temp[0]):
                    if self.est_temp[0][j] == var[0]:
                        i = 1
                        while i < self.num_linea - 1:
                            if self.est_temp[i][j] >= num[0] and self.est_temp[i][j] <= num[1]:
                                seleccion.append(self.est_temp[i])
                            i = i + 1
                    j = j + 1
            elif where[k].find('IS NULL') != -1:
                kaux = where[k].replace(" ", "")
                var = kaux.split("ISNULL")
                j = 0
                while j < len(self.est_temp[0]):
                    if self.est_temp[0][j] == var[0]:
                        i = 1
                        while i < self.num_linea - 1:
                            if self.est_temp[i][j] == "":
                                seleccion.append(self.est_temp[i])
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
                while j < len(self.est_temp[0]):
                    if self.est_temp[0][j] == var[0]:
                        i = 1
                        while i < self.num_linea - 1:
                            h = 0
                            band = 0
                            while h < len(num):
                                if self.est_temp[i][j] == num[h]:
                                    band = 1
                                h = h + 1
                            if band == 0:
                                seleccion.append(self.est_temp[i])
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
                while j < len(self.est_temp[0]):
                    if self.est_temp[0][j] == var[0]:
                        i = 1
                        while i < self.num_linea - 1:
                            h = 0
                            while h < len(num):
                                if self.est_temp[i][j] == num[h]:
                                    seleccion.append(self.est_temp[i])
                                h = h + 1
                            i = i + 1
                    j = j + 1
            k = k + 1
            cad_imp = ""
            i=0
            while i < len(seleccion):
                j = 0
                while j < len(seleccion[0]):
                    if (seleccion[i][j] == ""):
                        cad_imp = cad_imp + "NULL "
                    else:
                        cad_imp = cad_imp + seleccion[i][j]
                        cad_imp = cad_imp + " "
                    j = j + 1
                print("")
                cad_imp = cad_imp + "\n"
                i = i + 1
                print(cad_imp)
                self.impresion= wx.TextCtrl(self.contenedorSeleccion, wx.ID_ANY, size=(1200, 640),style=wx.TE_MULTILINE)
                self.impresion.AppendText(cad_imp)
                self.szSeleccionPrincipal.SetContainingWindow(self.panelSeleccion)
                self.panelSeleccion.SetSizer(self.szSeleccionPrincipal)
        else:
            seleccion = self.est_temp

    def mostrarProyeccion(self, orden):
        seleccion=self.est_temp
        orden_sin_comas = orden.replace(",", "")
        select = orden_sin_comas.split(" ")
        i = 0
        proyeccion = []
        if len(select) >= 2:
            if select[1] == "*":
                cad_imp = ""
                while i < len(seleccion):
                    j = 0
                    while j < len(seleccion[i]):
                        if (seleccion[i][j] == ""):
                            cad_imp = cad_imp + "NULL "
                        else:
                            cad_imp = cad_imp + seleccion[i][j]
                            cad_imp = cad_imp + " "
                        j = j + 1
                    cad_imp = cad_imp + "\n"

                    i = i + 1
                print(cad_imp)
                self.impresion = wx.TextCtrl(self.contenedorProyeccion, wx.ID_ANY, size=(1200, 640), style=wx.TE_MULTILINE)  # agregar posicion tamaño
                self.impresion.AppendText(cad_imp)
                self.szProyeccionPrincipal.SetContainingWindow(self.panelProyeccion)
                self.panelProyeccion.SetSizer(self.szSeleccionPrincipal)
            else:
                k = 1
                while k < len(select):
                    i = 1
                    j = 0
                    while j < len(seleccion[0]):
                        if seleccion[0][j] == select[k]:
                            proyeccion.append([])
                            proyeccion[0].append(seleccion[0][j])
                            while i < len(seleccion):
                                proyeccion.append([])
                                proyeccion[i].append(seleccion[i][j])
                                i = i + 1
                        j = j + 1
                    k = k + 1
                cad_imp=""
                i = 0
                while i < len(seleccion):
                    j = 0
                    while j < len(proyeccion[0]):
                        if (proyeccion[i][j] == ""):
                            cad_imp=cad_imp+"NULL "
                        else:
                            cad_imp = cad_imp + proyeccion[i][j]
                            cad_imp=cad_imp+" "
                        j = j + 1
                    cad_imp=cad_imp+"\n"
                    i = i + 1
                print(cad_imp)
                self.impresion = wx.TextCtrl(self.contenedorProyeccion,wx.ID_ANY, size=(1200,640), style=wx.TE_MULTILINE)#agregar posicion tamaño
                self.impresion.AppendText(cad_imp)
                self.szProyeccionPrincipal.Add(self.impresion,1,wx.EXPAND|wx.ALL,10)
                self.SetSizer(self.szProyeccionPrincipal)
        else:
            print("Faltan argumentos")
    def realizarConsulta(self,event):
        event.Skip()
        orden=self.listaConsultas.GetValue()
        if orden.find("SELECT")!=-1:
            self.mostrarProyeccion(orden)
        elif orden.find("WHERE")!=-1:
            self.mostrarSeleccion(orden)