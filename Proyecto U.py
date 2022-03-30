from tkinter import *
from tkinter import ttk


# Configuración de la raíz
root = Tk()
root.geometry('600x500')
root.title("PCgamersbuild.com") 

#Inventario
menubar = Menu(root)
root.config(menu=menubar)
Gamers = ["Eco PC ₡115000", 
"Eco PC 2.0 ₡150000",
"Baby rock PC ₡200000",
"Extreme PC ₡250000",
"Pro Gamer PC ₡500000", 
"Expert Pro ₡650000",
"Streamer Base PC ₡870000", 
"Futurist PC ₡1030000"]
AMDryzen = ["AMD ryzen 3 pro 4133G:110500", 
"AMD ryzen 5 pro 4566:140000",
"AMD ryzen 5 3600:155000",
"AMD ryzen 7 5700G:170000", 
"AMD ryzen 9 5950X:200000"]
Intel = ["INTEL PENTIUM GOLD G6400 : 52000", 
"INTEL CORE I3 10105 : 90000", 
"INTEL CORE I5 10400F : 125000", 
"INTEL CORE I7 10700F : 220000",
"INTEL CORE I9 12900K :529000"]
GPUs = ["BIOSTAR RADEON RX 560 4 GB : 145000", 
"ASUS GEFORCE GTX 1650 PHOENIX OC 4 GB : 185000", 
"ASROCK RADEON RX 6500 XT PHANTOM GAMING : 180000", 
"GAINWARD GEFORCE GTX 1660 TI PEGASUS 6 GB : 280000",
"ZOTAC GEFORCE RTX 3050 TWIN EDGE 8 GB : 300000",
"SAPPHIRE PULSE RADEON RX 6600 8 GB : 315000",
"ZOTAC GEFORCE RTX 3070 TWIN EDGE OC 8 GB : 600000",
"SAPPHIRE PULSE RADEON RX 6700 XT OC 12 GB : 610000",
"ZOTAC GEFORCE RTX 3080 TRINITY 12 GB : 1099000"]
Ram = ["MUSHKIN SILVERLINE 8 GB DDR4 3200MHZ : 25000",
"G.SKILL RIPJAWS V 8 GB DDR4 3200 : 28000",
"KINGSTON FURY 8 BEAST GB DDR4 3200 : 30000",
"ADATA XPG SPECTRIX D41 RGB 8 GB DDR4 3200 : 32000",
"ADATA XPG SPECTRIX D50 8 GB DDR4 3200 : 32000",
"HYPERX FURY RGB 8 GB DDR4 3200 : 34000",
"G.SKILL TRIDENT Z RGB 8 GB DDR4 3200 :40000",
"G.SKILL TRIDENT Z RGB 8 GB DDR4 4000 : 47000",]
mother = ["ASROCK A520M HVS  : 47000",
"MSI A520M PRO VH: 45000",
"ASROCK B450M-HDV R4.0 : 49000",
"ASROCK B450M PRO4- R2.0 : 500000",
"ASROCK B550M HDV : 62000",
"ASUS PRIME B450M A II : 62000",
"GIGABYTE H610M H DDR4 : 72000",
"MSI B550M A PRO : 78000",
"GIGABYTE B560M DS3H V2 : 77000",
"ASUS TUF B450 PLUS II : 97000",
"ASROCK B560M STEEL LEGEND : 105100",
"ASUS ROG STRIX B450 F GAMING II : 110000",
"GIGABYTE B660M DS3H DDR4 : 120000"]
Power = ["BITFENIX BP 600W 80 PLUS : 27000",
"AEROCOOL CYLON 700W ARGB - 80 PLUS BRONZE : 29000",
"BE QUIET! SYSTEM POWER U9 600W - 80 PLUS : 32000",
"GIGABYTE P550B 80 PLUS BRONZE :35000",
"BE QUIET! SYSTEM POWER U9 700W - 80 PLUS : 39000",
"EVGA 700W 80 PLUS : 42000",
"AEROCOOL DORADO 850W ARGB - 80 PLUS GOLD : 55000",
"SEASONIC FOCUS GM-850 - 80 PLUS GOLD : 85000",
"GIGABYTE AP850GM - 80 PLUS GOLD-MODULAR : 92000",
"EVGA SUPERNOVA 850 GT- 80 PLUS GOLD - MODULAR : 102000"]
almacenamiento = ["DISCO DURO WESTERN DIGITAL BLUE 1 TB 7200 RPM : 29000",
"DISCO DURO WESTERN DIGITAL BLUE 2 TB 5400 RPM : 35000",
"DISCO DURO WESTERN DIGITAL BLUE 4 TB 5400 RPM : 42000",
"BIOSTAR S100 120 GB : 12000",
"TEAMGROUP M.2 MP33 128 GB : 14000",
"ADATA XPG SX6000 128 GB : 15000",
"GIGABYTE M.2 128 GB : 19000",
"ADATA SU630 240GB : 19000",
"KINGSTON A400 240 GB : 24000",
"ADATA SU630 480GB : 34000",
"ADATA XPG SX8100 256 GB : 36000",
"ADATA XPG GAMMIX S11 PRO 256 GB : 38000",
"GIGABYTE M.2 512 GB : 42000",
"PATRIOT P300 1 TB : 84000",
"KINGSTON M.2 NV1 1 TB : 88000",
"ADATA XPG SX8100 1 TB: 89000"]
cases = ["AEROCOOL SPLIT TG RGB : 24000",
"AEROCOOL BOLT G RGB : 29000",
"NZXT H210 - BLANCO : 32000",
"AEROCOOL SHARD-G V2 - 4 VENTILADORES RGB : 39000",
"AZZA INFERNO 310DH - RGB DIGITAL : 42000",
"CORSAIR 470T RGB : 47000",
"AEROCOOL MIRAGE ARGB : 55000",
"LIAN LI LANCOOL 215X- NEGRO : 62000",
"NZXT H510 ELITE - NEGRO : 89125"]

#Ventana de Computadoras Armadas
def APB():
    newWindow1 = Toplevel(root) 
    newWindow1.title("New Window") 
    newWindow1.geometry("500x500") 
    Label(newWindow1,text ="Computadoras Armadas:").pack() 
    Label(newWindow1, text="").pack()
    combo = ttk.Combobox(newWindow1,state="readonly",values=Gamers)
    combo.pack()

#Ventana de de Contacto
def ubicacion(): 
    newWindow2 = Toplevel(root) 
    newWindow2.title("New Window") 
    newWindow2.geometry("200x200") 
    Label(newWindow2,text ="Contacto y Ubicacion").pack() 
    Label(newWindow2, text="").pack()
    Label(newWindow2, text="www.").pack()
    Label(newWindow2, text="506 ***********").pack()

#Ventana de Componentes
def AMD():
    newWindow3 = Toplevel(root) 
    newWindow3.title("Procesadores") 
    newWindow3.geometry("500x500") 
    Label(newWindow3,text ="Procesadores").pack() 
    Label(newWindow3, text="Procesadores AMD").pack()
    combo = ttk.Combobox(newWindow3,state="readonly",values=AMDryzen)
    combo.pack()
def INTEL():
    newWindow3 = Toplevel(root) 
    newWindow3.title("Procesadores") 
    newWindow3.geometry("500x500") 
    Label(newWindow3,text ="Procesadores").pack() 
    Label(newWindow3, text="Procesadores INTEL").pack()
    combo = ttk.Combobox(newWindow3,state="readonly",values=Intel)
    combo.pack()
def GPU():
    newWindow3 = Toplevel(root) 
    newWindow3.title("GPU") 
    newWindow3.geometry("500x500") 
    Label(newWindow3,text ="Targetas de Video").pack() 
    combo = ttk.Combobox(newWindow3,state="readonly",values=GPUs)
    combo.pack()
def RAM():
    newWindow3 = Toplevel(root) 
    newWindow3.title("Ram") 
    newWindow3.geometry("500x500") 
    Label(newWindow3, text="Targetas RAM").pack()
    combo = ttk.Combobox(newWindow3,state="readonly",values=Ram)
    combo.pack()
def MOTHER():
    newWindow3 = Toplevel(root) 
    newWindow3.title("Procesadores") 
    newWindow3.geometry("500x500") 
    Label(newWindow3, text="Targetas Madre").pack()
    combo = ttk.Combobox(newWindow3,state="readonly",values=mother)
    combo.pack()
def POWER():
    newWindow3 = Toplevel(root) 
    newWindow3.title("Procesadores") 
    newWindow3.geometry("500x500") 
    Label(newWindow3, text="Fuentes de poder").pack()
    combo = ttk.Combobox(newWindow3,state="readonly",values=Power)
    combo.pack()
def Alemacenamiento():
    newWindow3 = Toplevel(root) 
    newWindow3.title("Procesadores") 
    newWindow3.geometry("500x500") 
    Label(newWindow3, text="Almacenamiento").pack()
    combo = ttk.Combobox(newWindow3,state="readonly",values=almacenamiento)
    combo.pack()
def Cases():
    newWindow3 = Toplevel(root) 
    newWindow3.title("Procesadores") 
    newWindow3.geometry("500x500") 
    Label(newWindow3, text="Cases").pack()
    combo = ttk.Combobox(newWindow3,state="readonly",values=cases)
    combo.pack()
def componentes(): 
    newWindow4 = Toplevel(root) 
    newWindow4.title("Componentes") 
    newWindow4.geometry("500x500") 
    Label(newWindow4,text ="Componentes").pack() 
    Label(newWindow4, text="").pack()
    btn = Button(newWindow4,text="Procesadores AMD",command=AMD).pack()
    btn = Button(newWindow4,text="Procesadores INTEL",command=INTEL).pack()
    btn = Button(newWindow4,text="Targetas de video",command=GPU).pack()
    btn = Button(newWindow4,text="Targetas RAM",command=RAM).pack()
    btn = Button(newWindow4,text="Targetas madre",command=MOTHER).pack()
    btn = Button(newWindow4,text="Fuentes de poder",command=POWER).pack()
    btn = Button(newWindow4,text="Almacenamiento",command=Alemacenamiento).pack()
    btn = Button(newWindow4,text="Cases",command=Cases).pack()
#Ventana de Carrito de Compras
def carritocompras(): 
    newWindow5 = Toplevel(root) 
    newWindow5.title("Carrito de compras") 
    newWindow5.geometry("500x500") 
    Label(newWindow5,text ="Productos seleccionados").pack() 
    Label(newWindow5, text="").pack()
#Ventana de carrito de compras2 
def carritocompras2(): 
    newWindow6 = Toplevel(root)
    newWindow6.title("Carrito de compras")
    newWindow6.geometry("500x500")
    Label(newWindow6,text="Seleccione la cantidad").place(x=10,y=20)
    Label(newWindow6,text="El total es").place(x=30,y=90)
    Label(newWindow6,text="").pack()
    btn = Button(newWindow6,text="Pago con tarjeta",command=tarjeta).place(x=200,y=200)
    btn = Button(newWindow6,text="Pago en efectivo",command=efectivo).place(x=200,y=240)

def tarjeta(): 
    newWindow7 = Toplevel(root)
    newWindow7.title("Carrito de compras")
    newWindow7.geometry("500x500")
    Label(newWindow7,text="Seleccione la cantidad").place(x=10,y=20)
    Label(newWindow7,text="El total es",).place(x=30,y=90)

def efectivo(): 
    newWindow9 = Toplevel(root)
    newWindow9.title("Carrito de compras")
    newWindow9.geometry("500x500")
    Label(newWindow9,text="El total es",).place(x=30,y=90)
#Ventana de Quienes somos
def lema(): 
    newWindow6 = Toplevel(root) 
    newWindow6.title("Quienes Somos") 
    newWindow6.geometry("500x500") 
    Label(newWindow6,text ="Nuestro lema").pack() 
    Label(newWindow6, text="").pack()

#Menus principal
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Computadoras Armadas",command=APB)
filemenu.add_command(label="Armar tu propia Computadora",command=componentes)
filemenu.add_command(label="Contacto y Ubicacion",command=ubicacion)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)

#Menus de Inicio
menubar.add_cascade(label="Menu", menu=filemenu)
menubar.add_cascade(label="Quienes Somos", command=lema)
menubar.add_cascade(label="Carrito de Compras", command=carritocompras)

root.mainloop()
