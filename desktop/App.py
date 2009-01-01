from src.controllers.defineProject import *
from src.controllers.getProject import *
from src.controllers.alterProject import *

from view.interfaceConfigs import *

from tkinter import * 

class Application:
    def __init__(self, master=None):
        self.fonte = ('Verdana', '8')
        
        # Containers configs
        self.container1 = Frame(master)
        configContainer(
            self.container1, 20, 5
        )
        
        self.container2 = Frame(master)
        configContainer(
            self.container2, 20, 5
        )
        
        self.container3 = Frame(master)
        configContainer(
            self.container3, 20, 5
        )
        
        self.container4 = Frame(master)
        configContainer(
            self.container4, 20, 5
        )
        
        self.container5 = Frame(master)
        configContainer(
            self.container5, 20, 5
        )
        
        self.container6 = Frame(master)
        configContainer(
            self.container6, 20, 5
        )
        
        self.container7 = Frame(master)
        configContainer(
            self.container7, 20, 5
        )
        
        self.container8 = Frame(master)
        configContainer(
            self.container8, 20, 10
        )
        
        self.container9 = Frame(master)
        configContainer(
            self.container9, 20, 10
        )
        
        # Title
        self.titulo = Label(self.container1, text='Informe os dados')
        self.titulo['font'] = ('Calibri', '9', 'bold')
        self.titulo.pack()
        
        # Search field configs
        self.lblidproject = Label(self.container2, text='ID Projeto:', font=self.fonte)
        self.lblidproject.pack(side=LEFT)
        
        self.txtidproject = Entry(self.container2)
        configTextBox(
            self.txtidproject, 25, self.fonte
        )
        
        self.btnBuscar = Button(self.container2, text='Buscar', font=self.fonte, width=10)
        self.btnBuscar['command'] = self.searchProject
        self.btnBuscar.pack(side=RIGHT)
        
        self.lbldescription = Label(self.container3, text='Resumo', font=self.fonte)
        self.lbldescription.pack(side=LEFT)
        
        self.txtdescription = Entry(self.container3)
        configTextBox(
            self.txtdescription, 25, self.fonte
        )
        
        self.lblobjective = Label(self.container4, text='Objetivo', font=self.fonte)
        self.lblobjective.pack(side=LEFT)
        
        self.txtobjective = Entry(self.container4)
        configTextBox(
            self.txtobjective, 25, self.fonte
        )
        
        self.lblhistory = Label(self.container5, text='História', font=self.fonte)
        self.lblhistory.pack(side=LEFT)
        
        self.txthistory = Entry(self.container5)
        configTextBox(
            self.txthistory, 25, self.fonte
        )
        
        self.lblassets = Label(self.container6, text='Assets Fundamentais', font=self.fonte)
        self.lblassets.pack(side=LEFT)
        
        self.txtassets = Entry(self.container6)
        configTextBox(
            self.txtassets, 25, self.fonte
        )
        
        self.lblanimations = Label(self.container7, text='Animações/cinemáticas', font=self.fonte)
        self.lblanimations.pack(side=LEFT)
        
        self.txtanimations = Entry(self.container7)
        configTextBox(
            self.txtanimations, 25, self.fonte
        )
        
        self.lbllevels = Label(self.container3, text='Níveis Fundamentais', font=self.fonte)
        self.lbllevels.pack(side=LEFT)
        
        self.txtlevels = Entry(self.container3)
        configTextBox(
            self.txtlevels, 25, self.fonte
        )
        self.txtlevels.pack(side=LEFT)
        
        self.lblnetwork = Label(self.container4, text='Baseado em rede?', font=self.fonte)
        self.lblnetwork.pack(side=LEFT)
        
        self.txtnetwork = Entry(self.container4)
        configTextBox(
            self.txtnetwork, 25, self.fonte
        )
        self.txtnetwork.pack(side=LEFT)
        
        self.lblaudio = Label(self.container5, text='Música', font=self.fonte)
        self.lblaudio.pack(side=LEFT)
        
        self.txtaudio = Entry(self.container5)
        configTextBox(
            self.txtaudio, 25, self.fonte
        )
        self.txtaudio.pack(side=LEFT)
        
        self.lblmaingameplay = Label(self.container6, text='Jogabilidade Principal', font=self.fonte)
        self.lblmaingameplay.pack(side=LEFT)
        
        self.txtmaingameplay = Entry(self.container6)
        configTextBox(
            self.txtmaingameplay, 25, self.fonte
        )
        self.txtmaingameplay.pack(side=LEFT)
        
        self.lblsecgameplay = Label(self.container7, text='Mecânicas Secundárias', font=self.fonte)
        self.lblsecgameplay.pack(side=LEFT)
        
        self.txtsecgameplay = Entry(self.container7)
        configTextBox(
            self.txtsecgameplay, 25, self.fonte
        )
        self.txtsecgameplay.pack(side=LEFT)
        
        # Buttons
        self.btnCriar = Button(self.container8, font=self.fonte)
        configButton(
            self.btnCriar,
            'Criar',
            self.newProject
        )
        
        self.btnAlterar = Button(self.container8, font=self.fonte)
        configButton(
            self.btnAlterar,
            'Alterar',
            self.changeProject 
        )
        
        self.btnDeletar = Button(self.container8, font=self.fonte)
        configButton(
            self.btnDeletar,
            'Deletar',
            self.excludeProject
        )
        
        self.lblmsg = Label(self.container9, text='', font=self.fonte)
        self.lblmsg.pack()
        
        self.formInputs = [
            self.txtdescription,
            self.txtobjective,
            self.txthistory,
            self.txtassets,
            self.txtanimations,
            self.txtlevels,
            self.txtnetwork,
            self.txtaudio,
            self.txtmaingameplay,
            self.txtsecgameplay, 
        ]   
    
    # Handle project creation
    def newProject(self):        
        project = {
            'description':self.txtdescription.get(),
            'objective':self.txtobjective.get(),
            'history':self.txthistory.get(),
            'assets':self.txtassets.get(),
            'animations':self.txtanimations.get(),
            'levels':self.txtlevels.get(),
            'network':self.txtnetwork.get(),
            'audio':self.txtaudio.get(),
            'main_gameplay':self.txtmaingameplay.get(),
            'sec_gameplay':self.txtsecgameplay.get(),
        }
        
        self.lblmsg['text'] = createGameProject(project)
        
        for t in self.formInputs:
            t.delete(0, END)
    
    # Handle project update 
    def changeProject(self):
        project = [
            self.txtdescription.get(),
            self.txtobjective.get(),
            self.txthistory.get(),
            self.txtassets.get(),
            self.txtanimations.get(),
            self.txtlevels.get(),
            self.txtnetwork.get(),
            self.txtaudio.get(),
            self.txtmaingameplay.get(),
            self.txtsecgameplay.get(),
        ]
        
        self.lblmsg['text'] = updateGameProject(self.txtidproject.get(), project)
        
        for t in self.formInputs:
            t.delete(0, END)
    
    # Handle project exclusion
    def excludeProject(self):
        self.lblmsg['text'] = deleteGameProject(self.txtidproject.get())
        
        for t in self.formInputs:
            t.delete(0, END)
    
    # Handle project search
    def searchProject(self):  
        res = getGameProject(self.txtidproject.get())
        
        self.lblmsg['text'] = res['message']
        
        if res['register'] is not None:
            for i, t in enumerate(self.formInputs):
                t.delete(0, END)
                t.insert(INSERT, res['register'][i])
    
root = Tk()
Application(root)
root.mainloop()