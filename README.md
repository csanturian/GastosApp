# GastosApp

O **GastosApp** é um sistema de console em Python para controle de gastos financeiros mensais. Com ele, é possível se cadastrar, fazer login, registrar despesas por categoria e, ao final do mês, gerar um relatório em `.txt` com o total gasto e um resumo por categoria.

## Funcionalidades

- **Cadastro de usuário** com validação de nome de usuário e senha (exige letra maiúscula, minúscula, número e tamanho mínimo)
- **Login** com limite de tentativas (2 tentativas após o primeiro erro)
- **Adicionar despesas**, informando nome, valor e categoria
- **Listar despesas** adicionadas no mês
- **Ver total** gasto no mês
- **Fechar o mês**, gerando automaticamente um relatório em `.txt` contendo:
  - Lista completa das despesas do mês
  - Total geral gasto
  - Resumo por categoria (subtotal de cada categoria)
- Após o fechamento, a lista de despesas é zerada para o início de um novo mês

## Como rodar

Pré-requisito: ter o **Python 3** instalado.

1. Clone o repositório:
   ```bash
   git clone https://github.com/csanturian/GastosApp.git
   ```
2. Entre na pasta do projeto:
   ```bash
   cd GastosApp
   ```
3. Execute o programa:
   ```bash
   python main.py
   ```

Não há dependências externas — o projeto usa apenas bibliotecas padrão do Python (`re`, `datetime`).

## Estrutura do projeto

```
GastosApp/
├── main.py       # Ponto de entrada: login e menu principal
├── despesas.py   # Lógica de despesas (adicionar, listar, total, fechar mês)
├── senha.py      # Cadastro e validação de usuário/senha
└── .gitignore
```

## Exemplo de relatório gerado

Ao fechar o mês, um arquivo `relatorio_MM_AAAA.txt` é criado na pasta do projeto, com um conteúdo parecido com:

```
----- Relatório do seu mês -----
Mercado - R$150.0 - Alimentação
Uber - R$20.0 - Transporte
Padaria - R$15.0 - Alimentação

Total gasto no mês: R$185.0

-----
RESUMO POR CATEGORIA-----
Alimentação: R$165.0
Transporte: R$20.0
```

## Tecnologias e conceitos praticados

- Python 3
- Funções
- Estruturas de dados (listas e dicionários)
- Estruturas condicionais e de repetição
- Validação de dados
- Manipulação de arquivos `.txt`
- Expressões regulares (`re`)
- Manipulação de datas (`datetime`)

## Autor

Desenvolvido por [csanturian](https://github.com/csanturian) como projeto de estudo em Python.
