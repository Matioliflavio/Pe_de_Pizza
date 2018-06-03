from tkinter import *
import tkinter.messagebox as box
import time

class Entrar(Frame):
    
    #Cores
    _cinza = "#d9d9d9"
    _preto = "#000000"
    _branco = "#FFFFFF"

    def __init__(self,master = None):
        super().__init__()
        self.master.title("Login Pe de Pizza")
        self.pack(padx=200,pady = 19)

        self.frame1=Frame()
        self.frame1.pack(fill = X)
        self.Label1 = Label(self.frame1,text="Usuario")
        self.Label1.pack(padx=15,pady= 5)

        self.entry1=Entry(self.frame1)
        self.entry1.pack(padx=15, pady=5)
     
        self.frame2=Frame()
        self.frame2.pack(fill = X)
        self.Label2 = Label(self.frame2,text="Senha")
        self.Label2.pack(padx=15,pady= 6)

        self.entry2=Entry(self.frame2, show="*")
        self.entry2.pack(padx=15, pady=6)

        self.frame3 = Frame()
        self.frame3.pack(fill=X)
        self.btn = Button(self.frame3, width =15)
        self.btn["text"] = "Entrar"
        self.btn.bind("<Button-1>", self.login)
        self.btn.pack(side=RIGHT, padx=5, pady = 10)

    def login(self, event):
        usuario=self.entry1.get()
        senha = self.entry2.get()
        if (usuario == 'admin' and  senha == 'admin'):
            box.showinfo('Sucesso','Login efetuado com sucesso! ')
            time.sleep(2)
            app.destroy()
        else:
            box.showinfo('Falha ao Logar','Tente Novamente')
app = Tk()
lg = Entrar(app)
app.mainloop()