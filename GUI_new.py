from tkinter import *
from tkinter import filedialog
import tkinter.ttk as ttk
import ManipuladorDados as mp



class FramePrincipal(Frame):
    
    #Cores
    _cinza = "#d9d9d9"
    _preto = "#000000"
    _branco = "#FFFFFF"

    #Fontes
    _font1 = "Helvetica 9 "
    _font2 = "Helbetica 10"
    _font3 = "Helvetica 12"
    _font4 = "Helvetica 18"

    #Strings
    _info = '''Pé de Pizza é uma aplicação para gerenciamento de pizzaria.
        Desenvolvido na linguagem Python,
        o programa tem seu código fonte aberto, 
        esta licenciado sobre os termos do MIT 
        e pode ser baixado diretamento no gitHub pelo seguinte link:  '''
    _autores = "Flavio Matioli & Gabriel Nardini"
    _empresa = "PyCaretas LTDA"

    _caminho = ""
    
    def __init__(self, master=None):
        
        #------------------------
        #-------- Janela --------
        #------------------------
        super().__init__()
        self.master.iconbitmap("pedepizza.ico")
        self.centralizar(700,700)
        self.master.title("Pé de Pizza")
        self.master.resizable(False, False)
        self.master["bg"] = self._cinza
        self.pack()

    
        #criando noteBook. Aka "container de abas"
        notebook = ttk.Notebook(self.master)

        #--------------------------
        #------ Aba 1 Pedido ------
        #--------------------------
        framePedido = Frame(notebook, bg=self._cinza)

        self.addTitulo(framePedido, " >> Pedido << ", self._branco, self._font4)
        
        notebook.add(framePedido, text=" Pedido ")

        #---------------------------
        #------ Aba 2 Cliente ------
        #---------------------------
        frameCliente = Frame(notebook, bg=self._cinza)

        

        self.addTitulo(frameCliente, " >> Cliente << ", self._branco, self._font4)
        #--Nome--
        self.addTitulo(frameCliente, "Nome:", self._cinza,  self._font3, LEFT)
        frameNome = Frame(frameCliente, bg=self._cinza)
        frameNome.pack(side=TOP, fill=X)
        self.nomeClienteEntry= StringVar()
        self.nomeCliente = Entry(frameNome, width=80, bg=self._branco, font=self._font2, textvariable=self.nomeClienteEntry )
        self.nomeCliente.pack(side=LEFT, fill=X)
        self.nomeCliente.focus_set()

        #--Telefone--
        self.addTitulo(frameCliente, "Telefone:", self._cinza,  self._font3, LEFT)
        frameTelefone = Frame(frameCliente, bg=self._cinza)
        frameTelefone.pack(side=TOP, fill=X)
        self.telefoneClienteEntry= StringVar()
        self.telefoneCliente = Entry(frameTelefone, width=80, bg=self._branco, font=self._font2, textvariable=self.telefoneClienteEntry)
        self.telefoneCliente.pack(side=LEFT, fill=X)
        
        #--CEP--
        self.addTitulo(frameCliente, "CEP:", self._cinza,  self._font3, LEFT)
        frameCEP = Frame(frameCliente, bg=self._cinza)
        frameCEP.pack(side=TOP, fill=X)
        self.cepClienteEntry= StringVar()
        self.cepCliente = Entry(frameCEP, width=80, bg=self._branco, font=self._font2, textvariable=self.cepClienteEntry)
        self.cepCliente.pack(side=LEFT, fill=X)
        

        frameBotoes = Frame(frameCliente, bg=self._cinza)
        frameBotoes.pack(side=BOTTOM, fill=X)
        self.btnAdicionarCliente = Button(frameBotoes, width=10, text="Adicionar", command=self.adicionarCliente)
        self.btnAdicionarCliente.pack(side=RIGHT, padx=10)
        self.btnLimparCliente = Button(frameBotoes, width=10, text="Limpar", command=self.limparCliente)
        self.btnLimparCliente.pack(side=RIGHT, padx=10)

        notebook.add(frameCliente, text=" Cliente ")

        #--------------------------
        #------ Aba 3 Pizzas ------
        #--------------------------
        framePizzas = Frame(notebook, bg=self._cinza)

        self.addTitulo(framePizzas, " >> Pizzas << ", self._branco, self._font4)

        notebook.add(framePizzas, text=" Pizzas ")

        #---------------------------
        #------ Aba 4 Deletar ------
        #---------------------------
        frameDeletar = Frame(notebook, bg=self._cinza)

        self.addTitulo(frameDeletar, " >> Deletar << ", self._branco, self._font4)

        notebook.add(frameDeletar, text=" Deletar ")

        #-------------------------------
        #------ Aba 5 Faturamento ------
        #-------------------------------
        frameFaturamento = Frame(notebook, bg=self._cinza)

        self.addTitulo(frameFaturamento, " >> Faturamento << ", self._branco, self._font4)

        notebook.add(frameFaturamento, text=" Faturamento ")

        #----------------------------
        #------ Aba 6 Importar ------
        #----------------------------
        frameImportar = Frame(notebook, bg=self._cinza)

        self.addTitulo(frameImportar, " >> Importar << ", self._branco, self._font4)

        notebook.add(frameImportar, text=" Importar ")

        #----------------------------
        #------ Aba 7 Exportar ------
        #----------------------------
        frameExportar = Frame(notebook, bg=self._cinza)

        self.addTitulo(frameExportar, " >> Exportar << ", self._branco, self._font4)

        self.addTitulo(frameExportar, "Caminho:", self._cinza,  self._font3, LEFT)
        frameCaminho = Frame(frameExportar, bg=self._cinza)
        frameCaminho.pack(side=TOP, fill=X)
        self.entradaCaminho = StringVar()
        self.caminhoExportar = Entry(frameCaminho, width=80, bg=self._branco, font=self._font2, textvariable=self.entradaCaminho)
        self.caminhoExportar.pack(side=LEFT, fill=X)
        self.caminhoExportar.focus_set()
        self.btnProcuraCaminho = Button(frameCaminho, width=10, text="Buscar", command=self.botaoProcuraCaminho)
        self.btnProcuraCaminho.pack(side=RIGHT)

        notebook.add(frameExportar, text=" Exportar ")

        #-------------------------
        #------ Aba 8 Dados ------
        #-------------------------
        frameDados = Frame(notebook, bg=self._cinza)

        self.addTitulo(frameDados, " >> Dados << ", self._branco, self._font4)

        notebook.add(frameDados, text=" Dados ")

        #------------------------
        #------ Aba 9 Info ------
        #------------------------
        frameInfo = Frame(notebook, bg=self._cinza)

        self.addTitulo(frameInfo, " >> Info << ", self._branco, self._font4)

        notebook.add(frameInfo, text=" Info ")


        #---------------END ABAS-----------------
        notebook.pack(side=TOP, fill=X)
    
    #---------------------------------------------------------------------
    def centralizar(self, larg, alt):
        px=int((self.master.winfo_screenwidth()-larg)/2)
        py=int((self.master.winfo_screenheight()-alt)/2)
        self.master.geometry("{}x{}+{}+{}".format(larg, alt, px, py))

    #---------------------------------------------------------------------
    def addTitulo(self, frame, titulo, corFundo=_cinza, fonte=_font2, justificado=TOP):
        self.frame = Frame(frame, bg=corFundo, height=80)
        self.frame.pack(side=TOP,fill=X) 
        self.texto = Label(self.frame,bg=corFundo, font=fonte, text=titulo)
        self.texto.pack(side=justificado) 

    #---------------------------------------------------------------------
    #nao sera usado
    def addEntrada(self, frame, corFundo=_cinza, fonte=_font2, justificado=TOP):
        self.frame = Frame(frame, bg=corFundo, height=80)
        self.frame.pack(side=TOP,fill=X)
        self.entrada = Entry(self.frame, width=80, bg=self._branco, font=fonte)
        self.entrada.pack(side=LEFT, fill=X)

    #---------------------------------------------------------------------
    # Não será usado
    def addBotao(self, frame, texto, fonte=_font2, framePos=TOP, botaoPos=RIGHT):
        self.frame = Frame(frame, bg=self._cinza, height=80)
        self.frame.pack(side=framePos,fill=X)
        var= StringVar() 
        self.botao = Button(self.frame, text=texto, command=var)
        self.botao.pack(side=botaoPos) 
    
    #---------------------------------------------------------------------
    def adicionarCliente(self):
        print("adicionando")
        nome = self.nomeCliente.get()
        telefone = self.telefoneCliente.get()
        cep = self.cepCliente.get()
        print("%s, %s, %s" %(nome, telefone, cep))

    #---------------------------------------------------------------------
    def limparCliente(self):
        self.nomeClienteEntry.set("")
        self.telefoneClienteEntry.set("")
        self.cepClienteEntry.set("")
        print("limpar")
        
    
    #---------------------------------------------------------------------    
    def botaoProcuraCaminho(self):
        caminho = filedialog.askdirectory()
        self.entradaCaminho.set(caminho)
        print(caminho)
    

    
app = FramePrincipal()
app.mainloop()