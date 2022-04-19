from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD

from setuptools import Command


# Configuración de la raíz
root = Tk()
root.geometry('600x500')
root.title("PCgamersbuild.com") 
frame = Frame(root)
frame.pack()
frame.config(bg="plum4") 
frame.config(width=600,height=600)   
#Inventario
menubar = Menu(root)
root.config(menu=menubar)
Computadoras = {"Eco PC":115000, 
"Eco PC 2.0":150000,
"Baby rock PC":200000,
"Extreme PC":250000,
"Pro Gamer PC":500000, 
"Expert Pro":650000,
"Streamer Base PC":870000, 
"Futurist PC":1030000,}
procesadoresAMDryzen = {"AMD ryzen 3 pro 4133G" : 110500, 
"AMD ryzen 5 pro 4566" : 140000,
"AMD ryzen 5 3600" : 155000,
"AMD ryzen 7 5700G" : 170000, 
"AMD ryzen 9 5950X" : 200000}
procesadoresIntel = {"INTEL PENTIUM GOLD G6400": 52000, 
"INTEL CORE I3 10105" : 90000, 
"INTEL CORE I5 10400F" : 125000, 
"INTEL CORE I7 10700F" : 220000,
"INTEL CORE I9 12900K":529000}
GPUs = {"BIOSTAR RADEON RX 560 4 GB" : 145000, 
"ASUS GEFORCE GTX 1650 PHOENIX OC 4 GB" : 185000, 
"ASROCK RADEON RX 6500 XT PHANTOM GAMING": 180000, 
"GAINWARD GEFORCE GTX 1660 TI PEGASUS 6 GB": 280000,
"ZOTAC GEFORCE RTX 3050 TWIN EDGE 8 GB" : 300000,
"SAPPHIRE PULSE RADEON RX 6600 8 GB" : 315000,
"ZOTAC GEFORCE RTX 3070 TWIN EDGE OC 8 GB" : 600000,
"SAPPHIRE PULSE RADEON RX 6700 XT OC 12 GB": 610000,
"ZOTAC GEFORCE RTX 3080 TRINITY 12 GB" : 1099000}
tarjetasRam = {"MUSHKIN SILVERLINE 8 GB DDR4 3200MHZ" : 25000,
"G.SKILL RIPJAWS V 8 GB DDR4 3200" : 28000,
"KINGSTON FURY 8 BEAST GB DDR4 3200" : 30000,
"ADATA XPG SPECTRIX D41 RGB 8 GB DDR4 3200" : 32000,
"ADATA XPG SPECTRIX D50 8 GB DDR4 3200" : 32000,
"HYPERX FURY RGB 8 GB DDR4 3200": 34000,
"G.SKILL TRIDENT Z RGB 8 GB DDR4 3200" :40000,
"G.SKILL TRIDENT Z RGB 8 GB DDR4 4000" : 47000}
tarjetamother = {"ASROCK A520M HVS"  : 47000,
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
fuentesDePoder = {"BITFENIX BP 600W 80 PLUS" : 27000,
"AEROCOOL CYLON 700W ARGB - 80 PLUS BRONZE" : 29000,
"BE QUIET! SYSTEM POWER U9 600W - 80 PLUS" : 32000,
"GIGABYTE P550B 80 PLUS BRONZE" :35000,
"BE QUIET! SYSTEM POWER U9 700W - 80 PLUS" : 39000,
"EVGA 700W 80 PLUS" : 42000,
"AEROCOOL DORADO 850W ARGB - 80 PLUS GOLD" : 55000,
"SEASONIC FOCUS GM-850 - 80 PLUS GOLD" : 85000,
"GIGABYTE AP850GM - 80 PLUS GOLD-MODULAR" : 92000,
"EVGA SUPERNOVA 850 GT- 80 PLUS GOLD - MODULAR" : 102000}
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
"ADATA XPG SX8100 1 TB" : 89000}
cases = {"AEROCOOL SPLIT TG RGB" : 24000,
"AEROCOOL BOLT G RGB" : 29000,
"NZXT H210 - BLANCO" : 32000,
"AEROCOOL SHARD-G V2 - 4 VENTILADORES RGB" : 39000,
"AZZA INFERNO 310DH - RGB DIGITAL" : 42000,
"CORSAIR 470T RGB" : 47000,
"AEROCOOL MIRAGE ARGB" : 55000,
"LIAN LI LANCOOL 215X- NEGRO" : 62000,
"NZXT H510 ELITE - NEGRO" : 89125}


controlVars ={"Eco PC":IntVar(), 
"Eco PC 2.0":IntVar(),
"Baby rock PC":IntVar(),
"Extreme PC":IntVar(),
"Pro Gamer PC":IntVar(), 
"Expert Pro":IntVar(),
"Streamer Base PC":IntVar(), 
"Futurist PC":IntVar(),}
controlVars1 = {"AMD ryzen 3 pro 4133G" : IntVar(), 
"AMD ryzen 5 pro 4566" : IntVar(),
"AMD ryzen 5 3600" : IntVar(),
"AMD ryzen 7 5700G" : IntVar(), 
"AMD ryzen 9 5950X" : IntVar()}
controlVars2 = {"INTEL PENTIUM GOLD G6400": IntVar(), 
"INTEL CORE I3 10105" : IntVar(), 
"INTEL CORE I5 10400F" : IntVar(), 
"INTEL CORE I7 10700F" : IntVar(),
"INTEL CORE I9 12900K":IntVar()}
controlVars3 = {"BIOSTAR RADEON RX 560 4 GB" : IntVar(), 
"ASUS GEFORCE GTX 1650 PHOENIX OC 4 GB" : IntVar(), 
"ASROCK RADEON RX 6500 XT PHANTOM GAMING": IntVar(), 
"GAINWARD GEFORCE GTX 1660 TI PEGASUS 6 GB": IntVar(),
"ZOTAC GEFORCE RTX 3050 TWIN EDGE 8 GB" : IntVar(),
"SAPPHIRE PULSE RADEON RX 6600 8 GB" : IntVar(),
"ZOTAC GEFORCE RTX 3070 TWIN EDGE OC 8 GB" : IntVar(),
"SAPPHIRE PULSE RADEON RX 6700 XT OC 12 GB": IntVar(),
"ZOTAC GEFORCE RTX 3080 TRINITY 12 GB" : IntVar()}
controlVars4 = {"MUSHKIN SILVERLINE 8 GB DDR4 3200MHZ" : IntVar(),
"G.SKILL RIPJAWS V 8 GB DDR4 3200" : IntVar(),
"KINGSTON FURY 8 BEAST GB DDR4 3200" : IntVar(),
"ADATA XPG SPECTRIX D41 RGB 8 GB DDR4 3200" : IntVar(),
"ADATA XPG SPECTRIX D50 8 GB DDR4 3200" : IntVar(),
"HYPERX FURY RGB 8 GB DDR4 3200": IntVar(),
"G.SKILL TRIDENT Z RGB 8 GB DDR4 3200" :IntVar(),
"G.SKILL TRIDENT Z RGB 8 GB DDR4 4000" : IntVar()}
controlVars5 = {"ASROCK A520M HVS"  : IntVar(),
"MSI A520M PRO VH": IntVar(),
"ASROCK B450M-HDV R4.0" : IntVar(),
"ASROCK B450M PRO4- R2.0" : IntVar(),
"ASROCK B550M HDV" : IntVar(),
"ASUS PRIME B450M A II" : IntVar(),
"GIGABYTE H610M H DDR4" :IntVar(),
"MSI B550M A PRO" : IntVar(),
"GIGABYTE B560M DS3H V2" : IntVar(),
"ASUS TUF B450 PLUS II" : IntVar(),
"ASROCK B560M STEEL LEGEND" : IntVar(),
"ASUS ROG STRIX B450 F GAMING II" : IntVar(),
"GIGABYTE B660M DS3H DDR4" : IntVar()}
controlVars6 = {"BITFENIX BP 600W 80 PLUS" : IntVar(),
"AEROCOOL CYLON 700W ARGB - 80 PLUS BRONZE" : IntVar(),
"BE QUIET! SYSTEM POWER U9 600W - 80 PLUS" : IntVar(),
"GIGABYTE P550B 80 PLUS BRONZE" :IntVar(),
"BE QUIET! SYSTEM POWER U9 700W - 80 PLUS" :IntVar(),
"EVGA 700W 80 PLUS" : IntVar(),
"AEROCOOL DORADO 850W ARGB - 80 PLUS GOLD" : IntVar(),
"SEASONIC FOCUS GM-850 - 80 PLUS GOLD" : IntVar(),
"GIGABYTE AP850GM - 80 PLUS GOLD-MODULAR" :IntVar(),
"EVGA SUPERNOVA 850 GT- 80 PLUS GOLD - MODULAR" : IntVar()}
controlVars7 = {"DISCO DURO WESTERN DIGITAL BLUE 1 TB 7200 RPM" : IntVar(),
"DISCO DURO WESTERN DIGITAL BLUE 2 TB 5400 RPM" : IntVar(),
"DISCO DURO WESTERN DIGITAL BLUE 4 TB 5400 RPM" : IntVar(),
"BIOSTAR S100 120 GB" : IntVar(),
"TEAMGROUP M.2 MP33 128 GB" : IntVar(),
"ADATA XPG SX6000 128 GB" : IntVar(),
"GIGABYTE M.2 128 GB" : IntVar(),
"ADATA SU630 240GB" : IntVar(),
"KINGSTON A400 240 GB" : IntVar(),
"ADATA SU630 480GB" : IntVar(),
"ADATA XPG SX8100 256 GB" : IntVar(),
"ADATA XPG GAMMIX S11 PRO 256 GB" : IntVar(),
"GIGABYTE M.2 512 GB" : IntVar(),
"PATRIOT P300 1 TB" : IntVar(),
"KINGSTON M.2 NV1 1 TB" : IntVar(),
"ADATA XPG SX8100 1 TB" : IntVar()}
controlVars8 = {"AEROCOOL SPLIT TG RGB" : IntVar(),
"AEROCOOL BOLT G RGB" : IntVar(),
"NZXT H210 - BLANCO" : IntVar(),
"AEROCOOL SHARD-G V2 - 4 VENTILADORES RGB" : IntVar(),
"AZZA INFERNO 310DH - RGB DIGITAL" : IntVar(),
"CORSAIR 470T RGB" : IntVar(),
"AEROCOOL MIRAGE ARGB" : IntVar(),
"LIAN LI LANCOOL 215X- NEGRO" : IntVar(),
"NZXT H510 ELITE - NEGRO" : IntVar()}

Productos = []

Recorredor = ""
Recorredor1 = ""
Recorredor2 = ""
Recorredor3 = ""
Recorredor4 = ""
Recorredor5 = ""
Recorredor6 = ""
Recorredor7 = ""
Recorredor8 = ""
#Ventana de Computadoras Armadas
def APB():
    newWindow1 = Toplevel(root) 
    newWindow1.title("Computadoras Armadas") 
    newWindow1.geometry("500x500")
    Label(newWindow1,text ="Computadoras Armadas:").pack() 
    Label(newWindow1, text="").pack()
    combo = ttk.Combobox(newWindow1,state="readonly",values=Computadoras)
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

def componentes(): 
    global newWindow4
    newWindow4 = Toplevel(root) 
    newWindow4.title("Componentes") 
    newWindow4.geometry("1624x980") 
    frame1 = Frame(newWindow4)
    frame1.grid(row=0,column=0)
    frame2 = Frame(newWindow4)
    frame2.grid(row=0,column=1)
    frame3 = Frame(newWindow4)
    frame3.grid(row=0,column=2)
    frame4 = Frame(newWindow4)
    frame4.grid(row=0,column=3)
    frame5 = Frame(newWindow4)
    frame5.grid(row=1,column=0)
    frame6 = Frame(newWindow4)
    frame6.grid(row=1,column=1)
    frame7 = Frame(newWindow4)
    frame7.grid(row=1,column=2)
    global frame8
    frame8 = Frame(newWindow4)
    frame8.grid(row=1,column=3)
    

    Label(frame1,text="Procesador").pack()
    
    for procesador in procesadoresAMDryzen:
        ck=ttk.Checkbutton(frame1,text=procesador,variable=controlVars1[(procesador) + str(Recorredor1)],onvalue=1,offvalue=0).pack()
    for procesadorI in procesadoresIntel:
        ttk.Checkbutton(frame1,text=procesadorI,variable=controlVars2[(procesadorI) + str(Recorredor2)],onvalue=1,offvalue=0).pack()

    Label(frame2,text="Targetas madre").pack()
    for tarjetas in tarjetamother:
        ttk.Checkbutton(frame2,text=tarjetas,variable=controlVars5[(tarjetas) + str(Recorredor5)],onvalue=1,offvalue=0).pack()

    Label(frame3,text="Tarjetas RAM").pack()
    for tagetasR in tarjetasRam:
        ttk.Checkbutton(frame3,text=tagetasR,variable=controlVars4[(tagetasR) + str(Recorredor4)],onvalue=1,offvalue=0).pack()


    Label(frame4,text="Tarjetas de video").pack()
    for grafica in GPUs:
        ttk.Checkbutton(frame4,text=grafica,variable=controlVars3[(grafica) + str(Recorredor3)],onvalue=1,offvalue=0).pack()
    
    Label(frame5,text="Almacenameinto").pack()
    for almacen in almacenamiento:
        ttk.Checkbutton(frame5,text=almacen,variable=controlVars7[(almacen) + str(Recorredor7)],onvalue=1,offvalue=0).pack()
    
    Label(frame6,text="Fuentes de Poder").pack()
    for fuentes in fuentesDePoder:
        ttk.Checkbutton(frame6,text=fuentes,variable=controlVars6[(fuentes) + str(Recorredor6)],onvalue=1,offvalue=0).pack()

    Label(frame7,text="Cases/Gabinetes").pack()
    for caja in cases:
        ttk.Checkbutton(frame7,text=caja,variable=controlVars8[(caja) + str(Recorredor8)],onvalue=1,offvalue=0).pack()
    Button(frame8,text="Click para agregar calcular el costo de su producto",command=calculo).pack()
#Boton de Calculo

def calculo():
    global newWindow6
    newWindow6 = Toplevel(root)
    newWindow6.title("Carrito de compras")
    newWindow6.geometry("500x500")
    global calculo
    total = 0
    for i in controlVars:
        if controlVars[i].get() == 1:
            valor = Computadoras[i]
            Label(newWindow6,text=( str(i) + "=" + str(valor))).pack()
            total += valor

    for j in controlVars1:
        if controlVars1[j].get() == 1:
            valor1 = procesadoresAMDryzen[j]
            Label(newWindow6,text=( str(j) + "=" + str(valor1))).pack()
            total += valor1
    
    for k in controlVars2:
        if controlVars2[k].get() == 1:
            valor2 = procesadoresIntel[k]
            Label(newWindow6,text=( str(k) + "=" + str(valor2))).pack()
            total += valor2
    
    for l in controlVars3:
        if controlVars3[l].get() == 1:
            valor3 = GPUs[l]
            Label(newWindow6,text=( str(l) + "=" + str(valor3))).pack()
            total += valor3
    
    for z in controlVars4:
        if controlVars4[z].get() == 1:
            valor4 = tarjetasRam[z]
            Label(newWindow6,text=( str(z) + "=" + str(valor4))).pack()
            total += valor4
    
    for x in controlVars5:
        if controlVars5[x].get() == 1:
            valor5 = tarjetamother[x]
            Label(newWindow6,text=( str(x) + "=" + str(valor5))).pack()
            total += valor5
        
    
    for c in controlVars6:
        if controlVars6[c].get() == 1:
            valor6 = fuentesDePoder[c]
            Label(newWindow6,text=( str(c) + "=" + str(valor6))).pack()
            total += valor6
    
    for v in controlVars7:
        if controlVars7[v].get() == 1:
            valor7 = almacenamiento[v]
            Label(newWindow6,text=( str(v) + "=" + str(valor7))).pack()
            total += valor7
        
    
    for b in controlVars8:
        if controlVars8[b].get() == 1:
            valor8 = cases[b]
            Label(newWindow6,text=( str(b) + "=" + str(valor8))).pack()
            total += valor8
    Label(newWindow6,text=("Total = " + str(total))).place(x=100,y=200)
def computadorasarmadas():
    newWindow10 = Toplevel(root)
    newWindow10.title('Comptadoras Prearmadas')
    newWindow10.geometry("1000x1000")
    #frame10= Frame(newWindow10)
    #frame10.grid(row=1,column=2)
    for computador in Computadoras:
    
        ttk.Checkbutton(newWindow10,text=computador,variable=controlVars[(computador) + str(Recorredor)],onvalue=1,offvalue=0).pack()
    Button(newWindow10,text="Click para agregar calcular el costo de su producto",command=calculo).pack()

#Ventana de carrito de compras2 
def carritocompras2(): 
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
    newWindow8 = Toplevel(root) 
    newWindow8.title("Quienes Somos") 
    newWindow8.geometry("500x500") 
    Label(newWindow8,text ="Nuestro lema").pack() 
    Label(newWindow8, text="").pack()

#Menus principal
filemenu = Menu(menubar,tearoff=0)
filemenu.add_command(label="Computadoras Armadas",command=computadorasarmadas)
filemenu.add_command(label="Contacto y Ubicacion",command=ubicacion)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)

#Menus de Inicio
menubar.add_cascade(label="Menu",menu=filemenu)
menubar.add_cascade(label="Componentes",command=componentes)
menubar.add_cascade(label="Quienes Somos", command=lema)
root.mainloop()
