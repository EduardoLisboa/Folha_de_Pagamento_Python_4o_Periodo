from empregado import Empregado
from venda import Venda
from cartãoponto import CartãoPonto
from taxaserviço import TaxaDeServiço
from datetime import date, timedelta, datetime

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""                          FUNÇÕES GERAIS                          """
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Dicionário para a função 'mostrar_taxas_serviço()'
meses = {1 : 'Janeiro', 2 : 'Fevereiro', 3 : 'Março',
        4 : 'Abril', 5 : 'Maio', 6 : 'Junho',
        7 : 'Julho', 8 : 'Agosto', 9 : 'Setembro',
        10 : 'Outubro', 11 : 'Novembro', 12 : 'Dezembro'}


def menu_principal():
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


def checar_ano_bissexto(data):
    return True if data.year % 4 == 0 and data.year % 100 != 0 or data.year % 400 == 0 else False


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""                            EMPREGADOS                            """
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def menu_empregado():
    print("""\n-=-=- FUNCIONÁRIOS -=-=-
1 - Adicionar funcionário
2 - Remover funcionário
3 - Editar funcionário
4 - Mostrar empregados
5 - Retornar
>> """, end='')


def localizar_empregado():
    id_func = int(input('Insira o ID do funcionário: '))
    for func in Empregado.empregados:
        if func.id_empregado == id_func:
            print('\nFuncionário localizado!')
            return func


def mostrar_empregados():
    print('\n-=-=- EMPREGADOS -=-=-', end='')
    for empregado in Empregado.empregados:
        if empregado.ativo:
            print(f'\nNome: {empregado.nome}')
            print(f'ID: {empregado.id_empregado}')
            print('Pertence a sindicato? ', end='')
            print(f'Sim' if empregado.sindicato else 'Não')
            if empregado.sindicato:
                print(f'ID Sindicato: {empregado.id_sindicato}')
            print(f'Prazo de pagamento: {Empregado.prazo_pagamento[empregado.p_pagamento]}')
            print(f'Forma de pagamento: {Empregado.forma_pagamento[empregado.f_pagamento]}')
            print(f'Próximo pagamento: {empregado.proximo_pagamento}')


def adicionar_empregado():
    print('\n-=-=- ADICIONAR -=-=-')
    novo_empregado = Empregado()
    novo_empregado.ativo = True
    novo_empregado.id_empregado = Empregado.id_empregado + 1
    novo_empregado.nome = str(input('Nome: ')).strip().title()
    novo_empregado.endereço = str(input('Endereço: ')).strip().title()
    tipo = int(input("""Tipo de empregado
1 - Horário
2 - Assalariado
3 - Comissionado
>> """))
    novo_empregado.t_empregado = tipo - 1
    if tipo == 1 or tipo == 2:
        novo_empregado.salario = float(input('Salário: R$'))
    elif tipo == 3:
        novo_empregado.comissao = float(input('Comissão (sem o sinal de %): '))
    
    sindicato = str(input('Pertence a sindicato? (s/n) ')).lower().strip()[0]
    if sindicato == 's':
        novo_empregado.sindicato = True
        novo_empregado.taxa = float(input('Taxa do sindicato: R$'))
        novo_empregado.id_sindicato = Empregado.id_sindicato + 1
        Empregado.id_sindicato += 1
    else:
        novo_empregado.sindicato = False
    prazo_pagamento = int(input("""Prazo de pagamento
1 - Semanal
2 - Mensal
3 - Quinzenal
>> """))
    novo_empregado.p_pagamento = prazo_pagamento - 1
    forma_pagamento = int(input("""Forma de pagamento
1 - Cheque correios
2 - Cheque mãos
3 - Depósito bancário
>> """))
    novo_empregado.f_pagamento = forma_pagamento - 1
    data_hoje = date.today()
    if prazo_pagamento == 1:
        delta = timedelta(days = 7)
    elif prazo_pagamento == 2:
        if data_hoje.month in [1, 3, 5, 7, 8, 10, 12]:
            delta = timedelta(days = 31)
        elif data_hoje.month == 2:
            if checar_ano_bissexto(data_hoje):
                delta = timedelta(days = 29)
            else:
                delta = timedelta(days = 28)
        else:
            delta = timedelta(days = 30)
    elif prazo_pagamento == 3:
        delta = timedelta(days = 15)
    data_hoje += delta
    novo_empregado.proximo_pagamento = data_hoje.strftime('%d/%m/%Y')

    Empregado.empregados.append(novo_empregado)
    Empregado.id_empregado += 1
    print('\nEmpregado cadastrado com sucesso!')


def remover_empregado():
    while True:
        print('\n-=-=- REMOVER -=-=-')
        aux_func = localizar_empregado()
        print(f'\nNome: {aux_func.nome}\n')
        confirmação = str(input('Confirmar remoção do funcionário? (s/n) ')).lower().strip()[0]
        if confirmação == 's':
            aux_func.ativo = False
            for venda in Venda.vendas:
                if venda.id_empregado == aux_func.id_empregado:
                    venda.ativo = False
            for taxa in TaxaDeServiço.taxas:
                if taxa.id_empregado == aux_func.id_empregado:
                    taxa.ativo = False
            break


def editar_empregado():
    while True:
        print('\n-=-=- EDITAR -=-=-')
        aux_func = localizar_empregado()

        print(f'\nNome: {aux_func.nome}')
        print(f'Endereço: {aux_func.endereço}')
        print(f'Tipo de empregado: {Empregado.tipo_empregado[aux_func.t_empregado]}')
        print('Sindicato: ', end='')
        print(f'Sim' if aux_func.sindicato else 'Não')
        print(f'Prazo de pagamento: {Empregado.prazo_pagamento[aux_func.p_pagamento]}')
        print(f'Forma de pagamento: {Empregado.forma_pagamento[aux_func.f_pagamento]}\n')

        editar = str(input("""1 - Nome
2 - Endereço
3 - Tipo de empregado
4 - Sindicato
5 - Tipo de pagamento
6 - Forma de pagamento
7 - Retornar
>> """))
        if editar.isnumeric() and 0 < int(editar) < 8: break
    editar = int(editar)
    if editar == 1:
        aux_func.nome = str(input('\nNovo nome: ')).strip().title()
    elif editar == 2:
        aux_func.endereço = str(input('\nNovo endereço: ')).strip().title()
    elif editar == 3:
        tipo = int(input("""\nTipo de empregado
1 - Horário
2 - Assalariado
3 - Comissionado
>> """))
        aux_func.tipo = tipo - 1
        aux_func.salario = float(input('Salário: R$'))
        if tipo == 3:
            aux_func.comissao = float(input('Comissão (sem o sinal de %): '))
    elif editar == 4:
        sindicato = str(input('Pertence a sindicato? (s/n) ')).lower().strip()[0]
        if sindicato == 's':
            aux_func.sindicato = True
            aux_func.taxa = float(input('Taxa do sindicato: R$'))
            aux_func.id_sindicato = Empregado.id_sindicato + 1
            Empregado.id_sindicato += 1
        else:
            aux_func.sindicato = False
    elif editar == 5:
        prazo_pagamento = int(input("""Prazo de pagamento
1 - Semanal
2 - Mensal
3 - Quinzenal
>> """))
        aux_func.p_pagamento = prazo_pagamento - 1
        data_hoje = date.today()
        if prazo_pagamento == 1:
            delta = timedelta(days = 7)
        elif prazo_pagamento == 2:
            if data_hoje.month in [1, 3, 5, 7, 8, 10, 12]:
                delta = timedelta(days = 31)
            elif data_hoje.month == 2:
                if checar_ano_bissexto(data_hoje):
                    delta = timedelta(days = 29)
                else:
                    delta = timedelta(days = 28)
            else:
                delta = timedelta(days = 30)
        elif prazo_pagamento == 3:
            delta = timedelta(days = 15)
        data_hoje += delta
        aux_func.proximo_pagamento = data_hoje.strftime('%d/%m/%Y')
    elif editar == 6:
        forma_pagamento = int(input("""Forma de pagamento
1 - Cheque correios
2 - Cheque mãos
3 - Depósito bancário
>> """))
        aux_func.f_pagamento = forma_pagamento - 1
    elif editar == 7:
        return
    
    continuar = str(input('Deseja editar algo mais? (s/n) ')).lower().strip()[0]
    if continuar == 's':
        editar_empregado()
        return
    else:
        return


def func_empregado():
    while True:
        menu_empregado()
        while True:
            opção = str(input())
            if opção.isnumeric() and 0 < int(opção) < 6: break
            else: print('\nOpção inválida!\n')

        opção = int(opção)

        if opção == 1: adicionar_empregado()
        elif opção == 2: remover_empregado()
        elif opção == 3: editar_empregado()
        elif opção == 4: mostrar_empregados()
        elif opção == 5: return


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""                           CARTÃO PONTO                           """
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def menu_cartão_ponto():
    print("""\n-=-=- CARTÃO PONTO -=-=-
1 - Entrada
2 - Saída
3 - Exibir pontos
4 - Retornar
>> """, end='')


def mostrar_pontos():
    print('\n-=-=- CARTÕES PONTO -=-=-')
    for ponto in CartãoPonto.pontos:
        print(f'\nNome: {Empregado.empregados[ponto.id_empregado - 1].nome}')
        print(f'ID: {ponto.id_empregado}')
        print(f'Data: {ponto.data}')
        print(f'Entrada: {ponto.entrada}')
        print('Funcionário ainda em serviço' if not ponto.entrando else f'Saída: {ponto.saída}')


def func_cartão_ponto():
    while True:
        menu_cartão_ponto()
        while True:
            opção = str(input())
            if opção.isnumeric() and 0 < int(opção) < 5: break
            else: print('\nOpção inválida!\n')

        opção = int(opção)

        if opção == 1: lançar_cartão_ponto(1)
        elif opção == 2: lançar_cartão_ponto(0)
        elif opção == 3: mostrar_pontos()
        elif opção == 4: return


def localizar_ponto(data, id_emp):
    for ponto in CartãoPonto.pontos:
        if data == ponto.data and ponto.id_empregado == id_emp and not ponto.entrando:
            return ponto


def lançar_cartão_ponto(opc):
    if opc == 1:
        ponto = CartãoPonto()

        aux_func = localizar_empregado()
        print(f'\nNome: {aux_func.nome}\n')
        
        hora = datetime.now()
        hora = hora.strftime('%H:%M:%S')

        ponto.entrada = hora
        ponto.entrando = False
        data_ponto = date.today().strftime('%d/%m/%Y')
        ponto.data = data_ponto
        ponto.id_empregado = aux_func.id_empregado

        CartãoPonto.pontos.append(ponto)
        print('Ponto de entrada OK!\n')

    elif opc == 0:
        aux_func = localizar_empregado()
        print(f'\nNome: {aux_func.nome}\n')

        data = date.today().strftime('%d/%m/%Y')
        hora = datetime.now()
        hora = hora.strftime('%H:%M:%S')
        ponto = localizar_ponto(data, aux_func.id_empregado)
        ponto.saída = hora
        ponto.entrando = True
        print('Ponto de saída OK!\n')


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""                              VENDAS                              """
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def menu_vendas():
    print("""\n-=-=- VENDAS -=-=-
1 - Registrar venda
2 - Mostrar vendas efetuadas
3 - Retornar
>> """, end='')


def func_vendas():
    while True:
        menu_vendas()
        while True:
            opção = str(input())
            if opção.isnumeric() and 0 < int(opção) < 4: break
            else: print('\nOpção inválida!\n')
        opção = int(opção)

        if opção == 1: lançar_venda()
        elif opção == 2: mostrar_vendas()
        elif opção == 3: return


def mostrar_vendas():
    print('\n-=-=- VENDAS EFETUADAS -=-=-', end='')
    for venda in Venda.vendas:
        if venda.ativo:
            print(f'\nID Empregado: {venda.id_empregado}')
            print(f'Nome: {Empregado.empregados[venda.id_empregado - 1].nome}')
            print(f'Valor da venda: R${venda.valor:.2f}')
            print(f'Data da venda: {venda.data}')


def lançar_venda():
    print('\n-=-=- REGISTRAR VENDA -=-=-')
    venda = Venda()
    valor = float(input('Valor da venda: R$'))
    data_venda = date.today()
    print('Empregado responsável pela venda:')
    aux_func = localizar_empregado()
    venda.valor = valor
    venda.ativo = True
    venda.data = data_venda.strftime('%d/%m/%Y')
    venda.id_empregado = aux_func.id_empregado

    Venda.vendas.append(venda)


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""                        FOLHA DE PAGAMENTO                        """
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def atualizar_data(emp, data_hoje):
    prazo = emp.p_pagamento
    if prazo == 0:
        delta = timedelta(days = 7)
    elif prazo == 1:
        if data_hoje.month in [1, 3, 5, 7, 8, 10, 12]:
            delta = timedelta(days = 31)
        elif data_hoje.month == 2:
            if checar_ano_bissexto(data_hoje):
                delta = timedelta(days = 29)
            else:
                delta = timedelta(days = 28)
        else:
            delta = timedelta(days = 30)
    elif prazo == 2:
        delta = timedelta(days = 15)
    data_hoje += delta
    aux_func.proximo_pagamento = data_hoje.strftime('%d/%m/%Y')


def calcular_salario(emp):
    if emp.t_empregado == 0:
        salario = emp.salario * 40
        if emp.p_pagamento == 1: salario *= 4
        elif emp.p_pagamento == 2: salario *= 2
    elif emp.t_empregado == 1:
        salario = emp.salario
    elif emp.t_empregado == 2:
        salario = 0
        for venda in Venda.vendas:
            if venda.id_empregado == emp.id_empregado and venda.data > emp.ultimo_pagamento:
                salario += ((emp.comissao) / 100) * venda.valor
    return salario


def rodar_folha():
    cont = False
    hoje = date.today().strftime('%d/%m/%Y')
    for empregado in Empregado.empregados:
        if empregado.proximo_pagamento == hoje:
            cont = True
            print(f'Nome: {empregado.nome}')
            empregado.ultimo_pagamento = empregado.proximo_pagamento
            empregado.proximo_pagamento = atualizar_data(empregado, date.today())
            print(f'Salário: R${calcular_salario(empregado):.2f}')
    if not cont:
        print('\nNenhum funcionário para receber hoje!\n')


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""                         TAXAS DE SERVIÇO                         """
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def menu_taxas_serviço():
    print("""\n -=-=- TAXAS DE SERVIÇO -=-=-
1 - Lançar Taxa de Serviço
2 - Exibir Taxas
3 - Retornar
>> """, end='')


def func_taxas_serviço():
    while True:
        menu_taxas_serviço()
        while True:
            opção = str(input())
            if opção.isnumeric() and 0 < int(opção) < 4: break
            else: print('\nOpção inválida!\n')
        opção = int(opção)

        if opção == 1: lançar_taxa_serviço()
        elif opção == 2: mostrar_taxas_serviço()
        elif opção == 3: return


def lançar_taxa_serviço():
    taxa = TaxaDeServiço()
    taxa.valor = float(input('Valor da taxa: R$'))
    print('Funcionário associado à taxa:')
    aux_func = localizar_empregado()
    print(f'\nNome: {aux_func.nome}')
    taxa.id_empregado = aux_func.id_empregado
    taxa.mes = date.today().month
    taxa.ativo = True

    TaxaDeServiço.taxas.append(taxa)
    print('Taxa associada com sucesso!')


def mostrar_taxas_serviço():
    print('\n-=-=- TAXAS REGISTRADAS -=-=-', end='')
    for taxa in TaxaDeServiço.taxas:
        if taxa.ativo:
            print(f'\nValor da taxa: {taxa.valor:.2f}')
            print(f'Nome: {Empregado.empregados[taxa.id_empregado - 1].nome}')
            print(f'ID: {taxa.id_empregado}')
            print(f'Mês da taxa: {meses[taxa.mes]}')


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""                       AGENDAS DE PAGAMENTO                       """
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def listar_agendas():
    print('\n-=-=- AGENDAS DE PAGAMENTOS -=-=-', end='')
    for empregado in Empregado.empregados:
        if empregado.ativo:
            print(f'\nNome: {empregado.nome}')
            print(f'ID: {empregado.id_empregado}')
            print(f'Forma de pagamento: {Empregado.forma_pagamento[empregado.f_pagamento]}')
            print(f'Prazo de pagamento: {Empregado.prazo_pagamento[empregado.p_pagamento]}')
            print(f'Próximo pagamento: {empregado.proximo_pagamento}')


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""                           UNDO E REDO                            """
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def undo():
    pass


def redo():
    pass


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""                        PROGRAMA PRINCIPAL                        """
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
while True:
    menu_principal()
    while True:
        opção = str(input())
        if opção.isnumeric() and 0 < int(opção) < 10:
            break
        else:
            print('\nOpção inválida!\n')
            break
    
    opção = int(opção)

    if opção == 1: func_empregado()
    elif opção == 2: rodar_folha()
    elif opção == 3: func_cartão_ponto()
    elif opção == 4: func_vendas()
    elif opção == 5: func_taxas_serviço()
    elif opção == 6: listar_agendas()
    elif opção == 7: undo()
    elif opção == 8: redo()
    elif opção == 9:
        print('\nAté logo!\n')
        exit()
