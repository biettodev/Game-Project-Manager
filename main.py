#############################
# FILE OF MAIN INTERACTIONS #
#############################

from controllers.gameProjectController import *
from desktop.interface import *

from time import sleep

while True:
    choice = menu(['Listar Documentos', 'Criar Novo Documento', 'Atualizar Dados de Documento', 'Deletar Documento de Jogo', 'Sair'])
    if choice == 1:
        getGameProject()
        
    elif choice == 2:
        header('NOVO PROJETO DE GAME')
        
        # Reading game informations
        project = {
            'description': str(input('Digite o Resumo: ')),
            'strongs': str(input('Pontos Fortes: ')),
            'weaks': str(input('Pontos Fracos: ')),
            'oportunities': str(input('Oportunidades: ')),
            'theads': str(input('Ameaças: ')),
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
        cod = int(input('Digite o Código do Documento que deseja Alterar: '))
        description = str(input('Altere as informações do Resumo: '))
        updateGameProject(cod, description)
        
    elif choice == 4:
        cod = int(input('Digite o Código do Documento que deseja Deletar: '))
        deleteGameProject(cod)
    elif choice == 5:
        print('Saindo do sistema...Até logo!')
        break
    else:
        print('ERRO! Tente novamente. Digite um número válido!')
    sleep(1)
