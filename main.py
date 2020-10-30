#############################
# FILE OF MAIN INTERACTIONS #
#############################

from src.controllers.defineProject import *
from src.controllers.getProject import *
from src.controllers.alterProject import *

from desktop.interface import *

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
            'description': str(input('Digite o Resumo: ')),
            'strongs': str(input('Pontos Fortes: ')),
            'weaks': str(input('Pontos Fracos: ')),
            'oportunities': str(input('Oportunidades: ')),
            'threads': str(input('Ameaças: ')),
            'objective': str(input('Objetivo/impacto: ')),
            'history': str(input('Baseado em história? ')),
            'assets': str(input('Assets Fundamentais: ')),
            'animations': str(input('Animações/cinemáticas: ')),
            'levels': str(input('Níveis Fundamentais: ')),
            'network': str(input('Funcionalidades de Rede? ')),
            'audio': str(input('Sonoplastia: ')),
            'main_gameplay': str(input('Jogabilidade Principal: ')),
            'sec_gameplay': str(input('Mecânicas Secundárias: ')),
            'interfaces': str(input('Interfaces: ')),
            'colors1': str(input('Paleta 1: ')),
            'colors2': str(input('Paleta 2: ')),
            'session_time': str(input('Tempo Médio de Sessão: '))
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
                    
                    updatedInfo = str(input('Mudar para: '))
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
