from tkinter import *
from tkinter import filedialog
import tkinter.ttk as ttk
from tkinter import messagebox as mbox
import ManipuladorDados as mp
import exportaDados as ed
import importaDados as imp



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
        self.centralizar(700,500)
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
        
        #--Rua--
        self.addTitulo(frameCliente, "Rua:", self._cinza,  self._font3, LEFT)
        frameRua = Frame(frameCliente, bg=self._cinza)
        frameRua.pack(side=TOP, fill=X)
        self.ruaClienteEntry= StringVar()
        self.ruaCliente = Entry(frameRua, width=80, bg=self._branco, font=self._font2, textvariable=self.ruaClienteEntry)
        self.ruaCliente.pack(side=LEFT, fill=X)

        #--Numero--
        self.addTitulo(frameCliente, "Numero:", self._cinza,  self._font3, LEFT)
        frameNumero = Frame(frameCliente, bg=self._cinza)
        frameNumero.pack(side=TOP, fill=X)
        self.numeroClienteEntry= StringVar()
        self.numeroCliente = Entry(frameNumero, width=80, bg=self._branco, font=self._font2, textvariable=self.numeroClienteEntry)
        self.numeroCliente.pack(side=LEFT, fill=X)

        #--Complemento--
        self.addTitulo(frameCliente, "Complemento:", self._cinza,  self._font3, LEFT)
        frameComplemento = Frame(frameCliente, bg=self._cinza)
        frameComplemento.pack(side=TOP, fill=X)
        self.complementoClienteEntry= StringVar()
        self.complemento = Entry(frameComplemento, width=80, bg=self._branco, font=self._font2, textvariable=self.complementoClienteEntry)
        self.complemento.pack(side=LEFT, fill=X)

        #--Bairro--
        self.addTitulo(frameCliente, "Bairro:", self._cinza,  self._font3, LEFT)
        frameBairro = Frame(frameCliente, bg=self._cinza)
        frameBairro.pack(side=TOP, fill=X)
        self.bairroClienteEntry= StringVar()
        self.bairroCliente = Entry(frameBairro, width=80, bg=self._branco, font=self._font2, textvariable=self.bairroClienteEntry)
        self.bairroCliente.pack(side=LEFT, fill=X)   

        frameVazio = Frame(frameCliente, bg=self._cinza, height=100).pack(side=TOP, fill=X)

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
        
        #--Sabor--
        self.addTitulo(framePizzas, "Sabor:", self._cinza,  self._font3, LEFT)
        frameSabor = Frame(framePizzas, bg=self._cinza)
        frameSabor.pack(side=TOP, fill=X)
        self.saborPizzasEntry= StringVar()
        self.saborPizzas = Entry(frameSabor, width=80, bg=self._branco, font=self._font2, textvariable=self.saborPizzasEntry )
        self.saborPizzas.pack(side=LEFT, fill=X)
        self.saborPizzas.focus_set()
        
        #--Valor--
        self.addTitulo(framePizzas, "Valor:", self._cinza,  self._font3, LEFT)
        frameValor = Frame(framePizzas, bg=self._cinza)
        frameValor.pack(side=TOP, fill=X)
        self.valorPizzasEntry= StringVar()
        self.valorPizzas = Entry(frameValor, width=80, bg=self._branco, font=self._font2, textvariable=self.valorPizzasEntry)
        self.valorPizzas.pack(side=LEFT, fill=X)
        
        frameVazio = Frame(framePizzas, bg=self._cinza, height=100).pack(side=TOP, fill=X)

        frameBotoesPizzas = Frame(framePizzas, bg=self._cinza)
        frameBotoesPizzas.pack(side=BOTTOM, fill=X)
        self.btnAdicionarSabor = Button(frameBotoesPizzas, width=10, text="Adicionar", command=self.adicionarSabor)
        self.btnAdicionarSabor.pack(side=RIGHT, padx=10)
        self.btnLimparSabor = Button(frameBotoesPizzas, width=10, text="Limpar", command=self.limparSabor)
        self.btnLimparSabor.pack(side=RIGHT, padx=10)
        
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

        self.addTitulo(frameImportar, "URL da Internet:", self._cinza,  self._font3, LEFT)
        frameURL = Frame(frameImportar, bg=self._cinza)
        frameURL.pack(side=TOP, fill=X)
        self.importaUrlEntry = StringVar()
        self.caminhoImportar = Entry(frameURL, width=80, bg=self._branco, font=self._font2, textvariable=self.importaUrlEntry)
        self.caminhoImportar.pack(side=LEFT, fill=X)
        self.caminhoImportar.focus_set()

        frameBotoesImportar = Frame(frameImportar, bg=self._cinza)
        frameBotoesImportar.pack(side=BOTTOM, fill=X)
        self.btnInportarDados = Button(frameBotoesImportar, width=10, text="Importar", command=self.importarDados)
        self.btnInportarDados.pack(side=RIGHT, padx=10)
        self.btnLimparURL = Button(frameBotoesImportar, width=10, text="Limpar", command=self.limparImportar)
        self.btnLimparURL.pack(side=RIGHT, padx=10)

        notebook.add(frameImportar, text=" Importar ")

        #----------------------------
        #------ Aba 7 Exportar ------
        #----------------------------
        frameExportar = Frame(notebook, bg=self._cinza)

        self.addTitulo(frameExportar, " >> Exportar << ", self._branco, self._font4)

        self.addTitulo(frameExportar, "Caminho:", self._cinza,  self._font3, LEFT)
        frameCaminho = Frame(frameExportar, bg=self._cinza)
        frameCaminho.pack(side=TOP, fill=X)
        self.exportaCaminhoEntry = StringVar()
        self.caminhoExportar = Entry(frameCaminho, width=80, bg=self._branco, font=self._font2, textvariable=self.exportaCaminhoEntry)
        self.caminhoExportar.pack(side=LEFT, fill=X)
        self.caminhoExportar.focus_set()
        self.btnProcuraCaminho = Button(frameCaminho, width=10, text="Buscar", command=self.botaoProcuraCaminho)
        self.btnProcuraCaminho.pack(side=RIGHT)

        frameBotoesExportar = Frame(frameExportar, bg=self._cinza)
        frameBotoesExportar.pack(side=BOTTOM, fill=X)
        self.btnExportarDados = Button(frameBotoesExportar, width=10, text="Exportar", command=self.exportarDados)
        self.btnExportarDados.pack(side=RIGHT, padx=10)
        self.btnLimparCaminho = Button(frameBotoesExportar, width=10, text="Limpar", command=self.limparExportar)
        self.btnLimparCaminho.pack(side=RIGHT, padx=10)

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
        nome = str(self.nomeCliente.get())
        telefone = str(self.telefoneCliente.get())
        cep = str(self.cepCliente.get())
        rua = str(self.ruaClienteEntry.get())
        numero = str(self.numeroClienteEntry.get())
        complemento = str(self.complementoClienteEntry.get())
        bairro = str(self.bairroClienteEntry.get())
        cid=None
        cid = mp.insere_cliente(nome, telefone, cep, rua, numero, complemento, bairro)
        if cid:
            self.exibirMensagem("%s, ID: %s adicionado " %(cliente, cid))
            self.limparCliente()
        else:
            self.exibirMensagem("Falha ao adicionar")    

    #---------------------------------------------------------------------
    def limparCliente(self):
        self.nomeClienteEntry.set("")
        self.telefoneClienteEntry.set("")
        self.cepClienteEntry.set("")
        self.ruaClienteEntry.set("")
        self.complementoClienteEntry.set("")                
        self.numeroClienteEntry.set("")
        self.bairroClienteEntry.set("")
        print("limpar")
        
    
    #---------------------------------------------------------------------    
    def botaoProcuraCaminho(self):
        caminho = filedialog.askdirectory()
        self.exportaCaminhoEntry.set(caminho)
        print(caminho)

    #---------------------------------------------------------------------    
    def importarDados(self):
        print("importar")
        url = str(self.importaUrlEntry.get())
        imp.importa_dados(url)
        self.exibirMensagem("Importação Concluída!")
        self.limparImportar()

    #---------------------------------------------------------------------    
    def limparImportar(self):
        self.importaUrlEntry.set("")

    #---------------------------------------------------------------------    
    def exportarDados(self):
        print("exportar")
        caminho = str(self.exportaCaminhoEntry.get())
        ed.cria_backup_json(caminho)
        self.exibirMensagem("Exportação Concluída!")

    #---------------------------------------------------------------------    
    def limparExportar(self):
        self.entradaCaminho.set("")

    #---------------------------------------------------------------------
    def exibirMensagem(self, msg):
        mbox.showinfo("Atenção", msg)

    #---------------------------------------------------------------------
    def adicionarSabor(self):
        sabor = str(self.saborPizzasEntry.get())
        valor = str(self.valorPizzasEntry.get()).replace(",", ".")
        pid = mp.insere_pizza(sabor, valor)
        if pid:
            self.exibirMensagem("Inserida com Sucesso")
            self.limparSabor()
        else:
            self.exibirMensagem("Erro ao Inserir")

    #---------------------------------------------------------------------
    def limparSabor(self):
        self.saborPizzasEntry.set("")
        self.valorPizzasEntry.set("")
        print("limpar")

    
app = FramePrincipal()
app.mainloop()