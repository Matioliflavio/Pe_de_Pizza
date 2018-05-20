from tkinter import *
import tkinter.ttk as ttk

class FramePrincipal(Frame):

    def __init__(self, master=None):

        #Cores
        cinza = "#d9d9d9"
        preto = "#000000"
        branco = "#FFFFFF"

        #Fontes
        font1 = "-family {Courier New} -size 12 "
        font2 = "-family {Segoe UI} -size 12"
        font3 = "Helvetica 12"

        super().__init__()
        self.master.iconbitmap("pedepizza.ico")
        self.master.geometry("700x600")
        self.master.title("Pé de Pizza")
        self.master.resizable(False, False)
        self.pack()

        #criando noteBook. Aka "container de abas"
        notebook = ttk.Notebook(self.master)

        #cirnado a aba 1 Pedido
        framePedido = Frame(notebook, bg=cinza, height=590, width=690)
        
        #---------------------------
        #------ Aba 2 Cliente ------
        #---------------------------

        frameCliente = Frame(bg=cinza, height=590, width=690)

            #Nome
        frameNome = Frame(frameCliente, bg=cinza)
        frameNome.pack(side=TOP, pady=10)
        self.nomeCliente = Label(frameNome, text="Nome:", bg=cinza, font=font2)
        self.nomeCliente.pack(side=LEFT, ipadx=5, ipady=5)
        self.nomeCliente = Entry(frameNome, width=60, bg=branco, font=font2 )
        self.nomeCliente.pack(side=LEFT)
        self.nomeCliente.focus_set()
            
            #Telefone
        frameTelefone = Frame(frameCliente, bg=cinza, height=50, width=690)
        frameTelefone.pack(side=TOP, pady=10)
        self.telefoneCliente = Label(frameTelefone, text="Telefone:", bg=cinza, font=font2)
        self.telefoneCliente.pack(side=LEFT, ipadx=5, ipady=5)
        self.telefoneCliente = Entry(frameTelefone, width=60, bg=branco, font=font2 )
        self.telefoneCliente.pack(side=LEFT)
        self.telefoneCliente.focus_set()

            #CEP
        frameCEP = Frame(frameCliente, bg=cinza, height=50, width=690)
        frameCEP.pack(side=TOP, pady=10)
        self.CEPCliente = Label(frameCEP, text="CEP:", bg=cinza, font=font2)
        self.CEPCliente.pack(side=LEFT, ipadx=5, ipady=5)
        self.CEPCliente = Entry(frameCEP, width=60, bg=branco, font=font2 )
        self.CEPCliente.pack(side=LEFT )
        self.CEPCliente.focus_set()

            #Rua
        frameRua = Frame(frameCliente, bg=cinza, height=50, width=690)
        frameRua.pack(side=TOP, pady=10)
        self.ruaCliente = Label(frameRua, text="Rua:", bg=cinza, font=font2)
        self.ruaCliente.pack(side=LEFT, ipadx=5, ipady=5)
        self.ruaCliente = Entry(frameRua, width=60, bg=branco, font=font2 )
        self.ruaCliente.pack(side=LEFT )
        self.ruaCliente.focus_set()

            #Numero
        frameNumero = Frame(frameCliente, bg=cinza, height=50, width=690)
        frameNumero.pack(side=TOP, pady=10)
        self.numeroCliente = Label(frameNumero, text="Número:", bg=cinza, font=font2)
        self.numeroCliente.pack(side=LEFT, ipadx=5, ipady=5)
        self.numeroCliente = Entry(frameNumero, width=60, bg=branco, font=font2 )
        self.numeroCliente.pack(side=LEFT )
        self.numeroCliente.focus_set()

            #Complemento
        frameComplemento = Frame(frameCliente, bg=cinza, height=50, width=690)
        frameComplemento.pack(side=TOP, pady=10)
        self.complementoCliente = Label(frameComplemento, text="Complemento:", bg=cinza, font=font2)
        self.complementoCliente.pack(side=LEFT, ipadx=5, ipady=5)
        self.complementoCliente = Entry(frameComplemento, width=60, bg=branco, font=font2 )
        self.complementoCliente.pack(side=LEFT )
        self.complementoCliente.focus_set()

            #Bairro
        frameBairro = Frame(frameCliente, bg=cinza, height=50, width=690)
        frameBairro.pack(side=TOP, pady=10)
        self.bairroCliente = Label(frameBairro, text="Bairro:", bg=cinza, font=font2)
        self.bairroCliente.pack(side=LEFT, ipadx=5, ipady=5)
        self.bairroCliente = Entry(frameBairro, width=60, bg=branco, font=font2 )
        self.bairroCliente.pack(side=LEFT )
        self.bairroCliente.focus_set()
        
            #Botoes
        frameBotoes = Frame(frameCliente, bg=cinza, height=50, width=690)
        frameBotoes.pack(side=BOTTOM, pady=10)
        self.btnAdicionarCliente = Button(frameBotoes, width=10, text="Adicionar")
        self.btnAdicionarCliente.pack(side=RIGHT)

        #Criando aba 3 Pizza
        framePizza = Frame(notebook, bg=cinza, height=590, width=690) 
        
        #Adicionando as abas no notebook
        notebook.add(framePedido, text="Pedido", sticky='nsew')
        notebook.add(frameCliente, text="Clientes")
        notebook.add(framePizza, text="Pizzas")
        notebook.pack()
        '''
        self.lblNomeCliente = Label(self.frameCliente, text="Nome:", bg=cinza, font=font2)
        self.lblNomeCliente.pack(side=LEFT, ipadx=10, ipady=10)

        self.nomeCliente = Entry(self.frameCliente, width=22, bg="#DEDEDE", font="Helvetica 12" )
        self.nomeCliente.pack(side=LEFT)
        self.nomeCliente.focus_set()'''



app = FramePrincipal()
app.mainloop()