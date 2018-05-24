from tkinter import *
from tkinter import filedialog
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
        font4 = "Helvetica 18"

        #Strings
        info = '''Pé de Pizza é uma aplicação para gerenciamento de pizzaria.
        Desenvolvido na linguagem Python,
        o programa tem seu código fonte aberto, 
        esta licenciado sobre os termos do MIT 
        e pode ser baixado diretamento no gitHub pelo seguinte link:  '''
        autores = "Flavio Matioli & Gabriel Nardini"
        empresa = "PyCaretas LTDA"

        caminho = ""
        #-------------------------
        #-------- Funções --------
        #-------------------------

        def botaoProcuraCaminho():
            caminho = filedialog.askdirectory()
            print(caminho)
            self.caminhoExportar.set(caminho)
            return str(caminho)

        #------------------------
        #-------- Janela --------
        #------------------------
        super().__init__()
        self.master.iconbitmap("pedepizza.ico")
        self.master.geometry("700x600")
        self.master.title("Pé de Pizza")
        self.master.resizable(False, False)
        self.pack()

        #criando noteBook. Aka "container de abas"
        notebook = ttk.Notebook(self.master)

        #--------------------------
        #------ Aba 1 Pedido ------
        #--------------------------
        framePedido = Frame(notebook, bg=cinza, height=590, width=690)
            #Titulo
        frameTituloPedido = Frame(framePedido, bg=cinza, height=50, width=690)
        frameTituloPedido.pack(side=TOP, fill=X, pady=10)
        self.tituloPedido = Label(frameTituloPedido, text="Pedidos", bg=branco, font=font4)
        self.tituloPedido.pack(side=TOP, fill=X)
        
        #---------------------------
        #------ Aba 2 Cliente ------
        #---------------------------
        frameCliente = Frame(bg=cinza, height=590, width=690)
            #Titulo
        frameTituloCliente = Frame(frameCliente, bg=cinza, height=50, width=690)
        frameTituloCliente.pack(side=TOP, fill=X, pady=10)
        self.tituloCliente = Label(frameTituloCliente, text="Adicionar Cliente", bg=branco, font=font4)
        self.tituloCliente.pack(side=TOP, fill=X)

            #Nome
        frameNome = Frame(frameCliente, bg=cinza)
        frameNome.pack(side=TOP, fill=X, pady=10)
        self.nomeCliente = Label(frameNome, text="Nome:", bg=cinza, font=font2)
        self.nomeCliente.pack(side=LEFT , ipadx=5, ipady=5)
        self.nomeCliente = Entry(frameNome, width=60, bg=branco, font=font2 )
        self.nomeCliente.pack(side=RIGHT, padx=20)
        self.nomeCliente.focus_set()
            
            #Telefone
        frameTelefone = Frame(frameCliente, bg=cinza, height=50, width=690)
        frameTelefone.pack(side=TOP, fill=X, pady=10)
        self.telefoneCliente = Label(frameTelefone, text="Telefone:", bg=cinza, font=font2)
        self.telefoneCliente.pack(side=LEFT, ipadx=5, ipady=5)
        self.telefoneCliente = Entry(frameTelefone, width=60, bg=branco, font=font2 )
        self.telefoneCliente.pack(side=RIGHT, padx=20)
        self.telefoneCliente.focus_set()

            #CEP
        frameCEP = Frame(frameCliente, bg=cinza, height=50, width=690)
        frameCEP.pack(side=TOP, fill=X, pady=10)
        self.CEPCliente = Label(frameCEP, text="CEP:", bg=cinza, font=font2)
        self.CEPCliente.pack(side=LEFT, ipadx=5, ipady=5)
        self.CEPCliente = Entry(frameCEP, width=60, bg=branco, font=font2 )
        self.CEPCliente.pack(side=RIGHT, padx=20)
        self.CEPCliente.focus_set()

            #Rua
        frameRua = Frame(frameCliente, bg=cinza, height=50, width=690)
        frameRua.pack(side=TOP, fill=X, pady=10)
        self.ruaCliente = Label(frameRua, text="Rua:", bg=cinza, font=font2)
        self.ruaCliente.pack(side=LEFT, ipadx=5, ipady=5)
        self.ruaCliente = Entry(frameRua, width=60, bg=branco, font=font2 )
        self.ruaCliente.pack(side=RIGHT, padx=20)
        self.ruaCliente.focus_set()

            #Numero
        frameNumero = Frame(frameCliente, bg=cinza, height=50, width=690)
        frameNumero.pack(side=TOP, fill=X, pady=10)
        self.numeroCliente = Label(frameNumero, text="Número:", bg=cinza, font=font2)
        self.numeroCliente.pack(side=LEFT, ipadx=5, ipady=5)
        self.numeroCliente = Entry(frameNumero, width=60, bg=branco, font=font2 )
        self.numeroCliente.pack(side=RIGHT, padx=20)
        self.numeroCliente.focus_set()

            #Complemento
        frameComplemento = Frame(frameCliente, bg=cinza, height=50, width=690)
        frameComplemento.pack(side=TOP, fill=X, pady=10)
        self.complementoCliente = Label(frameComplemento, text="Complemento:", bg=cinza, font=font2)
        self.complementoCliente.pack(side=LEFT, ipadx=0, ipady=5)
        self.complementoCliente = Entry(frameComplemento, width=60, bg=branco, font=font2 )
        self.complementoCliente.pack(side=RIGHT, padx=20)
        self.complementoCliente.focus_set()

            #Bairro
        frameBairro = Frame(frameCliente, bg=cinza, height=50, width=690)
        frameBairro.pack(side=TOP, fill=X, pady=10)
        self.bairroCliente = Label(frameBairro, text="Bairro:", bg=cinza, font=font2)
        self.bairroCliente.pack(side=LEFT, ipadx=5, ipady=5)
        self.bairroCliente = Entry(frameBairro, width=60, bg=branco, font=font2 )
        self.bairroCliente.pack(side=RIGHT, padx=20)
        self.bairroCliente.focus_set()
        
            #Botoes
        frameBotoes = Frame(frameCliente, bg=cinza, height=50, width=690)
        frameBotoes.pack(side=BOTTOM, fill=X, pady=10)
        self.btnAdicionarCliente = Button(frameBotoes, width=10, text="Adicionar")
        self.btnAdicionarCliente.pack(side=RIGHT, padx=10)
        self.btnLimparCliente = Button(frameBotoes, width=10, text="Limpar")
        self.btnLimparCliente.pack(side=RIGHT, padx=10)

        #--------------------------
        #------ Aba 3 Pizzas ------
        #--------------------------
        framePizza = Frame(notebook, bg=cinza, height=590, width=690)
            #Titulo
        frameTituloPizza = Frame(framePizza, bg=cinza, height=50, width=690)
        frameTituloPizza.pack(side=TOP, fill=X, pady=10)
        self.tituloPizza = Label(frameTituloPizza, text="Adicionar Pizza", bg=branco, font=font4)
        self.tituloPizza.pack(side=TOP, fill=X)

            #Sabor
        frameSabor = Frame(framePizza, bg=cinza, height=50, width=690)
        frameSabor.pack(side=TOP, fill=X, pady=10)
        self.saborPizza = Label(frameSabor, text="Sabor:", bg=cinza, font=font2)
        self.saborPizza.pack(side=LEFT, ipadx=0, ipady=5)
        self.saborPizza = Entry(frameSabor, width=60, bg=branco, font=font2 )
        self.saborPizza.pack(side=RIGHT, padx=20)
        self.saborPizza.focus_set()

            #Preço
        framePreco = Frame(framePizza, bg=cinza, height=50, width=690)
        framePreco.pack(side=TOP, fill=X, pady=10)
        self.precoPizza = Label(framePreco, text="Preço:", bg=cinza, font=font2)
        self.precoPizza.pack(side=LEFT, ipadx=5, ipady=5)
        self.precoPizza = Entry(framePreco, width=60, bg=branco, font=font2 )
        self.precoPizza.pack(side=RIGHT, padx=20)
        self.precoPizza.focus_set()
        
            #Botoes
        frameBotoesPizza = Frame(framePizza, bg=cinza, height=50, width=690)
        frameBotoesPizza.pack(side=BOTTOM, fill=X, pady=10)
        self.btnAdicionarCliente = Button(frameBotoesPizza, width=10, text="Adicionar")
        self.btnAdicionarCliente.pack(side=RIGHT, padx=10)
        self.btnLimparCliente = Button(frameBotoesPizza, width=10, text="Limpar")
        self.btnLimparCliente.pack(side=RIGHT, padx=10)

        #---------------------------
        #------ Aba 4 Deletar ------
        #---------------------------
        frameDeletar = Frame(notebook, bg=cinza, height=590, width=690)
            #Titulo
        frameTituloDeletar = Frame(frameDeletar, bg=cinza, height=50, width=690)
        frameTituloDeletar.pack(side=TOP, fill=X, pady=10)
        self.tituloDeletar = Label(frameTituloDeletar, text="Deletar Dados", bg=branco, font=font4)
        self.tituloDeletar.pack(side=TOP, fill=X)

        #-------------------------------
        #------ Aba 5 Faturamento ------
        #-------------------------------
        frameFaturamento = Frame(notebook, bg=cinza, height=590, width=690)
            #Titulo
        frameTituloFaturamento = Frame(frameFaturamento, bg=cinza, height=50, width=690)
        frameTituloFaturamento.pack(side=TOP, fill=X, pady=10)
        self.tituloFaturamento = Label(frameTituloFaturamento, text="Faturamento", bg=branco, font=font4)
        self.tituloFaturamento.pack(side=TOP, fill=X)

        #----------------------------
        #------ Aba 6 Importar ------
        #----------------------------
        frameImportar = Frame(notebook, bg=cinza, height=590, width=690)
                #Titulo
        frameTituloImportar = Frame(frameImportar, bg=cinza, height=50, width=690)
        frameTituloImportar.pack(side=TOP, fill=X, pady=10)
        self.tituloImportar = Label(frameTituloImportar, text="Importar Dados", bg=branco, font=font4)
        self.tituloImportar.pack(side=TOP, fill=X)

            #URL
        frameURL = Frame(frameImportar, bg=cinza, height=50, width=690)
        frameURL.pack(side=TOP, fill=X, pady=10)
        self.URLImportar = Label(frameURL, text="URL:", bg=cinza, font=font2)
        self.URLImportar.pack(side=LEFT, ipadx=5, ipady=5)
        self.URLImportar = Entry(frameURL, width=60, bg=branco, font=font2 )
        self.URLImportar.pack(side=RIGHT, padx=20)
        self.URLImportar.focus_set()

            #Botoes
        frameBotoesImportar = Frame(frameImportar, bg=cinza, height=50, width=690)
        frameBotoesImportar.pack(side=BOTTOM, fill=X, pady=10)
        self.btnAdicionarDados = Button(frameBotoesImportar, width=10, text="Carregar")
        self.btnAdicionarDados.pack(side=RIGHT, padx=10)
        self.btnLimparDados = Button(frameBotoesImportar, width=10, text="Limpar")
        self.btnLimparDados.pack(side=RIGHT, padx=10)
        
        #----------------------------
        #------ Aba 7 Exportar ------
        #----------------------------
        frameExportar = Frame(notebook, bg=cinza, height=590, width=690)
            #Titulo
        frameTituloExportar = Frame(frameExportar, bg=cinza, height=50, width=690)
        frameTituloExportar.pack(side=TOP, fill=X, pady=10)
        self.tituloExportar = Label(frameTituloExportar, text="Exportar Dados", bg=branco, font=font4)
        self.tituloExportar.pack(side=TOP, fill=X)

            #Caminho
        frameCaminhoExportar = Frame(frameExportar, bg=cinza, height=50, width=690)
        frameCaminhoExportar.pack(side=TOP, fill=X, pady=10)
        self.caminhoExportar = Label(frameCaminhoExportar, text="Caminho :", bg=cinza, font=font2)
        self.caminhoExportar.pack(side=LEFT, ipadx=5, ipady=5)
        self.caminhoExportar = Entry(frameCaminhoExportar, width=60, bg=branco, font=font2)
        self.caminhoExportar.pack(side=LEFT, padx=10)
        self.btnProcuraCaminho = Button(frameCaminhoExportar, width=10, text="...", command=botaoProcuraCaminho)
        self.btnProcuraCaminho.pack(side=RIGHT, padx=10)
        
            #Botoes
        frameBotoesExportar = Frame(frameExportar, bg=cinza, height=50, width=690)
        frameBotoesExportar.pack(side=BOTTOM, fill=X, pady=10)
        self.btnExportarDados = Button(frameBotoesExportar, width=10, text="Exportar")
        self.btnExportarDados.pack(side=RIGHT, padx=10)
        self.btnLimparExportacao = Button(frameBotoesExportar, width=10, text="Limpar")
        self.btnLimparExportacao.pack(side=RIGHT, padx=10)

        #-------------------------
        #------ Aba 8 Dados ------
        #-------------------------
        frameDados = Frame(notebook, bg=cinza, height=590, width=690)
            #Titulo
        frameTituloDados = Frame(frameDados, bg=cinza, height=50, width=690)
        frameTituloDados.pack(side=TOP, fill=X, pady=10)
        self.tituloDados = Label(frameTituloDados, text="Relatórios", bg=branco, font=font4)
        self.tituloDados.pack(side=TOP, fill=X)

        #------------------------
        #------ Aba 9 Info ------
        #------------------------
        frameInfo = Frame(notebook, bg=cinza, height=590, width=690)
            #Titulo
        frameTituloInfo = Frame(frameInfo, bg=cinza, height=50, width=690)
        frameTituloInfo.pack(side=TOP, fill=X, pady=10)
        self.tituloInfo = Label(frameTituloInfo, text="Informações", bg=branco, font=font4)
        self.tituloInfo.pack(side=TOP, fill=X)

        self.infoInfo = Label(frameInfo, text=info, bg=cinza, font=font3)
        self.infoInfo.pack(side=TOP, fill=X)
        self.infoInfo = Label(frameInfo, bg=cinza, font=font3)
        self.infoInfo.pack(side=TOP, fill=X)
        self.infoInfo = Label(frameInfo, text=autores, bg=cinza, font=font4)
        self.infoInfo.pack(side=TOP, fill=X)
        self.infoInfo = Label(frameInfo, text=empresa, bg=cinza, font=font3)
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