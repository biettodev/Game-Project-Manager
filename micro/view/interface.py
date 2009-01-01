##################################
# INTERFACE SETTINGS FOR DESKTOP #
##################################

# Int input validations function
def readInt(msg):
    while True:
        try:
            print()
            valor = int(input(msg))
        except (TypeError, ValueError):
            print('ERRO! Digite um número inteiro válido.')
            continue
        except KeyboardInterrupt:
            print('O usuário optou por não digitar esse valor.')
            continue
        else:
            return valor
            break

# Draw line			
def line(tam=42):
    return '-' * tam

# Show header with a title
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

# Confirm operation function
def confirm():
    while True:
        try:
            print('Deseja mesmo realizar essa operação?')
            opt = str(input('Digite: S[Sim] - N[Não]: ')).lower()
            if opt == 's':
                return True
            else:
                return False
        except (TypeError, ValueError):
            print('ERRO! Digite um número inteiro válido.')
            continue
        except KeyboardInterrupt:
            print('O usuário optou por não digitar esse valor.')
            continue        
        except:
            print('Houve um problema com essa operação!')