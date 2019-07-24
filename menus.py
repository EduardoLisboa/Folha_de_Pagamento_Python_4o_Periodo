from os import system

def menu_principal():
    system('clear')
    print("""\n-=-=- MENU PRINCIPAL -=-=-
1 - Funcionários
2 - Rodar Folha de Pagamentos
3 - Lançar Cartão de Ponto
4 - Lançar Venda
5 - Lançar Taxa de Serviço
6 - Listar Agendas de Pagamentos
7 - Undo
8 - Redo
9 - Sair
>> """, end='')


def menu_empregado():
    system('clear')
    print("""\n-=-=- FUNCIONÁRIOS -=-=-
1 - Adicionar funcionário
2 - Remover funcionário
3 - Editar funcionário
4 - Mostrar empregados
5 - Retornar
>> """, end='')


def menu_cartão_ponto():
    system('clear')
    print("""\n-=-=- CARTÃO PONTO -=-=-
1 - Entrada
2 - Saída
3 - Exibir pontos
4 - Retornar
>> """, end='')


def menu_vendas():
    system('clear')
    print("""\n-=-=- VENDAS -=-=-
1 - Registrar venda
2 - Mostrar vendas efetuadas
3 - Retornar
>> """, end='')


def menu_taxas_serviço():
    system('clear')
    print("""\n -=-=- TAXAS DE SERVIÇO -=-=-
1 - Lançar Taxa de Serviço
2 - Exibir Taxas
3 - Retornar
>> """, end='')
