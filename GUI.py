from tkinter import *
from tkinter import filedialog
import tkinter.ttk as ttk

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

    def centralizar(self, larg, alt):
        px=int((self.master.winfo_screenwidth()-larg)/2)
        py=int((self.master.winfo_screenheight()-alt)/2)
        self.master.geometry("{}x{}+{}+{}".format(larg, alt, px, py))

    def botaoProcuraCaminho():
        caminho = filedialog.askdirectory()
        print(caminho)
        self.caminhoExportar.set(caminho)
        return str(caminho)
    
    def __init__(self, master=None):
        
        #------------------------
        #-------- Janela --------
        #------------------------
        super().__init__()
        self.master.iconbitmap("pedepizza.ico")
        self.centralizar(700,600)
        self.master.title("Pé de Pizza")
        self.master.resizable(False, False)
        self.pack()

        

        #criando noteBook. Aka "container de abas"
        notebook = ttk.Notebook(self.master)

        #--------------------------
        #------ Aba 1 Pedido ------
        #--------------------------
        framePedido = Frame(notebook, bg=self._cinza, height=590, width=690)
            #Titulo
        frameTituloPedido = Frame(framePedido, bg=self._cinza, height=50, width=690)
        frameTituloPedido.pack(side=TOP, fill=X, pady=10)
        self.tituloPedido = Label(frameTituloPedido, text="Pedidos", bg=self._branco, font=self._font4)
        self.tituloPedido.pack(side=TOP, fill=X)
        
        #---------------------------
        #------ Aba 2 Cliente ------
        #---------------------------
        frameCliente = Frame(bg=self._cinza, height=590, width=690)
            #Titulo
        frameTituloCliente = Frame(frameCliente, bg=self._cinza, height=50, width=690)
        frameTituloCliente.pack(side=TOP, fill=X, pady=10)
        self.tituloCliente = Label(frameTituloCliente, text="Adicionar Cliente", bg=self._branco, font=self._font4)
        self.tituloCliente.pack(side=TOP, fill=X)

            #Nome
        frameNome = Frame(frameCliente, bg=self._cinza)
        frameNome.pack(side=TOP, fill=X, pady=10)
        self.nomeCliente = Label(frameNome, text="Nome:", bg=self._cinza, font=self._font2)
        self.nomeCliente.pack(side=LEFT , ipadx=5, ipady=5)
        self.nomeCliente = Entry(frameNome, width=60, bg=self._branco, font=self._font2 )
        self.nomeCliente.pack(side=RIGHT, padx=20)
        self.nomeCliente.focus_set()
            
            #Telefone
        frameTelefone = Frame(frameCliente, bg=self._cinza, height=50, width=690)
        frameTelefone.pack(side=TOP, fill=X, pady=10)
        self.telefoneCliente = Label(frameTelefone, text="Telefone:", bg=self._cinza, font=self._font2)
        self.telefoneCliente.pack(side=LEFT, ipadx=5, ipady=5)
        self.telefoneCliente = Entry(frameTelefone, width=60, bg=self._branco, font=self._font2 )
        self.telefoneCliente.pack(side=RIGHT, padx=20)
        self.telefoneCliente.focus_set()

            #CEP
        frameCEP = Frame(frameCliente, bg=self._cinza, height=50, width=690)
        frameCEP.pack(side=TOP, fill=X, pady=10)
        self.CEPCliente = Label(frameCEP, text="CEP:", bg=self._cinza, font=self._font2)
        self.CEPCliente.pack(side=LEFT, ipadx=5, ipady=5)
        self.CEPCliente = Entry(frameCEP, width=60, bg=self._branco, font=self._font2 )
        self.CEPCliente.pack(side=RIGHT, padx=20)
        self.CEPCliente.focus_set()

            #Rua
        frameRua = Frame(frameCliente, bg=self._cinza, height=50, width=690)
        frameRua.pack(side=TOP, fill=X, pady=10)
        self.ruaCliente = Label(frameRua, text="Rua:", bg=self._cinza, font=self._font2)
        self.ruaCliente.pack(side=LEFT, ipadx=5, ipady=5)
        self.ruaCliente = Entry(frameRua, width=60, bg=self._branco, font=self._font2 )
        self.ruaCliente.pack(side=RIGHT, padx=20)
        self.ruaCliente.focus_set()

            #Numero
        frameNumero = Frame(frameCliente, bg=self._cinza, height=50, width=690)
        frameNumero.pack(side=TOP, fill=X, pady=10)
        self.numeroCliente = Label(frameNumero, text="Número:", bg=self._cinza, font=self._font2)
        self.numeroCliente.pack(side=LEFT, ipadx=5, ipady=5)
        self.numeroCliente = Entry(frameNumero, width=60, bg=self._branco, font=self._font2 )
        self.numeroCliente.pack(side=RIGHT, padx=20)
        self.numeroCliente.focus_set()

            #Complemento
        frameComplemento = Frame(frameCliente, bg=self._cinza, height=50, width=690)
        frameComplemento.pack(side=TOP, fill=X, pady=10)
        self.complementoCliente = Label(frameComplemento, text="Complemento:", bg=self._cinza, font=self._font2)
        self.complementoCliente.pack(side=LEFT, ipadx=0, ipady=5)
        self.complementoCliente = Entry(frameComplemento, width=60, bg=self._branco, font=self._font2 )
        self.complementoCliente.pack(side=RIGHT, padx=20)
        self.complementoCliente.focus_set()

            #Bairro
        frameBairro = Frame(frameCliente, bg=self._cinza, height=50, width=690)
        frameBairro.pack(side=TOP, fill=X, pady=10)
        self.bairroCliente = Label(frameBairro, text="Bairro:", bg=self._cinza, font=self._font2)
        self.bairroCliente.pack(side=LEFT, ipadx=5, ipady=5)
        self.bairroCliente = Entry(frameBairro, width=60, bg=self._branco, font=self._font2 )
        self.bairroCliente.pack(side=RIGHT, padx=20)
        self.bairroCliente.focus_set()
        
            #Botoes
        frameBotoes = Frame(frameCliente, bg=self._cinza, height=50, width=690)
        frameBotoes.pack(side=BOTTOM, fill=X, pady=10)
        self.btnAdicionarCliente = Button(frameBotoes, width=10, text="Adicionar")
        self.btnAdicionarCliente.pack(side=RIGHT, padx=10)
        self.btnLimparCliente = Button(frameBotoes, width=10, text="Limpar")
        self.btnLimparCliente.pack(side=RIGHT, padx=10)

        #--------------------------
        #------ Aba 3 Pizzas ------
        #--------------------------
        framePizza = Frame(notebook, bg=self._cinza, height=590, width=690)
            #Titulo
        frameTituloPizza = Frame(framePizza, bg=self._cinza, height=50, width=690)
        frameTituloPizza.pack(side=TOP, fill=X, pady=10)
        self.tituloPizza = Label(frameTituloPizza, text="Adicionar Pizza", bg=self._branco, font=self._font4)
        self.tituloPizza.pack(side=TOP, fill=X)

            #Sabor
        frameSabor = Frame(framePizza, bg=self._cinza, height=50, width=690)
        frameSabor.pack(side=TOP, fill=X, pady=10)
        self.saborPizza = Label(frameSabor, text="Sabor:", bg=self._cinza, font=self._font2)
        self.saborPizza.pack(side=LEFT, ipadx=0, ipady=5)
        self.saborPizza = Entry(frameSabor, width=60, bg=self._branco, font=self._font2 )
        self.saborPizza.pack(side=RIGHT, padx=20)
        self.saborPizza.focus_set()

            #Preço
        framePreco = Frame(framePizza, bg=self._cinza, height=50, width=690)
        framePreco.pack(side=TOP, fill=X, pady=10)
        self.precoPizza = Label(framePreco, text="Preço:", bg=self._cinza, font=self._font2)
        self.precoPizza.pack(side=LEFT, ipadx=5, ipady=5)
        self.precoPizza = Entry(framePreco, width=60, bg=self._branco, font=self._font2 )
        self.precoPizza.pack(side=RIGHT, padx=20)
        self.precoPizza.focus_set()
        
            #Botoes
        frameBotoesPizza = Frame(framePizza, bg=self._cinza, height=50, width=690)
        frameBotoesPizza.pack(side=BOTTOM, fill=X, pady=10)
        self.btnAdicionarCliente = Button(frameBotoesPizza, width=10, text="Adicionar")
        self.btnAdicionarCliente.pack(side=RIGHT, padx=10)
        self.btnLimparCliente = Button(frameBotoesPizza, width=10, text="Limpar")
        self.btnLimparCliente.pack(side=RIGHT, padx=10)

        #---------------------------
        #------ Aba 4 Deletar ------
        #---------------------------
        frameDeletar = Frame(notebook, bg=self._cinza, height=590, width=690)
            #Titulo
        frameTituloDeletar = Frame(frameDeletar, bg=self._cinza, height=50, width=690)
        frameTituloDeletar.pack(side=TOP, fill=X, pady=10)
        self.tituloDeletar = Label(frameTituloDeletar, text="Deletar Dados", bg=self._branco, font=self._font4)
        self.tituloDeletar.pack(side=TOP, fill=X)

        #-------------------------------
        #------ Aba 5 Faturamento ------
        #-------------------------------
        frameFaturamento = Frame(notebook, bg=self._cinza, height=590, width=690)
            #Titulo
        frameTituloFaturamento = Frame(frameFaturamento, bg=self._cinza, height=50, width=690)
        frameTituloFaturamento.pack(side=TOP, fill=X, pady=10)
        self.tituloFaturamento = Label(frameTituloFaturamento, text="Faturamento", bg=self._branco, font=self._font4)
        self.tituloFaturamento.pack(side=TOP, fill=X)

        #----------------------------
        #------ Aba 6 Importar ------
        #----------------------------
        frameImportar = Frame(notebook, bg=self._cinza, height=590, width=690)
                #Titulo
        frameTituloImportar = Frame(frameImportar, bg=self._cinza, height=50, width=690)
        frameTituloImportar.pack(side=TOP, fill=X, pady=10)
        self.tituloImportar = Label(frameTituloImportar, text="Importar Dados", bg=self._branco, font=self._font4)
        self.tituloImportar.pack(side=TOP, fill=X)

            #URL
        frameURL = Frame(frameImportar, bg=self._cinza, height=50, width=690)
        frameURL.pack(side=TOP, fill=X, pady=10)
        self.URLImportar = Label(frameURL, text="URL:", bg=self._cinza, font=self._font2)
        self.URLImportar.pack(side=LEFT, ipadx=5, ipady=5)
        self.URLImportar = Entry(frameURL, width=60, bg=self._branco, font=self._font2 )
        self.URLImportar.pack(side=RIGHT, padx=20)
        self.URLImportar.focus_set()

            #Botoes
        frameBotoesImportar = Frame(frameImportar, bg=self._cinza, height=50, width=690)
        frameBotoesImportar.pack(side=BOTTOM, fill=X, pady=10)
        self.btnAdicionarDados = Button(frameBotoesImportar, width=10, text="Carregar")
        self.btnAdicionarDados.pack(side=RIGHT, padx=10)
        self.btnLimparDados = Button(frameBotoesImportar, width=10, text="Limpar")
        self.btnLimparDados.pack(side=RIGHT, padx=10)
        
        #----------------------------
        #------ Aba 7 Exportar ------
        #----------------------------
        frameExportar = Frame(notebook, bg=self._cinza, height=590, width=690)
            #Titulo
        frameTituloExportar = Frame(frameExportar, bg=self._cinza, height=50, width=690)
        frameTituloExportar.pack(side=TOP, fill=X, pady=10)
        self.tituloExportar = Label(frameTituloExportar, text="Exportar Dados", bg=self._branco, font=self._font4)
        self.tituloExportar.pack(side=TOP, fill=X)

            #Caminho
        frameCaminhoExportar = Frame(frameExportar, bg=self._cinza, height=50, width=690)
        frameCaminhoExportar.pack(side=TOP, fill=X, pady=10)
        self.caminhoExportar = Label(frameCaminhoExportar, text="Caminho :", bg=self._cinza, font=self._font2)
        self.caminhoExportar.pack(side=LEFT, ipadx=5, ipady=5)
        self.caminhoExportar = Entry(frameCaminhoExportar, width=60, bg=self._branco, font=self._font2)
        self.caminhoExportar.pack(side=LEFT, padx=10)
        self.btnProcuraCaminho = Button(frameCaminhoExportar, width=10, text="...", command=self.botaoProcuraCaminho)
        self.btnProcuraCaminho.pack(side=RIGHT, padx=10)
        
            #Botoes
        frameBotoesExportar = Frame(frameExportar, bg=self._cinza, height=50, width=690)
        frameBotoesExportar.pack(side=BOTTOM, fill=X, pady=10)
        self.btnExportarDados = Button(frameBotoesExportar, width=10, text="Exportar")
        self.btnExportarDados.pack(side=RIGHT, padx=10)
        self.btnLimparExportacao = Button(frameBotoesExportar, width=10, text="Limpar")
        self.btnLimparExportacao.pack(side=RIGHT, padx=10)

        #-------------------------
        #------ Aba 8 Dados ------
        #-------------------------
        frameDados = Frame(notebook, bg=self._cinza, height=590, width=690)
            #Titulo
        frameTituloDados = Frame(frameDados, bg=self._cinza, height=50, width=690)
        frameTituloDados.pack(side=TOP, fill=X, pady=10)
        self.tituloDados = Label(frameTituloDados, text="Relatórios", bg=self._branco, font=self._font4)
        self.tituloDados.pack(side=TOP, fill=X)

        #------------------------
        #------ Aba 9 Info ------
        #------------------------
        frameInfo = Frame(notebook, bg=self._cinza, height=590, width=690)
            #Titulo
        frameTituloInfo = Frame(frameInfo, bg=self._cinza, height=50, width=690)
        frameTituloInfo.pack(side=TOP, fill=X, pady=10)
        self.tituloInfo = Label(frameTituloInfo, text="Informações", bg=self._branco, font=self._font4)
        self.tituloInfo.pack(side=TOP, fill=X)

        self.infoInfo = Label(frameInfo, text=self._info, bg=self._cinza, font=self._font3)
        self.infoInfo.pack(side=TOP, fill=X)
        self.infoInfo = Label(frameInfo, bg=self._cinza, font=self._font3)
        self.infoInfo.pack(side=TOP, fill=X)
        self.infoInfo = Label(frameInfo, text=self._autores, bg=self._cinza, font=self._font4)
        self.infoInfo.pack(side=TOP, fill=X)
        self.infoInfo = Label(frameInfo, text=self._empresa, bg=self._cinza, font=self._font3)
        self.infoInfo.pack(side=TOP, fill=X)

        #Adicionando as abas no notebook
        notebook.add(framePedido, text="Pedido")
        notebook.add(frameCliente, text="Clientes")
        notebook.add(framePizza, text="Pizzas")
        notebook.add(frameDeletar, text="Deletar")
        notebook.add(frameFaturamento, text="Faturamento")
        notebook.add(frameImportar, text="Importar")
        notebook.add(frameExportar, text="Exportar")
        notebook.add(frameDados, text="Dados")
        notebook.add(frameInfo, text="Info")
        notebook.pack()

    



app = FramePrincipal()
app.mainloop()