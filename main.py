from controllers.gameProjectController import *
from view.interface import *
from time import sleep

while True:
    choice = menu(['Listar Documentos', 'Criar Novo Documento', 'Atualizar Dados de Documento', 'Deletar Documento de Jogo', 'Sair'])
    if choice == 1:
        getGameProject()
    elif choice == 2:
        header('NOVO PROJETO DE GAME')
        description = str(input('Digite o Resumo: '))
        createGameProject(description)
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
