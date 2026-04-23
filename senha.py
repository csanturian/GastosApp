import re

print('---DESPESAS DO MÊS---')


def validar_usuario(usuario):
        if len(usuario) > 15: 
              return('Nome de usuario longo demais!')
        if not re.search ('[a-z]', usuario) : 
              return 'Falta letra minúscula'
        if not re.search ('[A-Z]', usuario) : 
              return('Falta letra maiúscula!')
        return 'OK'

def validar_senha(senha_informada):
        if len(senha_informada) < 8: 
              return('Senha Curta!')
        if not re.search ('[a-z]', senha_informada) : 
              return 'Falta letra minúscula'
        if not re.search ('[A-Z]', senha_informada) : 
              return('Falta letra maiúscula!')
        if not re.search ('[0-9]', senha_informada) : 
              return('Falta número em sua senha!')
        return 'OK'
    
def cadastrar():
        usuario = input('Crie um usuário: ')
        senha_informada = input('Crie uma senha(minimo 8 caracteres): ')
        
        if validar_usuario(usuario) != 'OK':
            print(validar_usuario(usuario))
            return None, None
        
        if validar_senha(senha_informada) != 'OK':
            print(validar_senha(senha_informada))
            return None, None
        
        print('Cadastro feito com sucesso!')
        return usuario, senha_informada