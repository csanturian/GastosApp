from datetime import datetime

despesas = []

def calcular_total():
     return sum(valor for nome, valor, categoria in despesas)

def adicionar_despesa():
    nome = input('Qual o nome da despesa adicionada: ')
    valor = float(input('Qual o valor da despesa: '))
    categoria = input('Qual a categoria da despesa: ')

    despesas.append((nome, valor, categoria))
    print('Despesa Adicionada!')

def listar_despesas():
    if len(despesas) == 0:
        print('Nenhuma despesa adicionada!')
        return
    
    print('\n--- Suas Despesas ---')
    for nome, valor, categoria in despesas:
        print(f'{nome} - R${valor} - {categoria}')
        
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
                 subtotal_categoria = {}
                 for nome, valor, categoria in despesas:
                      if categoria in subtotal_categoria:
                           subtotal_categoria[categoria] = subtotal_categoria[categoria] + valor
                      else:
                           subtotal_categoria[categoria] = valor
                      arquivo.write(f'{nome} - R${valor} - {categoria}\n')
                 arquivo.write(f'\nTotal gasto no mês: R${total}\n')

                 arquivo.write('\n-----RESUMO POR CATEGORIA-----\n')
                 for categoria, valor in subtotal_categoria.items():
                        arquivo.write(f'{categoria}: R${valor}\n')
            despesas = []

            print('Novo mês iniciado! Despesas zeradas.')
            break
        
        elif confirmar == 'n':
            print('Fechamento Cancelado! Suas despesas foram mantidas.')
            break
        else:
            print('Opção Inválida! Digite apenas "s" ou "n".')