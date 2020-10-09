##################################
# INTERFACE SETTINGS FOR DESKTOP #
##################################

# Int input validations function
def readInt(msg):
    while True:
        try:
            valor = int(input(msg))
        except (TypeError, ValueError):
            print('ERRO! Digite um número inteiro válido.')
            continue
        except KeyboardInterrupt:
            print('O usuário optou por não digitar esse valor.')
            return 0
        else:
            return valor

# Draw line			
def line(tam=42):
    return '-' * tam

# Show header with section title
def header(txt):
    print(line())
    print(f'{txt.center(42)}')
    print(line())

# Menu settings
def menu(lista):
    header('MENU PRINCIPAL')

    for p, v in enumerate(lista):
        print(f'Opção {p+1} - {v}')
    opcao = readInt('Sua opção: ')

    return opcao