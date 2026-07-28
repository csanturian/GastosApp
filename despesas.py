from datetime import datetime

despesas = []

def calcular_total():
     return sum(valor for nome, valor in despesas)

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
    total = calcular_total()
    print(f'O total gasto foi: R${total}')

def fechar_mes():
    global despesas

    if len(despesas) == 0:
                print('Nenhuma despesa foi adicionada no mês.')
                return
    
    while True:
        confirmar = input('Deseja fechar a lista do mês? (s/n): ').lower()
        if confirmar == 's':
            total = calcular_total()

            print('\n--- FECHAMENTO DO MÊS ---')
            print(f'Total gasto no mês: R${total}')

            data_atual = datetime.now().strftime('%m_%Y')
            nome_arquivo = f'relatorio_{data_atual}.txt'
            with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
                 arquivo.write('----- Relatório do seu mês -----\n')
                 for nome, valor in despesas:
                      arquivo.write(f'{nome} - R${valor}\n')
                 arquivo.write(f'\nTotal gasto no mês: R${total}\n')

            despesas = []

            print('Novo mês iniciado! Despesas zeradas.')
            break
        
        elif confirmar == 'n':
            print('Fechamento Cancelado! Suas despesas foram mantidas.')
            break
        else:
            print('Opção Inválida! Digite apenas "s" ou "n".')