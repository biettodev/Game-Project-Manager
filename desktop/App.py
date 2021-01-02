from src.controllers.defineProject import *
from src.controllers.getProject import *
from src.controllers.alterProject import *

from view.widgetConfigs import *
from view.uiSettings import Layout, Header, Form, Menu

from tkinter import * 

class Application:
    def __init__(self, master=None):
        self.font = ('Verdana', '8')
        
        # Containers configs
        self.container1 = Frame(master)
        self.container2 = Frame(master)
        self.container3 = Frame(master)
        self.container4 = Frame(master)
        self.container5 = Frame(master)
        self.container6 = Frame(master)
        self.container7 = Frame(master)
        self.container8 = Frame(master)
        self.container9 = Frame(master)
        
        containers = [
            self.container1,
            self.container2,
            self.container3,
            self.container4,
            self.container5,
            self.container6,
            self.container7,
            self.container8,
            self.container9,
        ]
        
        Layout(containers)
        
        ##########
        # Header #
        ##########
        
        self.titulo = Label(self.container1, text='Informe os dados', font='Arial')
        self.titulo['font'] = ('Calibri', '9', 'bold')
        self.titulo.pack()
        
        self.lblidproject = Label(self.container2, text='ID Projeto:')
        
        self.txtidproject = Entry(self.container2)
        
        self.btnBuscar = Button(self.container2, text='Buscar')
        
        Header(
            self.lblidproject, 
            self.txtidproject, 
            self.btnBuscar, self.searchProject
        )
        
        ########
        # Form #
        ########
        
        self.lbldescription = Label(self.container3, text='Resumo')
        
        self.txtdescription = Entry(self.container3)
        
        self.lblobjective = Label(self.container4, text='Objetivo')
        
        self.txtobjective = Entry(self.container4)
        
        self.lblhistory = Label(self.container5, text='História')
        
        self.txthistory = Entry(self.container5)
        
        self.lblassets = Label(self.container6, text='Assets Fundamentais')
        
        self.txtassets = Entry(self.container6)
        
        self.lblanimations = Label(self.container7, text='Animações/cinemáticas')
        
        self.txtanimations = Entry(self.container7)
        
        self.lbllevels = Label(self.container3, text='Níveis Fundamentais', font=self.font)
        
        self.txtlevels = Entry(self.container3)
        
        self.lblnetwork = Label(self.container4, text='Baseado em rede?', font=self.font)
        
        self.txtnetwork = Entry(self.container4)
        
        self.lblaudio = Label(self.container5, text='Música')
        
        self.txtaudio = Entry(self.container5)
        
        self.lblmaingameplay = Label(self.container6, text='Jogabilidade Principal', font=self.font)
        
        self.txtmaingameplay = Entry(self.container6)
        
        self.lblsecgameplay = Label(self.container7, text='Mecânicas Secundárias')
        
        self.txtsecgameplay = Entry(self.container7)
        
        self.formLabels = [
                self.lbldescription,
                self.lblobjective,
                self.lblhistory,
                self.lblassets,
                self.lblanimations,
                self.lbllevels,
                self.lblnetwork,
                self.lblaudio,
                self.lblmaingameplay,
                self.lblsecgameplay
                
            ]
        
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
        
        Form(self.formLabels, self.formInputs)
        
        ########
        # Menu #
        ########
        
        self.btnCriar = Button(self.container8,text='Criar')
        # configButton(
            # self.btnCriar,
            # self.newProject
        # )
        
        self.btnAlterar = Button(self.container8, text='Alterar')
        # configButton(
            # self.btnAlterar,
            # self.changeProject 
        # )
        
        self.btnDeletar = Button(self.container8, text='Deletar')
        # configButton(
            # self.btnDeletar,
            # self.excludeProject
        # )
        
        self.options = [
            self.btnCriar, 
            self.btnAlterar, 
            self.btnDeletar
        ]
        
        Menu(self.options)
        
        # Menu([
            # {
                # 'button':self.btnCriar, 
                # 'command':self.newProject
            # },
            # {
                # 'button':self.btnAlterar,
                # 'command':self.changeProject,
            # },
            # {
                # 'button':self.btnDeletar, 
                # 'command':self.excludeProject
            # }
        # ])
        
        self.lblmsg = Label(self.container9, text='', font=self.font)
        self.lblmsg.pack()
    
    ###########
    # Handles #
    ###########
    
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
            
    def excludeProject(self):
        self.lblmsg['text'] = deleteGameProject(self.txtidproject.get())
        
        for t in self.formInputs:
            t.delete(0, END)
    
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