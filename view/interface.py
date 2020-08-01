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
			
def line(tam=42):
    return '-' * tam

def header(txt):
    print(line())
    print(f'{txt.center(42)}')
    print(line())

def menu(lista):
    header('MENU PRINCIPAL')

    for p, v in enumerate(lista):
        print(f'Opção {p+1} - {v}')
    opcao = readInt('Sua opção: ')

    return opcao