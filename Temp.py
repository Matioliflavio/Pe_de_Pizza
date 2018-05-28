def preencherListBox(self):
        self.frame = Frame( bg="#d9d9d9", height=100, width=690)
        self.frame.pack(side=TOP, fill=X, pady=10)
        scrollY = Scrollbar(self.frame, orient=VERTICAL)
        self.lista = Listbox(self.frame, yscrollcommand=scrollY.set, height=5, font="Helvetica 12" , selectmode=SINGLE)

        self.lista.insert(END, "pizza1")
        self.lista.insert(END, "pizza2")
        self.lista.insert(END, "pizza3")
        self.lista.insert(END, "pizza4")
        self.lista.insert(END, "pizza5")
        self.lista.insert(END, "pizza6")
        self.lista.insert(END, "pizza7")
        self.lista.insert(END, "pizza8")
        self.lista.insert(END, "pizza9")

        self.lista.bind("<<ListboxSelect>>", self.onListSelect)

        self.lista.pack(side=LEFT, fill=X, expand=True)
        scrollY["command"] = self.lista.yview
        scrollY.pack(side=LEFT, fill=Y)
    
    def onListSelect(self, event):
        pos = self.lista.curselection()
        item = self.lista.get(pos)
        print("item: %s" %item)

    def addCheckBox(self, chaves):
        self.frame = Frame( bg="#d9d9d9", height=100, width=690)
        self.frame.pack(side=TOP, fill=X, pady=10)

        self.estados = []
        for item in chaves:
            var = IntVar()
            ckb = Checkbutton(self.frame, bg="#d9d9d9", font="Helvetica 12", text=item, variable=var, command=self.onCheckSelect)
            self.estados.append(var)
            ckb.pack(side=LEFT)

    def onCheckSelect(self):
        print("Seleciona5")

