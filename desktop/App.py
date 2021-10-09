from src.controllers.defineProject import *
from src.controllers.getProject import *
from src.controllers.alterProject import *

# from view.wgtsettings import *
# from view.layoutsettings import Layout, Header, Form

import remi.gui as gui
from remi import start, App


class Application(App):
    def __init__(self, *args):
        super(Application, self).__init__(*args)

    def main(self):

        # the margin 0px auto centers the main container
        verticalContainer = gui.Container(width=1040, margin='170px auto',
        style={
            'display': 'block',
            'overflow': 'hidden',
            'border-radius': '20px',
            'padding': '20px'
            }
        )

        horizontalContainer = gui.Container(width='100%', layout_orientation=gui.Container.LAYOUT_HORIZONTAL, margin='0px',
        style={
            'display': 'block',
            'overflow': 'auto'
            }
        )

        ##########
        # Header #
        ##########

        self.lbTitle = gui.Label(text='Game Project Manager',
        style={
            'text-align': 'center',
            'margin': '20px 0',
            'font-size': '20px'
            }
        )

        ########
        # Menu #
        ########

        menu = gui.Menu(width='100%', height='30px')

        m1 = gui.MenuItem('Criar', width=100, height=30,
                          style={'background': '#8E1DE0'})
        m2 = gui.MenuItem('Alterar', width=100, height=30)
        m3 = gui.MenuItem('Deletar', width=100, height=30)
        self.projectid = gui.TextInput(width=100, height=30, 
        style={
            'color': 'black',
            }
        )
        
        self.m5 = gui.MenuItem('Buscar', width=100, height=30)
        self.m5.onclick.do(self.searchProject())

        menu.append([m1, m2, m3, self.projectid, self.m5])

        menubar = gui.MenuBar(width='100%', height='30px')

        menubar.append(menu)

        ########
        # Form #
        ########

        self.txtDescription = gui.TextInput(style={
            'padding': '10px',
            'color': '#580494',
        })
        self.txtDescription.set_text('Resumo')
        
        self.txtObjective = gui.TextInput()
        self.txtStrongs = gui.TextInput()
        self.txtWeaks = gui.TextInput()
        self.txtOportunities = gui.TextInput()
        self.txtThreads = gui.TextInput()
        self.txtHistory = gui.TextInput()
        self.txtAssets = gui.TextInput()
        self.txtAnimations = gui.TextInput()
        self.txtLevels = gui.TextInput()
        self.txtNetwork = gui.TextInput()
        self.txtAudio = gui.TextInput()
        self.txtMainGameplay = gui.TextInput()
        self.txtSecGameplay = gui.TextInput()
        self.txtColors1 = gui.TextInput()
        self.txtColors2 = gui.TextInput()
        self.txtSessionTime = gui.TextInput()

        self.formInputs = [
            self.txtDescription,
            self.txtObjective,
            self.txtStrongs,
            self.txtWeaks,
            self.txtOportunities,
            self.txtThreads,
            self.txtHistory,
            self.txtAssets,
            self.txtAnimations,
            self.txtLevels,
            self.txtNetwork,
            self.txtAudio,
            self.txtMainGameplay,
            self.txtSecGameplay,
            self.txtColors1,
            self.txtColors2,
            self.txtSessionTime,
        ]

        horizontalContainer.append([self.inputs])

        verticalContainer.append([self.lbTitle, menubar, horizontalContainer])

        # returning the root widget
        return verticalContainer

    ############
    # Handlers #
    ############

    def newProject(self):
        project = {
            'description': self.txtDescription.get_text(),
            'objective': self.txtObjective.get_text(),
            'strongs': self.txtStrongs.get_text(),
            'weaks': self.txtWeaks.get_text(),
            'oportunities': self.txtOportunities.get_text(),
            'threads': self.txtThreads.get_text(),
            'history': self.txtHistory.get_text(),
            'assets': self.txtAssets.get_text(),
            'animations': self.txtAnimations.get_text(),
            'levels': self.txtLevels.get_text(),
            'network': self.txtNetwork.get_text(),
            'audio': self.txtAudio.get_text(),
            'main_gameplay': self.txtMainGameplay.get_text(),
            'sec_gameplay': self.txtSecGameplay.get_text(),
            'colors1': self.txtColors1.get_text(),
            'colors2': self.txtColors2.get_text(),
            'session_time': self.txtSessionTime.get_text(),
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

        self.lblmsg['text'] = updateGameProject(
            self.txtidproject.get(), project)

        for t in self.formInputs:
            t.delete(0, END)

    def excludeProject(self):
        self.lblmsg['text']=deleteGameProject(self.txtidproject.get())

        for t in self.formInputs:
            t.delete(0, END)

    def searchProject(self):
        result=getGameProject(self.projectid.get_value())
        
        if result != 0:
            self.lbTitle.set_text(f"{result['message']}")

            for i, t in enumerate(self.formInputs):
                t.set_text('')
                t.set_text(result['register'][i])

        self.lbTitle.set_text('Dados não encontrados')

        


start(Application)
