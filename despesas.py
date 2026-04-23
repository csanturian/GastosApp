despesas = []

def adicionar_despesa():
    nome = input('Qual o nome da despesa adicionada: ')
    valor = float(input('Qual o valor da despesa: '))

    despesas.append((nome, valor))
    print('Despesa Adicionada!')

def listar_despesas():
    if len(despesas) == 0:
        print('Nenhuma despesa adicionada!')
        return
    
    print('\n--- Suas Despesas ---')
    for nome, valor in despesas:
        print(f'{nome} - R${valor}')
        
def total_despesas():
    total = sum(valor for nome, valor in despesas)
    print(f'O total gasto foi: R${total}')

def fechar_mes():
    global despesas

    if len(despesas) == 0:
                print('Nenhuma despesa foi adicionada no mês.')
                return
    
    while True:
        confirmar = input('Deseja fechar a lista do mês? (s/n): ').lower()
        if confirmar == 's':
            total = sum(valor for nome, valor in despesas)

            print('\n--- FECHAMENTO DO MÊS ---')
            print(f'Total gasto no mês: R${total}')

            despesas = []

            print('Novo mês iniciado! Despesas zeradas.')
            break
        
        elif confirmar == 'n':
            print('Fechamento Cancelado! Suas despesas foram mantidas.')
            break
        else:
            print('Opção Inválida! Digite apenas "s" ou "n".')