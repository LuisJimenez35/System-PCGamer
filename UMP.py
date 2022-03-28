
print('Bienvenid@ a\n\
Pc Gamers Build\n')
print('Digite una de las siguientes opciones\n\
1- PC Armada por PC Gamers Build:\n\
2- Armar tu propia Pc:\n\
3- Contacto y ubicacion\n\
4-Salir:\n')
opcion=input()
while True:
    while True:
        if opcion=="1":   
            print("La lista de productos es la siguiente:")
            Gamers = {"Eco PC" : 115000, 
            "Eco PC 2.0":150000,
            "Baby rock PC":200000,
            "Extreme PC":250000,
            "Pro Gamer PC":500000, 
            "Expert Pro":650000,
            "Streamer Base PC":870000, 
            "Futurist PC": 1030000}
            for i,j in Gamers.items():
                print(i,"₡",j)
            break
        elif opcion=="2":
        
            print("Bienvendo a la seccion de creat tu propia computadora:")
            dirigir = input("Componentes"
            "\n{1} Procesadores"
            "\n{2} Targetas de video"
            "\n{3} Ram"
            "\n{4} Tarjetas madre"
            "\n{5} Fuentes de poder"
            "\n{6} Almacenamiento"
            "\n{7} Cases"
            "\n")
            if dirigir == "1":
                eleccion = input("{A} Para AMD"
                "\n{I} Para Intel"
                "\n")
                if eleccion.upper() == "A":
                    AMD = {"AMD ryzen 3 pro 4133G":110500, 
                    "AMD ryzen 5 pro 4566":140000,
                    "AMD ryzen 5 3600":155000,
                    "AMD ryzen 7 5700G":170000, 
                    "AMD ryzen 9 5950X":200000}
                    for i,j in AMD.items():
                        print(i,"₡",j)
                else:
                    Intel = {"INTEL PENTIUM GOLD G6400" : 52000, 
                    "INTEL CORE I3 10105" : 90000, 
                    "INTEL CORE I5 10400F" : 125000, 
                    "INTEL CORE I7 10700F" : 220000,
                    "INTEL CORE I9 12900K" :529000}
                    for i,j in Intel.items():
                        print(i,"₡",j)
            elif dirigir == "2":
                GPU = {"BIOSTAR RADEON RX 560 4 GB" : 145000, 
                "ASUS GEFORCE GTX 1650 PHOENIX OC 4 GB" : 185000, 
                "ASROCK RADEON RX 6500 XT PHANTOM GAMING" : 180000, 
                "GAINWARD GEFORCE GTX 1660 TI PEGASUS 6 GB" : 280000,
                "ZOTAC GEFORCE RTX 3050 TWIN EDGE 8 GB" : 300000,
                "SAPPHIRE PULSE RADEON RX 6600 8 GB" : 315000,
                "ZOTAC GEFORCE RTX 3070 TWIN EDGE OC 8 GB" : 600000,
                "SAPPHIRE PULSE RADEON RX 6700 XT OC 12 GB" : 610000,
                "ZOTAC GEFORCE RTX 3080 TRINITY 12 GB" : 1099000}
                for i,j in GPU.items():
                        print(i,"₡",j)
            elif dirigir == "3":
                Ram = {"MUSHKIN SILVERLINE 8 GB DDR4 3200MHZ" : 25000,
                "G.SKILL RIPJAWS V 8 GB DDR4 3200 " : 28000,
                "KINGSTON FURY 8 BEAST GB DDR4 3200" : 30000,
                "ADATA XPG SPECTRIX D41 RGB 8 GB DDR4 3200" : 32000,
                "ADATA XPG SPECTRIX D50 8 GB DDR4 3200" : 32000,
                "HYPERX FURY RGB 8 GB DDR4 3200" : 34000,
                "G.SKILL TRIDENT Z RGB 8 GB DDR4 3200":40000,
                "G.SKILL TRIDENT Z RGB 8 GB DDR4 4000" : 47000,}
                for i,j in Ram.items():
                        print(i,"₡",j)
            elif dirigir == "4":
                mother = {"ASROCK A520M HVS"  : 47000,
                "MSI A520M PRO VH": 45000,
                "ASROCK B450M-HDV R4.0" : 49000,
                "ASROCK B450M PRO4- R2.0" : 500000,
                "ASROCK B550M HDV" : 62000,
            "ASUS PRIME B450M A II" : 62000,
                "GIGABYTE H610M H DDR4" : 72000,
                "MSI B550M A PRO" : 78000,
                "GIGABYTE B560M DS3H V2" : 77000,
                "ASUS TUF B450 PLUS II" : 97000,
                "ASROCK B560M STEEL LEGEND" : 105100,
                "ASUS ROG STRIX B450 F GAMING II" : 110000,
                "GIGABYTE B660M DS3H DDR4" : 120000}
                for i,j in mother.items():
                        print(i,"₡",j)
            elif dirigir == "5":
                Power = {"BITFENIX BP 600W 80 PLUS" : 27000,
                "AEROCOOL CYLON 700W ARGB - 80 PLUS BRONZE" : 29000,
                "BE QUIET! SYSTEM POWER U9 600W - 80 PLUS" : 32000,
                "GIGABYTE P550B 80 PLUS BRONZE" :35000,
                "BE QUIET! SYSTEM POWER U9 700W - 80 PLUS" : 39000,
                "EVGA 700W 80 PLUS" : 42000,
                "AEROCOOL DORADO 850W ARGB - 80 PLUS GOLD" : 55000,
                "SEASONIC FOCUS GM-850 - 80 PLUS GOLD" : 85000,
                "GIGABYTE AP850GM - 80 PLUS GOLD-MODULAR" : 92000,
                "EVGA SUPERNOVA 850 GT- 80 PLUS GOLD - MODULAR" : 102000}
                for i,j in Power.items():
                        print(i,"₡",j)
            elif dirigir == "6":
                almacenamiento = {"DISCO DURO WESTERN DIGITAL BLUE 1 TB 7200 RPM" : 29000,
                "DISCO DURO WESTERN DIGITAL BLUE 2 TB 5400 RPM" : 35000,
                "DISCO DURO WESTERN DIGITAL BLUE 4 TB 5400 RPM" : 42000,
                "BIOSTAR S100 120 GB" : 12000,
                "TEAMGROUP M.2 MP33 128 GB" : 14000,
                "ADATA XPG SX6000 128 GB" : 15000,
                "GIGABYTE M.2 128 GB" : 19000,
                "ADATA SU630 240GB" : 19000,
                "KINGSTON A400 240 GB" : 24000,
                "ADATA SU630 480GB" : 34000,
                "ADATA XPG SX8100 256 GB" : 36000,
                "ADATA XPG GAMMIX S11 PRO 256 GB" : 38000,
                "GIGABYTE M.2 512 GB" : 42000,
                "PATRIOT P300 1 TB" : 84000,
                "KINGSTON M.2 NV1 1 TB" : 88000,
                "ADATA XPG SX8100 1 TB": 89000}
                for i,j in almacenamiento.items():
                        print(i,"₡",j)

            elif dirigir == "7":
                cases = {"AEROCOOL SPLIT TG RGB" : 24000,
                "AEROCOOL BOLT G RGB" : 29000,
                "NZXT H210 - BLANCO" : 32000,
                "AEROCOOL SHARD-G V2 - 4 VENTILADORES RGB" : 39000,
                "AZZA INFERNO 310DH - RGB DIGITAL" : 42000,
                "CORSAIR 470T RGB" : 47000,
                "AEROCOOL MIRAGE ARGB" : 55000,
                "LIAN LI LANCOOL 215X- NEGRO" : 62000,
                "NZXT H510 ELITE - NEGRO" : 89125}
                for i,j in cases.items():
                        print(i,"₡",j)
        
            Vuelta = input("Necesitas otro componente?. Digitá S/N")
    
            if Vuelta.upper() == "S":
                continue
            elif Vuelta.upper() == "N":
                quit()
            elif Vuelta.upper() != "S" or Vuelta != "N":
                print("Digite correctamente")
                Vuelta = input("Armas otra?. Digitá S/N")
        elif opcion=="3":
            print('Contancto y Ubicacion:\n\
            www.\n\
            Numero: 506 ********\n')
        elif opcion=="4":
            print('Cerrando sistema')
            quit()
        else :
            print('Por favor digite una opcion correcta')
            opcion=int(input())
        
from tkinter import *
from tkinter import ttk

class interfaz:

    def _init_(self,ventana):
        self.ventana = ventana 
        self.productos = ("Eco Pc-₡115000","Eco Pc 2.0-₡150000","Baby rock Pc-₡200000","Extreme Pc-₡250000","Pro Gamer Pc-₡500000","Expert Pro-₡650000",
        "Streamer Base Pc-₡870000","Futurist Pc-₡1030000","AMD ryzen 3 pro 4133G-₡110500","AMD ryzen 5 pro 4566-₡140000","AMD ryzen 5 3600-₡155000",
        "AMD ryzen 7 5700G-₡170000","AMD ryzen 9 5950x-₡200000","INTEL CORE I3 10105-₡90000","INTEL CORE I5 10400F-₡125000","INTEL CORE I7 10700F-₡220000",
        "INTEL CORE I9 12900K-₡529000","BIOSTAR RADEON RX 560 4 GB-₡145000","ASUS GEFORCE GTX 1650 PHOENIX OC 4 GB-₡185000","ASROCK RADEON RX 6500 XT PHANTOM GAMING-₡180000",
        "GAINWARD GEFORCE GTX 1660 TI PEGASUS 6 GB-₡280000","ZOTAC GEFORCE RTX 3050 TWIN EDGE 8 GB-₡300000","SAPPHIRE PULSE RADEON RX 6600 8 GB-₡315000",
        "ZOTAC GEFORCE RTX 3070 TWIN EDGE OC 8 GB-₡600000","SAPPHIRE PULSE RADEON RX 6700 XT OC 12 GB-₡610000","ZOTAC GEFORCE RTX 3080 TRINITY 12 GB-₡1099000",
        "MUSHKIN SILVERLINE 8 GB DDR4 3200MHZ-₡25000","G.SKILL RIPJAWS V 8 GB DDR4 3200-₡28000","KINGSTON FURY 8 BEAST GB DDR4 3200-₡30000",
        "ADATA XPG SPECTRIX D41 RGB 8 GB DDR4 3200-₡32000","ADATA XPG SPECTRIX D50 8 GB DDR4 3200-₡32000","HYPERX FURY RGB 8 GB DDR4 3200-₡34000",
        "G.SKILL TRIDENT Z RGB 8 GB DDR4 3200-₡40000","G.SKILL TRIDENT Z RGB 8 GB DDR4 4000-₡47000","ASROCK A520M HVS-₡47000","MSI A520M PRO VH-₡45000",
        "ASROCK B450M HDV R4.0-₡49000","ASROCK B450M PRO4 R2.O-₡50000","ASROCK B550M HDV-₡62000","ASUS PRIME B450M A II-₡62000","GIGABYTE H610M H DDR4-₡72000",
        "MSI B550M A PRO-₡78000","GIGABYTE B560M DS3H V2-₡77000","ASUS TUF B450 PLUS II-₡97000","ASROCK B560M STEEL LEGEND-₡105100",
        "ASUS ROG STRIX B450 F GAMING II-₡110000","GIGABYTE B660M DS3H DDR4-₡120000","BITFENIX BP 600W 80 PLUS-₡27000","AEROCOOL CYLON 700W ARGB 80 PLUS BRONZE-₡29000",
        "BE QUIET! SYSTEM POWER U9 600W 80 PLUS-₡32000","GIGABYTE P550B 80 PLUS BRONZE-₡35000","BE QUIET! SYSTEM POWER U9 700W 80 PLUS-₡39000",
        "EVGA 700W 80 PLUS-₡42000","AEROCOOL DORADO 850W ARGB 80 PLUS GOLD-₡55000","SEASONIC FOCUS GM-850 80 PLUS GOLD-₡85000","GIGABYTE AP850GM 80 PLUS GOLD-MODULAR-₡92000",
        "EVGA SUPERNOVA 850 GT 80 PLUS GOLD MODULAR-₡102000","DISCO DURO WESTERN DIGITAL BLUE 1 TB 7200 RPM-₡29000","DISCO DURO WESTERN DIGITAL BLUE 2 TB 5400 RPM-₡35000",
        "DISCO DURO WESTERN DIGITAL BLUE 4 TB 5400 RPM-₡42000","BIOSTAR S100 120 GB-₡12000","TEAMGROUP M.2 MP33 128 GB-₡14000","ADATA XPG SX6000 128 GB-₡15000",
        "GIGABYTE M.2 128 GB-₡19000","ADATA SU630 240GB-₡19000","KINGSTON A400 240 GB-₡24000","ADATA SU630 480GB-₡34000","ADATA XPG SX8100 256 GB-₡36000",
        "ADATA XPG GAMMIX S11 PRO 256 GB-₡38000","GIGABYTE M.2 512 GB-₡42000","PATRIOT P300 1 TB-₡84000","KINGSTON M.2 NV1 1 TB-₡88000","ADATA XPG SX8100 1 TB-₡89000",
        "AEROCOOL SPLIT TG RGB-₡24000","AEROCOOL BOLT G RGB-₡29000","NZXT H210 - BLANCO-₡32000","AEROCOOL SHARD G V2 4 VENTILADORES RGB-₡39000",
        "AZZA INFERNO 310DH RGB DIGITAL-₡42000","CORSAIR 470T RGB-₡47000","AEROCOOL MIRAGE ARGB-₡55000","LIAN LI LANCOOL 215X NEGRO-₡62000",
        "NZXT H510 ELITE NEGRO-₡89125")
        self.cantidad = IntVar()
        self.cajatotal = IntVar()
        self.total = 0
        self.dibujarComponentes()

    def dibujarComponentes(self):
        self .ventana.title("Carrito de compra")
        self.ventana.geometry("650x450")
        Label(self.ventana,text="Seleccione el producto: ").place(x=10,y=10)
        Label(self.ventana,Text="Seleccione la cantidad: ").place(x=10,y=60)
        Label(self.ventana,Text="El total es: ").place(x=450,y=400)
        self.combo = ttk.combobox(self.ventana,state="readonly")
        self.combo.place(x=10,y=35)
        self.combo["values"]=self.productos
        self.combo.current(0)
        Entry(self.ventana,textvariable=self.cantidad).place(x=10,y=85)
        Entry(self.ventana,textvariable=self.cajatotal).place(x=520,y=400)
        Button(self.ventana,text="Agregar",command=self.agregarProducto).place(x=10,y=110)

        self.tabla = ttk.treeview(self.ventana,columns=("Cantidad","Subtotal"))
        self.tabla.heading("#0","Producto")
        self.tabla.heading("Cantidad",text="Cantidad")
        self.tabla.heading("Subtotal",text="Subtotal")
        self.tabla.place(x=10,y=150)

    def agregarProducto(self):
        texto = self.combo.get()
        datos = texto.split("-₡")
        productos = datos[0]
        precio = datos[1]
        cantidad = self.cantidad.get()
        subtotal = int(precio)*int(cantidad)
        self.tabla.insert("",END,text=producto,values=(cantidad,"₡"+str (subtotal)))
        self.total = self.total + subtotal
        self.cajatotal.set("₡"+str (self.total))

        



obj = interfaz(Tk())
obj.ventana.mainloop()













