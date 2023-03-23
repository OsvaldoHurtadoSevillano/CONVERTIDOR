from tkinter import*
from PIL import ImageTk,Image


root=Tk()
root.title("CONVERTIDOR")
root.geometry("500x500")
ventanaPrincipal=Frame(root,width=1000,height=1000)
ventanaPrincipal.grid()


def Convertidor():

        if (Moneda1.get()=="USD"):
            if(Moneda2.get()=="MXN"):
                R1=Numero1.get()*18.55
                
                pass
        if (Moneda1.get()=="USD"):
            if(Moneda2.get()=="EURO"):
                R1=Numero1.get()*0.92
                
                pass
        pass
        if (Moneda1.get()=="MXN"):
            if(Moneda2.get()=="USD"):
                R1=Numero1.get()*0.054
                
                pass
        pass

        if (Moneda1.get()=="MXN"):
            if(Moneda2.get()=="EURO"):
                R1=Numero1.get()*0.049
                
                pass
        pass

        if (Moneda1.get()=="EURO"):
            if(Moneda2.get()=="USD"):
                R1=Numero1.get()*1.09
                
                pass
        pass

        if (Moneda1.get()=="EURO"):
            if(Moneda2.get()=="MXN"):
                R1=Numero1.get()*20.23
                
                pass
        pass
        return SPR1.set(R1)
        pass

Titulo=Label(ventanaPrincipal,text="CONVERTIDOR",font=("Times",15, "bold"),foreground="black", width=30,height=2,justify=CENTER,).place(x=70,y=1)

NumeroA=Label(ventanaPrincipal,text="CANTIDAD A:",font=("Roboto",12),foreground="black", width=15,height=2,justify=CENTER ).place(x=1,y=110)
Numero1=IntVar()
textNumeroA=Entry(ventanaPrincipal,font=("Roboto",12),textvariable=Numero1).place(x=180,y=110)

Moneda1=StringVar()
Moneda1.set("MONEDA")
drop=OptionMenu(root,Moneda1,"USD","MXN","EURO").place(x=80,y=200)


Moneda2=StringVar()
Moneda2.set("MONEDA")
drop=OptionMenu(root,Moneda2,"USD","MXN","EURO").place(x=280,y=200)

Resltado=Label(ventanaPrincipal,text="RESULTADO: ",font=("Roboto",14),foreground="black",width=12,height=2, justify=CENTER,).place(x=1,y=370)

SPR1=StringVar()


Resultadotext=Label(ventanaPrincipal,textvariable=SPR1,font=("Roboto",14),foreground="black", width=19,height=4, justify=CENTER,).place(x=150,y=350)


ButtonRegistrar=Button(ventanaPrincipal,font=("Roboto",14),text="CONVERTIR",command=Convertidor).place(x=160,y=300)

root.mainloop()