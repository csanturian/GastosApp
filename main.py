from senha import cadastrar
from despesas import adicionar_despesa, listar_despesas, total_despesas, fechar_mes

print('Vamos agora entrar em sua conta!')

usuario_cadastrado, senha_cadastrada = cadastrar()

if usuario_cadastrado is None:
    print('Erro no cadastro. Encerrando...')
else:
    print('---LOGIN---')

    tentativas = 0
    login_correto = False
    while tentativas < 3 and login_correto == False:
        nome_usuario = input('Digite seu nome de usuário: ')
        senha_usuario = input('Digite sua senha: ')

        if nome_usuario == usuario_cadastrado and senha_usuario == senha_cadastrada:
            login_correto = True
            print('LOGIN FEITO COM SUCESSO!')
            print('\n--- Bem vindo ao sistema de despesas ---')
            while True:
                print('\n--- MENU PRINCIPAL---')
                print('1. Adicionar Despesa')
                print('2. Listar Despesas')
                print('3. Ver total')
                print('4. Fechar Lista do Mês')
                print('0. Sair')

                opcao = input('Digite a opção desejada: ')
            
                if opcao == '1':
                    adicionar_despesa()
                elif opcao == '2':
                    listar_despesas()
                elif opcao == '3':
                    total_despesas()
                elif opcao == '4':
                    fechar_mes()
                elif opcao == '0':
                    print('Saindo...')
                    break
                else:
                    print('Opção Inválida!')

        else:
            tentativas += 1
            print(f'Usuário ou senha incorretos! Tentativas restantes: {3 - tentativas}')

    if login_correto == False:
        print('Números de tentativas excedido. Encerrando...')