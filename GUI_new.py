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
        Desenvolvido na linguagem Python, o programa tem seu código fonte aberto, 
        esta licenciado sobre os termos do MIT e pode ser baixado diretamente 
        do gitHub, pelo seguinte link:  '''
    _link = "https://github.com/Matioliflavio/Pe_de_Pizza"
    _autores = "Flavio Matioli & Gabriel Nardini"
    _empresa = "PyCaretas LTDA"

    _caminho = ""
    
    def __init__(self, master=None):
        
        #------------------------
        #-------- Janela --------
        #------------------------
        super().__init__()
        self.master.iconbitmap("pedepizza.ico")
        self.centralizar(600,500)
        self.master.title("Pé de Pizza")
        self.master.resizable(False, False)
        self.master["bg"] = self._cinza
        self.pack()

    
        #criando noteBook. Aka "container de abas"
        notebook = ttk.Notebook(self.master)

        ################################################################################################
        #------ Aba 1 Pedido  #################################### FUNCIONANDO #########################
        ################################################################################################
        framePedido = Frame(notebook, bg=self._cinza)

        self.addTitulo(framePedido, " >> Pedido << ", self._branco, self._font4)

        self.addTitulo(framePedido, "Cliente:", self._cinza, self._font2, LEFT)
        self.frameBuscaTitulo = Frame(framePedido, bg=self._cinza)
        self.frameBuscaTitulo.pack(side=TOP, fill=X)
        #Busca Cliente
        self.buscaClienteEntry= StringVar()
        self.buscaCliente = Entry(self.frameBuscaTitulo, width=70, bg=self._branco, font=self._font2, textvariable=self.buscaClienteEntry )
        self.buscaCliente.pack(side=LEFT, fill=X)
        self.buscaCliente.focus_set()
        self.btnBuscaCliente = Button(self.frameBuscaTitulo, width=10, text="Filtrar", command=self.botaoBuscaCliente)
        self.btnBuscaCliente.pack(side=LEFT, padx=10)

        #lista de busca
        self.frameResultadoBusca = Frame(framePedido, bg=self._cinza)
        self.frameResultadoBusca.pack(side=TOP, fill=X)
        scrollYCliente = Scrollbar(self.frameResultadoBusca, orient=VERTICAL)
        self.listaBusca = Listbox(self.frameResultadoBusca, yscrollcommand=scrollYCliente.set, height=4, width=50, font=self._font2, selectmode=SINGLE)
        self.listaBusca.bind("<<ListboxSelect>>", self.onListSelectBusca)
        self.listaBusca.pack(side=LEFT,fill=X,expand=True, pady=5)
        self.listaBusca.select_set(0)
        scrollYCliente["command"] = self.listaBusca.yview
        scrollYCliente.pack(side=LEFT,fill=Y, pady=5)
        
        self.botaoBuscaCliente()

        self.btnAdidcionarPedidoCliente = Button(self.frameResultadoBusca, width=10, text="Criar Pedido", state=DISABLED, command=self.criaPedido)
        self.btnAdidcionarPedidoCliente.pack(side=BOTTOM, padx=10)
        self.addTitulo(framePedido, " ", self._cinza, self._font1, LEFT)

        #seleção Pizza
        self.addTitulo(framePedido, "Pizza:", self._cinza, self._font2, LEFT)
        self.framePizzaPedido = Frame(framePedido, bg=self._cinza)
        self.framePizzaPedido.pack(side=TOP, fill=X)

        self.pizzas = mp.lista_pizzas()
        self.pz= []
        for pizza in self.pizzas:
                self.pz.append(str(pizza[0]) + " - " + pizza[1])
        self.comboPizzaPedido = ttk.Combobox(self.framePizzaPedido, font=self._font2, width=50, values=self.pz, state=DISABLED)
        self.comboPizzaPedido.pack(side=LEFT, fill=X)
        self.meia = IntVar()
        self.ckbMeiaPizza = Checkbutton(self.framePizzaPedido,bg=self._cinza,font=self._font2, text="Meia", state=DISABLED, variable=self.meia, command=self.meiaSelect)
        self.ckbMeiaPizza.pack(side=LEFT, padx=10)
        self.btnAdicionarPizzaPedido = Button(self.framePizzaPedido, width=20, text="Adicionar ao Pedido", state=DISABLED,command=self.botaoAdicionarPizzaPedido)
        self.btnAdicionarPizzaPedido.pack(side=LEFT, padx=10)

        #listaPedido
        self.addTitulo(framePedido, " ", self._cinza, self._font1, LEFT)
        self.addTitulo(framePedido, "Pedido: ", self._cinza, self._font2, LEFT)
        self.frameListaPedido = Frame(framePedido, bg=self._cinza)
        self.frameListaPedido.pack(side=TOP, fill=X)
        scrollYPedido = Scrollbar(self.frameListaPedido, orient=VERTICAL)
        self.listaPedido = Listbox(self.frameListaPedido, yscrollcommand=scrollYPedido.set, height=6, width=50, font=self._font2, selectmode=SINGLE)
        self.listaPedido.bind("<<ListboxSelect>>", self.onListSelectPedido)
        self.listaPedido.pack(side=LEFT,fill=X,expand=True, pady=5)
        self.listaPedido.select_set(0)
        scrollYPedido["command"] = self.listaPedido.yview
        scrollYPedido.pack(side=LEFT,fill=Y, pady=5)

        #Botões
        self.frameBotoesPedido = Frame(framePedido, bg=self._cinza)
        self.frameBotoesPedido.pack(side=BOTTOM, fill=X)
        self.btnAdicionarPedido = Button(self.frameBotoesPedido, width=12, text="Finaliza Pedido", command=self.btnSalvarPedido)
        self.btnAdicionarPedido.pack(side=RIGHT, padx=10)
        self.btnLimparPedido = Button(self.frameBotoesPedido, width=10, text="Limpar", command=self.limparPedido)
        self.btnLimparPedido.pack(side=RIGHT, padx=10)

        notebook.add(framePedido, text=" Pedido ")
        
        ################################################################################################
        #>>>>>> Aba 2 Cliente #################################### FUNCIONANDO #########################
        ################################################################################################
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

        ################################################################################################
        #>>>>>>> Aba 3 Pizzas #################################### FUNCIONANDO #########################
        ################################################################################################
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

        ################################################################################################
        #>>>>>> Aba 4 Deletar #################################### FUNCIONANDO #########################
        ################################################################################################
        frameDeletar = Frame(notebook, bg=self._cinza)

        self.addTitulo(frameDeletar, " >> Deletar << ", self._branco, self._font4)

        self.frameBotoesSelecDeletar = Frame(frameDeletar, bg=self._cinza)
        self.frameBotoesSelecDeletar.pack(side=TOP, fill=BOTH)
        self.btnListarClientes = Button(self.frameBotoesSelecDeletar, width=10, text="Listar Clientes", command=self.listarClientes)
        self.btnListarClientes.pack(side=LEFT, padx=10, pady=10)
        self.btnListarPizzas = Button(self.frameBotoesSelecDeletar, width=10, text="Listar Pizzas", command=self.listarPizzas)
        self.btnListarPizzas.pack(side=LEFT, padx=10, pady=10)
        
        self.frameListarDeletar = Frame(frameDeletar , bg=self._cinza, height=100)
        self.frameListarDeletar.pack(side=TOP,fill=X)

        scrollY = Scrollbar(self.frameListarDeletar, orient=VERTICAL)
        self.listaDeletar = Listbox(self.frameListarDeletar, yscrollcommand=scrollY.set, height=10, font=self._font2, selectmode=SINGLE)

        self.listaDeletar.bind("<<ListboxSelect>>", self.onListSelect)
        self.listaDeletar.pack(side=LEFT,fill=X,expand=True)

        self.listaDeletar.select_set(0)
        scrollY["command"] = self.listaDeletar.yview
        scrollY.pack(side=LEFT,fill=Y)

        self.frameBotoesDeletar = Frame(frameDeletar, bg=self._cinza)
        self.frameBotoesDeletar.pack(side=BOTTOM, fill=BOTH)
        self.btnDeletarSelecionado = Button(self.frameBotoesDeletar, width=10, text="Deletar", command=self.deletarSelecionado)
        self.btnDeletarSelecionado.pack(side=RIGHT, padx=10)
        self.btnListarPizzas = Button(self.frameBotoesDeletar, width=10, text="Limpar Lista", command=self.limparLista)
        self.btnListarPizzas.pack(side=RIGHT, padx=10)
        
        notebook.add(frameDeletar, text=" Deletar ")

        ################################################################################################
        #------ Aba 5 Faturamento ------
        ################################################################################################
        frameFaturamento = Frame(notebook, bg=self._cinza)

        self.addTitulo(frameFaturamento, " >> Faturamento << ", self._branco, self._font4)

        notebook.add(frameFaturamento, text=" Faturamento ")

        ################################################################################################
        #>>>>> Aba 6 Importar #################################### FUNCIONANDO #########################
        ################################################################################################
        frameImportar = Frame(notebook, bg=self._cinza)

        self.addTitulo(frameImportar, " >> Importar << ", self._branco, self._font4)

        self.addTitulo(frameImportar, "URL da Internet:", self._cinza,  self._font3, LEFT)
        frameURL = Frame(frameImportar, bg=self._cinza)
        frameURL.pack(side=TOP, fill=X)
        self.importaUrlEntry = StringVar()
        self.caminhoImportar = Entry(frameURL, width=80, bg=self._branco, font=self._font2, textvariable=self.importaUrlEntry)
        self.caminhoImportar.pack(side=LEFT, fill=X)
        self.caminhoImportar.focus_set()

        #lista Rsultado Import
        self.frameResultadoImport = Frame(frameImportar, bg=self._cinza)
        self.frameResultadoImport.pack(side=TOP, fill=X)
        self.frameResultadoImportXscr = Frame(frameImportar, bg=self._cinza)
        self.frameResultadoImportXscr.pack(side=TOP, fill=X)
        scrollYImport = Scrollbar(self.frameResultadoImport, orient=VERTICAL)
        scrollXImport = Scrollbar(self.frameResultadoImportXscr, orient=HORIZONTAL)
        self.listaImport = Listbox(self.frameResultadoImport, yscrollcommand=scrollYImport.set, xscrollcommand=scrollXImport.set, height=19, width=50, font=self._font2, selectmode=SINGLE)
        self.listaImport.pack(side=LEFT,fill=X,expand=True, pady=5)
        scrollYImport["command"] = self.listaImport.yview
        scrollYImport.pack(side=LEFT,fill=Y, pady=5)
        scrollXImport["command"] = self.listaImport.xview
        scrollXImport.pack(side=BOTTOM,fill=X)

        frameBotoesImportar = Frame(frameImportar, bg=self._cinza)
        frameBotoesImportar.pack(side=BOTTOM, fill=X)
        self.btnInportarDados = Button(frameBotoesImportar, width=10, text="Importar", command=self.importarDados)
        self.btnInportarDados.pack(side=RIGHT, padx=10)
        self.btnLimparURL = Button(frameBotoesImportar, width=10, text="Limpar", command=self.limparImportar)
        self.btnLimparURL.pack(side=RIGHT, padx=10)

        notebook.add(frameImportar, text=" Importar ")

        ################################################################################################
        #>>>>>> Aba 7 Exportar #################################### FUNCIONANDO ########################
        ################################################################################################
        frameExportar = Frame(notebook, bg=self._cinza)

        self.addTitulo(frameExportar, " >> Exportar << ", self._branco, self._font4)

        self.addTitulo(frameExportar, "Caminho:", self._cinza,  self._font3, LEFT)
        frameCaminho = Frame(frameExportar, bg=self._cinza)
        frameCaminho.pack(side=TOP, fill=X)
        self.exportaCaminhoEntry = StringVar()
        self.caminhoExportar = Entry(frameCaminho, width=70, bg=self._branco, font=self._font2, textvariable=self.exportaCaminhoEntry)
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

        ################################################################################################
        #------ Aba 8 Dados ------
        ################################################################################################
        frameDados = Frame(notebook, bg=self._cinza)

        self.addTitulo(frameDados, " >> Dados << ", self._branco, self._font4)

        notebook.add(frameDados, text=" Dados ")

        ################################################################################################
        #>>>>>>> Aba 9 Info #################################### FUNCIONANDO ###########################
        ################################################################################################
        frameInfo = Frame(notebook, bg=self._cinza)

        self.addTitulo(frameInfo, " >> Info << ", self._branco, self._font4)
        self.addTitulo(frameInfo, self._info, self._cinza, self._font3)
        self.addTitulo(frameInfo, self._link, self._branco, self._font3)
        self.addTitulo(frameInfo, " ", self._cinza, self._font4)
        self.addTitulo(frameInfo, self._autores, self._cinza, self._font2)
        self.addTitulo(frameInfo, self._empresa, self._cinza, self._font2)

        notebook.add(frameInfo, text=" Info ")

        #---------------END ABAS-----------------
        notebook.pack(side=TOP, fill=X)

        ################################################################################################
        ################################################################################################
        ################################################################################################
        ################################################################################################






    # ------------------------------------------------------------------------------------------
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> FUNÇÕES GERAIS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # ------------------------------------------------------------------------------------------ 
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
    def exibirMensagem(self, msg):
        mbox.showinfo("Atenção", msg)

    # ------------------------------------------------------------------------------------------
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> FUNÇÕES PEDIDO <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # ------------------------------------------------------------------------------------------   
    def botaoBuscaCliente(self):
        print("Buscando")
        self.listaBusca.delete(0, END)
        procura = self.buscaClienteEntry.get()
        clientes = mp.busca_clientes(procura)
        for cliente in clientes:
            cl = str(cliente[0]) + " - " + cliente[1]
            self.listaBusca.insert(END, cl)

    # ------------------------------------------------------------------------------------------
    def onListSelectBusca(self, arg):
        pos = self.listaBusca.curselection()
        self.clienteSelecionado = self.listaBusca.get(pos)
        self.btnAdidcionarPedidoCliente["state"] = ACTIVE
        print("Item: %s" %self.clienteSelecionado)

    # ------------------------------------------------------------------------------------------
    def botaoAdicionarPizzaPedido(self):
        print("Adicionar ao Pedido")
        sabor = self.comboPizzaPedido.get()
        idPizza = sabor[0] 
        meia = self.meia.get()
        pizza = mp.lista_pizza_por_id(idPizza)
        if meia:
            txtMeia = "Meia "
            valor = pizza[2]/2
        else:
            valor = pizza[2]
            txtMeia = "Inteira "
        
        idItem = mp.insere_item_pedido(self.pedidoAtivo, idPizza, 1, meia, str(valor))
        if idItem:
            print("Item inserido com sucesso!!!")
            self.pedidoAtivoValor += valor 
            self.listaPedido.delete(END)
            self.listaPedido.insert(END, txtMeia + sabor[4:] + " - Valor item R$:" + str(valor))
            self.listaPedido.insert(END, "-------------------> TOTAL Pedido R$:%.2f <-------------------" %self.pedidoAtivoValor)
        else:
            print("Deu Ruim ao inserir")

    # ------------------------------------------------------------------------------------------
    def meiaSelect(self):
        print("Meia Selecionada")

    # ------------------------------------------------------------------------------------------
    def onListSelectPedido(self):
        print("pedido")

    # ------------------------------------------------------------------------------------------
    def limparPedido(self):
        print("Limpa Pedido")
        self.pedidoAtivo = None
        self.btnAdidcionarPedidoCliente["state"] = DISABLED
        self.btnAdicionarPizzaPedido["state"]= DISABLED
        self.ckbMeiaPizza["state"]= DISABLED
        self.comboPizzaPedido["state"]= DISABLED
        self.pedidoAtivoValor = 0
        self.listaPedido.delete(0, END)

    # ------------------------------------------------------------------------------------------
    def btnSalvarPedido(self):
        print("Adiciona Pedido")
        txt = """   
        PEDIDO No: %s
        CLIENTE: %s
        VALOR R$: %.2f
        """ %(self.pedidoAtivo, self.clienteSelecionado, self.pedidoAtivoValor)
        result = mp.finaliza_pedido(self.clienteSelecionado[0], self.pedidoAtivoValor)
        if result: self.exibirMensagem(txt)
        self.limparPedido()
        
    # ------------------------------------------------------------------------------------------
    def criaPedido(self):
        self.pedidoAtivo = mp.insere_pedido(self.clienteSelecionado[0])
        self.pedidoAtivoValor = 0
        if self.pedidoAtivo:
            print("Pedido Criado")
            txt="Pedido n: %s    Cliente: %s" %(self.pedidoAtivo, str(self.clienteSelecionado))
            self.listaPedido.insert(END, txt)
            self.listaPedido.insert(END, "")
            self.btnAdicionarPizzaPedido["state"]= ACTIVE
            self.ckbMeiaPizza["state"]= ACTIVE
            self.comboPizzaPedido["state"]= ACTIVE
        else:
            self.exibirMensagem("Deu ruim")
    
    # -------------------------------------------------------------------------------------------
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> FUNÇÕES CLIENTE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # -------------------------------------------------------------------------------------------
    def adicionarCliente(self):
        print("adicionando")
        nome = str(self.nomeCliente.get()).upper()
        telefone = str(self.telefoneCliente.get())
        cep = str(self.cepCliente.get())
        rua = str(self.ruaClienteEntry.get())#.upper
        numero = str(self.numeroClienteEntry.get())
        complemento = str(self.complementoClienteEntry.get())#.upper()
        bairro = str(self.bairroClienteEntry.get())#.upper()
        cid=None
        cid = mp.insere_cliente(nome, telefone, cep, rua, numero, complemento, bairro)
        if cid:
            self.exibirMensagem("%s, ID: %s adicionado " %(nome, cid))
            self.limparCliente()
            self.botaoBuscaCliente()
        else:
            self.exibirMensagem("Falha ao adicionar")   

    # ------------------------------------------------------------------------------------------
    def limparCliente(self):
        self.nomeClienteEntry.set("")
        self.telefoneClienteEntry.set("")
        self.cepClienteEntry.set("")
        self.ruaClienteEntry.set("")
        self.complementoClienteEntry.set("")                
        self.numeroClienteEntry.set("")
        self.bairroClienteEntry.set("")
        print("limpar")

    # ------------------------------------------------------------------------------------------
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> FUNÇÕES PIZZAS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # ------------------------------------------------------------------------------------------
    def adicionarSabor(self):
        sabor = str(self.saborPizzasEntry.get()).upper()
        valor = str(self.valorPizzasEntry.get()).replace(",", ".")
        pid = mp.insere_pizza(sabor, valor)
        if pid:
            self.exibirMensagem("Inserida com Sucesso \nFavor Reiniciar o programa! ")
            self.limparSabor()
        else:
            self.exibirMensagem("Erro ao Inserir")

    # ------------------------------------------------------------------------------------------
    def limparSabor(self):
        self.saborPizzasEntry.set("")
        self.valorPizzasEntry.set("")
        print("limpar")

    # -------------------------------------------------------------------------------------------
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> FUNÇÕES DELETAR <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # -------------------------------------------------------------------------------------------
    
    def deletarSelecionado(self):
        id= self.itemDeletar[:2].replace(" ", "")
        print(id)
        if self.tipoDeletar == "P":
            delPizza = mp.deleta_pizza_por_id(str(id))
            if delPizza: self.exibirMensagem("Deletando %s" %self.itemDeletar)
            else: self.exibirMensagem("Erro ao Deletar %s" %self.itemDeletar)
        elif self.tipoDeletar == "C":
            delCliente = mp.deleta_cliente_por_id(str(id))
            if delCliente: self.exibirMensagem("Deletando %s" %self.itemDeletar)
            else: self.exibirMensagem("Erro ao Deletar %s" %self.itemDeletar)
        else:
            self.exibirMensagem("Selecione um item para deletar!")
            print("nada selecionado")
        self.limparLista()

    # ------------------------------------------------------------------------------------------
    def listarClientes(self):
        self.listaDeletar.delete(0, END)
        self.tipoDeletar = "C" 
        clientes = mp.lista_clientes()
        for cliente in clientes:
            cl = str(cliente[0]) + " - " + cliente[1]
            self.listaDeletar.insert(END, cl)
    # ------------------------------------------------------------------------------------------    
    def listarPizzas(self):
        self.listaDeletar.delete(0, END)
        self.tipoDeletar = "P"
        pizzas = mp.lista_pizzas()
        for pizza in pizzas:
            p= str(pizza[0]) + " - " + pizza[1]
            self.listaDeletar.insert(END, p)
    # ------------------------------------------------------------------------------------------    
    def limparLista(self):
        self.tipoDeletar = ""
        self.listaDeletar.delete(0, END)
    
    # ------------------------------------------------------------------------------------------ 
    def onListSelect(self, arg):
        pos = self.listaDeletar.curselection()
        self.itemDeletar = self.listaDeletar.get(pos)
        print("Item: %s" %self.itemDeletar)


    # -----------------------------------------------------------------------------------------------
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> FUNÇÕES FATURAMENTO <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # -----------------------------------------------------------------------------------------------


    # --------------------------------------------------------------------------------------------
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> FUNÇÕES IMPORTAR <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # --------------------------------------------------------------------------------------------
    def botaoProcuraCaminho(self):
        caminho = filedialog.askdirectory()
        self.exportaCaminhoEntry.set(caminho)
        print(caminho)

    # --------------------------------------------------------------------------------------------    
    def importarDados(self):
        print("importar")
        self.listaImport.insert(END, "Aguarde....")
        url = str(self.importaUrlEntry.get())
        self.listaImport.insert(END, "Carregando Dados....")
        self.resultadoImport = imp.importa_dados(url)
        self.listaImport.delete(0, END)
        for item in self.resultadoImport:
            self.listaImport.insert(END, str(item).replace("\'", "").replace("{", "").replace("}", ""))
        self.exibirMensagem("Importação Concluída!")
        self.importaUrlEntry.set("")
        self.buscaCliente()

    # --------------------------------------------------------------------------------------------    
    def limparImportar(self):
        self.importaUrlEntry.set("")
        self.listaImport.delete(0, END)

    # --------------------------------------------------------------------------------------------
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> FUNÇÕES EXPORTAR <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # --------------------------------------------------------------------------------------------
    def exportarDados(self):
        print("exportar")
        caminho = str(self.exportaCaminhoEntry.get())
        ed.cria_backup_json(caminho)
        self.exibirMensagem("Exportação Concluída!")

    #---------------------------------------------------------------------    
    def limparExportar(self):
        self.exportaCaminhoEntry.set("")

    # -----------------------------------------------------------------------------------------
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> FUNÇÕES DADOS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # -----------------------------------------------------------------------------------------


    ## -- Final das funções da GUI --

def main():
    app = FramePrincipal()
    app.mainloop()

main()