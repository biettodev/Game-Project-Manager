#############################
# FILE OF MAIN INTERACTIONS #
#############################

from src.controllers.defineProject import *
from src.controllers.getProject import *
from src.controllers.alterProject import *

from view.interface import *

from time import sleep

gameDescriptions = [
    'Resumo',
    'Pontos Fortes',
    'Pontos Fracos',
    'Oportunidades',
    'Ameaças',
    'Objetivo/impacto',
    'Baseado em história',
    'Assetes Fundamentais',
    'Animações/cinemáticas',
    'Níveis Fundamentais',
    'Funcionalidades de Rede',
    'Sonoplastia',
    'Jogabilidade Principal',
    'Mecânicas Secundárias',
    'Interfaces',
    'Paleta1',
    'Paleta2',
    'Tempo Médio de Sessão'
]

while True:
    choice = menu(['Listar Documentos', 'Criar Novo Documento', 'Atualizar Dados de Documento', 'Deletar Documento de Jogo', 'Sair'])
    if choice == 1:
        getGameProjects()
        
    elif choice == 2:
        header('NOVO PROJETO DE GAME')
        
        # Reading game informations
        project = {
            'description': str(input('Digite o Resumo: ')).upper(),
            'strongs': str(input('Pontos Fortes: ')).upper(),
            'weaks': str(input('Pontos Fracos: ')).upper(),
            'opportunities': str(input('Oportunidades: ')).upper(),
            'threads': str(input('Ameaças: ')).upper(),
            'objective': str(input('Objetivo/impacto: ')).upper(),
            'history': str(input('Baseado em história? ')).upper(),
            'assets': str(input('Assets Fundamentais: ')).upper(),
            'animations': str(input('Animações/cinemáticas: ')).upper(),
            'levels': str(input('Níveis Fundamentais: ')).upper(),
            'network': str(input('Funcionalidades de Rede? ')).upper(),
            'audio': str(input('Sonoplastia: ')).upper(),
            'main_gameplay': str(input('Jogabilidade Principal: ')).upper(),
            'sec_gameplay': str(input('Mecânicas Secundárias: ')).upper(),
            'interfaces': str(input('Interfaces: ')).upper(),
            'colors1': str(input('Paleta 1: ')).upper(),
            'colors2': str(input('Paleta 2: ')).upper(),
            'session_time': str(input('Tempo Médio de Sessão: ')).upper()
        }
        createGameProject(project)
        
    elif choice == 3:
        if confirm(): 
            cod = readInt('Digite o Código do Documento que deseja Alterar: ')
               
            gameInfos = getGameProject(cod)
            
            infosToUpdate = list()
            
            if gameInfos != None:
                for i in range(1, len(gameInfos)):
                    print(f'{i}. {gameDescriptions[i-1]}: {gameInfos[i]}')
                    
                    updatedInfo = str(input('Mudar para: ')).upper()
                    infosToUpdate.append(updatedInfo)
                    
                updateGameProject(cod, infosToUpdate)
            else:
                print('Nenhum Documento com esse Código foi encontrado!')
        else:          
            print('Operação cancelada.')
            
    elif choice == 4:
        if confirm():
            cod = readInt('Digite o Código do Documento que deseja Deletar: ')
            deleteGameProject(cod)
        else:          
            print('Operação cancelada.')
        
    elif choice == 5:
        print('Saindo do sistema...Até logo!')
        break
    else:
        print('ERRO! Tente novamente. Digite um número válido!')
    sleep(1)
