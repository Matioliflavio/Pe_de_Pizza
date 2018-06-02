from tkinter import *

def cliente():
    frameCliente = Frame(bg=self._cinza)

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