from tkinter import *
import tkinter.messagebox as box

def login():
    usuario=entry1.get()
    senha = entry2.get()
    if (usuario == 'admin' and  senha == 'admin'):
        box.showinfo('Sucesso','Login efetuado com sucesso! ')
        
    else:
        box.showinfo('Falha ao Logar','Tente Novamente')


janela = Tk()
janela.title('Login Pe de Pizza')
janela.iconbitmap("pedepizza.ico")
frame = Frame(janela)



Label1 = Label(janela,text = 'Usuario: ')
Label1.pack(padx=15,pady= 5)

entry1 = Entry(janela,bd =5)
entry1.pack(padx=15, pady=5)



Label2 = Label(janela,text = 'Senha: ')
Label2.pack(padx = 15,pady=6)

entry2 = Entry(janela, bd=5)
entry2.pack(padx = 15,pady=7)




btn = Button(frame, text = 'Login ',command = login)
btn.pack(side = RIGHT , padx =5)



frame.pack(padx=200,pady = 19)

janela.mainloop()