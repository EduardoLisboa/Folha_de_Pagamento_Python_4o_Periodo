from empregado import *
from venda import Venda
from cartãoponto import CartãoPonto
from taxaserviço import TaxaDeServiço
from menus import *
from entrada import func_entrada
from datetime import date, timedelta, datetime

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""                          FUNÇÕES GERAIS                          """
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def checar_ano_bissexto(data):
    return True if data.year % 4 == 0 and data.year % 100 != 0 or data.year % 400 == 0 else False


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""                            EMPREGADOS                            """
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def adicionar_empregado():
    print('\n-=-=- ADICIONAR -=-=-')
    ativo = True
    id_empregado = Empregado.id_empregado + 1
    Empregado.id_empregado += 1

    nome = func_entrada(str, 'Nome: ')
    endereço = func_entrada(str, 'Endereço: ')    
    sindicato = func_entrada(str, 'Pertence a sindicato? (s/n) ').lower().strip()[0]

    if sindicato == 's':
        sindicato = True
        taxa = func_entrada(float, 'Taxa do sindicato: R$')
        id_sindicato = Empregado.id_sindicato + 1
        id_sindicato += 1
    elif sindicato == 'n':
        sindicato = False
        id_sindicato = -1
        taxa = -1

    prazo_pagamento = func_entrada(int, """Prazo de pagamento
1 - Semanal
2 - Mensal
3 - Quinzenal
>> """, limite=True, lim_inf=1, lim_sup=3)
    prazo_pagamento -= 1

    forma_pagamento = func_entrada(int, """Forma de pagamento
1 - Cheque correios
2 - Cheque mãos
3 - Depósito bancário
>> """, limite=True, lim_inf=1, lim_sup=3)
    forma_pagamento -= 1

    dia_preferido = func_entrada(int, """Dia preferido para pagamento
2 - Segunda
3 - Terça
4 - Quarta
5 - Quinta
6 - Sexta
>> """, limite=True, lim_inf=2, lim_sup=6)

    data_hoje = date.today()
    if prazo_pagamento == 0:
        delta = timedelta(days = 7)
    elif prazo_pagamento == 1:
        if data_hoje.month in [1, 3, 5, 7, 8, 10, 12]:
            delta = timedelta(days = 31)
        elif data_hoje.month == 2:
            if checar_ano_bissexto(data_hoje):
                delta = timedelta(days = 29)
            else:
                delta = timedelta(days = 28)
        else:
            delta = timedelta(days = 30)
    elif prazo_pagamento == 2:
        delta = timedelta(days = 15)
    data_hoje += delta
    proximo_pagamento = data_hoje.strftime('%d/%m/%Y')

    tipo = func_entrada(int, """Tipo de empregado
1 - Horário
2 - Assalariado
3 - Comissionado
>> """, limite=True, lim_inf=1, lim_sup=3)

    tipo -= 1
    if tipo == 0:
        valor_hora = func_entrada(float, 'Valor da hora: R$')

        novo_empregado = Horario(id_empregado, nome, endereço, tipo, forma_pagamento, dia_preferido, ativo, sindicato, taxa, id_sindicato, '', proximo_pagamento, prazo_pagamento, valor_hora)

    elif tipo == 1:
        salario = func_entrada(float, 'Salário: R$')

        novo_empregado = Assalariado(id_empregado, nome, endereço, tipo, forma_pagamento, dia_preferido, ativo, sindicato, taxa, id_sindicato, '', proximo_pagamento, prazo_pagamento, salario)

    elif tipo == 2:
        salario = func_entrada(float, 'Salário: R$')
        comissao = func_entrada(float, 'Comissão (sem o sinal de %): ', limite=True, lim_inf=0.0, lim_sup=100.0)

        novo_empregado = Comissionado(id_empregado, nome, endereço, tipo, forma_pagamento, dia_preferido, ativo, sindicato, taxa, id_sindicato, '', proximo_pagamento, prazo_pagamento, salario, comissao)

    Empregado.empregados.append(novo_empregado)
    novo_empregado.duplicar()
    Transação.trns_ultima_undo.append(['Adicionar', novo_empregado.id_empregado])
    print('\nEmpregado cadastrado com sucesso!')
    input()


def remover_empregado():
    while True:
        print('\n-=-=- REMOVER -=-=-')
        aux_func = Empregado.localizar_empregado()
        print('\nFuncionário localizado!')
        print(f'\nNome: {aux_func.nome}\n')
        while True:
            confirmação = str(input('Confirmar remoção do funcionário? (s/n) ')).lower().strip()[0]
            if confirmação.isalpha() and confirmação in 'ns': break
            else: print('\nEntrada inválida!')
        if confirmação == 's':
            aux_func.ativo = False
            for venda in Venda.vendas:
                if venda.id_empregado == aux_func.id_empregado: venda.ativo = False
            for taxa in TaxaDeServiço.taxas:
                if taxa.id_empregado == aux_func.id_empregado: taxa.ativo = False
            Transação.trns_ultima_undo.append(['Remover', aux_func.id_empregado])
            print('\nFuncionário removido com sucesso!')
            break
        elif confirmação == 'n': return
    input()


def editar_empregado():
    while True:
        print('\n-=-=- EDITAR -=-=-')
        while True:
            aux_func = Empregado.localizar_empregado()
            if not aux_func:
                print('\nNão existe funcionário com esse ID!')
            else:
                print('\nFuncionário localizado!')
                break

        print(f'\nNome: {aux_func.nome}')
        print(f'Endereço: {aux_func.endereço}')
        print(f'Tipo de empregado: {Empregado.tipo_empregado[aux_func.t_empregado]}')
        print('Sindicato: ', end='')
        print(f'Sim' if aux_func.sindicato else 'Não')
        print(f'Prazo de pagamento: {Empregado.prazo_pagamento[aux_func.p_pagamento]}')
        print(f'Forma de pagamento: {Empregado.forma_pagamento[aux_func.f_pagamento]}\n')

        editar = func_entrada(int, """1 - Nome
2 - Endereço
3 - Tipo de empregado
4 - Sindicato
5 - Prazo de pagamento
6 - Forma de pagamento
7 - Retornar
>> """, limite=True, lim_inf=1, lim_sup=7)


        if editar == 1:
            novo_nome = func_entrada(str, 'Novo nome: ')
            aux_func.nome = novo_nome

        elif editar == 2:
            novo_endereço = func_entrada(str, 'Novo endereço: ')
            aux_func.endereço = novo_endereço

        elif editar == 3:
            novo_tipo = func_entrada(int, """\nTipo de empregado
1 - Horário
2 - Assalariado
3 - Comissionado
>> """, limite=True, lim_inf=1, lim_sup=3)
            

            aux_func.t_empregado = novo_tipo - 1
            if novo_tipo == 1:
                novo_valor_hora = func_entrada(float, 'Novo valor da hora: R$')
                aux_func.valor_hora = novo_valor_hora

            elif novo_tipo == 2 or novo_tipo == 3:
                novo_salario = func_entrada(float, 'Novo salário: R$')
                aux_func.salario = novo_salario

                if novo_tipo == 3:
                    nova_comissao = func_entrada(float, 'Nova comissão (sem o sinal de %): ', limite=True, lim_inf=0.0, lim_sup=100.0)
                    aux_func.comissao = nova_comissao

        elif editar == 4:
            novo_sindicato = func_entrada(str, 'Percente a sindicato? (s/n) ').lower().strip()[0]
            if novo_sindicato == 's':
                aux_func.sindicato = True
                taxa = func_entrada(float, 'Taxa do sindicato: R$')
                aux_func.taxa = taxa
                aux_func.id_sindicato = Empregado.id_sindicato + 1
                Empregado.id_sindicato += 1
            elif novo_sindicato == 'n':
                aux_func.sindicato = False
                aux_func.taxa = -1

        elif editar == 5:
            novo_prazo_pagamento = func_entrada(int, """Prazo de pagamento
1 - Semanal
2 - Mensal
3 - Quinzenal
>> """, limite=True, lim_inf=1, lim_sup=3)
            
            aux_func.p_pagamento = novo_prazo_pagamento - 1

            novo_dia_preferido = func_entrada(int, """Dia preferido para pagamento
2 - Segunda
3 - Terça
4 - Quarta
5 - Quinta
6 - Sexta
>> """, limite=True, lim_inf=2, lim_sup=6)
            
            aux_func.dia_preferido = novo_dia_preferido
            data_hoje = date.today()
            if novo_prazo_pagamento == 1:
                delta = timedelta(days = 7)
            elif novo_prazo_pagamento == 2:
                if data_hoje.month in [1, 3, 5, 7, 8, 10, 12]:
                    delta = timedelta(days = 31)
                elif data_hoje.month == 2:
                    if checar_ano_bissexto(data_hoje):
                        delta = timedelta(days = 29)
                    else:
                        delta = timedelta(days = 28)
                else:
                    delta = timedelta(days = 30)
            elif novo_prazo_pagamento == 3:
                delta = timedelta(days = 15)
            data_hoje += delta
            aux_func.proximo_pagamento = data_hoje.strftime('%d/%m/%Y')

        elif editar == 6:
            nova_forma_pagamento = func_entrada(int, """Forma de pagamento
1 - Cheque correios
2 - Cheque mãos
3 - Depósito bancário
>> """, limite=True, lim_inf=1, lim_sup=3)
            aux_func.f_pagamento = nova_forma_pagamento - 1

        elif editar == 7:
            return
    
        aux_func.duplicar()
        Transação.trns_ultima_undo.append(['Editar', aux_func.id_empregado])
        
        continuar = func_entrada(str, 'Deseja editar algo mais? (s/n) ').lower().strip()[0]
        if continuar == 'n':
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
        elif opção == 4: Empregado.mostrar_empregados()
        elif opção == 5: return


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""                           CARTÃO PONTO                           """
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def lançar_cartão_ponto(opc):
    if opc == 1:
        ponto = CartãoPonto()

        aux_func = Empregado.localizar_empregado()
        if not aux_func: print('\nNão há empregados com esse ID!'); return
        print('\nFuncionário localizado!')
        print(f'\nNome: {aux_func.nome}\n')
        
        hora = datetime.now()
        hora = hora.strftime('%H:%M:%S')

        ponto.entrada = hora
        ponto.entrando = False
        data_ponto = date.today().strftime('%d/%m/%Y')
        ponto.data = data_ponto
        ponto.id_empregado = aux_func.id_empregado
        ponto.ativo = True

        for pt in CartãoPonto.pontos:
            if aux_func.id_empregado == pt.id_empregado and data_ponto == pt.data:
                print('Empregado já bateu ponto hoje!')
                input()
                return

        CartãoPonto.pontos.append(ponto)
        Transação.trns_undo.append(ponto)
        Transação.trns_ultima_undo.append(['Ponto', ponto.id_empregado])
        Transação.trns_redo.clear()
        Transação.trns_ultima_redo.clear()
        print('Ponto de entrada OK!\n')
        input()

    elif opc == 2:
        aux_func = Empregado.localizar_empregado()
        if not aux_func: print('\nNão há empregados com esse ID!'); return
        print('\nFuncionário localizado!')
        print(f'\nNome: {aux_func.nome}\n')

        data = date.today().strftime('%d/%m/%Y')
        hora = datetime.now()
        hora_agora = hora.strftime('%H:%M:%S')
        ponto = CartãoPonto.localizar_ponto(data, aux_func.id_empregado)
        if not ponto:
            print('\nCartão ponto não consta no sistema!')
        else:
            ponto.saída = hora_agora
            ponto.entrando = True
            if aux_func.t_empregado == 0:
                hora_entrada = datetime(year=date.today().year, month=date.today().month, day=date.today().day, hour=int(ponto.entrada[:2]), minute=int(ponto.entrada[3:5]), second=int(ponto.entrada[6:8]))
                hora_saida = hora
                delta = int(float(hora_saida.strftime('%H.%M'))) - int(float(hora_entrada.strftime('%H.%M')))
                aux_func.horas_trabalhadas += delta
            print('Ponto de saída OK!\n')
        input()


def func_cartão_ponto():
    while True:
        menu_cartão_ponto()
        opção = func_entrada(int, '', limite=True, lim_inf=1, lim_sup=4)

        if opção == 1: lançar_cartão_ponto(1)
        elif opção == 2: lançar_cartão_ponto(2)
        elif opção == 3: CartãoPonto.mostrar_pontos()
        elif opção == 4: return

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""                              VENDAS                              """
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def lançar_venda():
    print('\n-=-=- REGISTRAR VENDA -=-=-')
    venda = Venda()
    valor = func_entrada(float, 'Valor da venda: R$')

    data_venda = date.today()
    print('Empregado responsável pela venda:')
    aux_func = Empregado.localizar_empregado()
    if not aux_func:
        print('\nNão há empregados com esse ID!')
        input()
        return

    print('\nFuncionário localizado!')
    venda.valor = valor
    venda.ativo = True
    venda.data = data_venda.strftime('%d/%m/%Y')
    venda.id_empregado = aux_func.id_empregado

    Venda.vendas.append(venda)
    Transação.trns_ultima_undo.append(['Venda', venda.id_empregado])
    Transação.trns_undo.append(venda)
    Transação.trns_redo.clear()
    Transação.trns_ultima_redo.clear()
    print('\nVenda registrada com sucesso!')
    input()


def func_vendas():
    while True:
        menu_vendas()
        opção = func_entrada(int, '', limite=True, lim_inf=1, lim_sup=3)

        if opção == 1: lançar_venda()
        elif opção == 2: Venda.mostrar_vendas()
        elif opção == 3: return


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""                         TAXAS DE SERVIÇO                         """
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def lançar_taxa_serviço():
    taxa = TaxaDeServiço()
    valor = func_entrada(float, 'Valor da taxa: R$')
    taxa.valor = valor
    print('Funcionário associado à taxa:')
    aux_func = Empregado.localizar_empregado()
    if not aux_func:
        print('\nNão há empregados com esse ID!')
        input()
        return
    print('\nFuncionário localizado!')
    print(f'\nNome: {aux_func.nome}')
    taxa.id_empregado = aux_func.id_empregado
    taxa.mes = date.today().month
    taxa.ativo = True

    TaxaDeServiço.taxas.append(taxa)
    Transação.trns_undo.append(taxa)
    Transação.trns_ultima_undo.append(['Taxa', taxa.id_empregado])
    Transação.trns_redo.clear()
    Transação.trns_ultima_redo.clear()
    print('Taxa associada com sucesso!')
    input()


def func_taxas_serviço():
    while True:
        menu_taxas_serviço()
        opção = func_entrada(int, '', limite=True, lim_inf=1, lim_sup=3)

        if opção == 1: lançar_taxa_serviço()
        elif opção == 2: TaxaDeServiço.mostrar_taxas_serviço()
        elif opção == 3: return


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
    return data_hoje.strftime('%d/%m/%Y')


def calcular_salario(emp):
    if emp.t_empregado == 0:
        salario = emp.valor_hora * emp.horas_trabalhadas
    elif emp.t_empregado == 1:
        salario = emp.salario
    elif emp.t_empregado == 2:
        salario = emp.salario
        for venda in Venda.vendas:
            if venda.id_empregado == emp.id_empregado:
                salario += ((emp.comissao) / 100) * venda.valor
    for taxa in TaxaDeServiço.taxas:
        if taxa.id_empregado == emp.id_empregado and taxa.mes == date.today().month:
            salario -= taxa.valor
    if emp.sindicato:
        salario -= emp.taxa
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
    input()


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""                       AGENDAS DE PAGAMENTO                       """
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def listar_agendas():
    print('\n-=-=- AGENDAS DE PAGAMENTOS -=-=-', end='')
    if Empregado.empregados:
        for empregado in Empregado.empregados:
            if empregado.ativo:
                print(f'\nNome: {empregado.nome}')
                print(f'ID: {empregado.id_empregado}')
                print(f'Forma de pagamento: {Empregado.forma_pagamento[empregado.f_pagamento]}')
                print(f'Prazo de pagamento: {Empregado.prazo_pagamento[empregado.p_pagamento]}')
                print(f'Próximo pagamento: {empregado.proximo_pagamento}')
                print(f'Salário a receber: {calcular_salario(empregado):.2f}')
    else: print('\nNão há funcionários cadastrados!')
    input()


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""                           UNDO E REDO                            """
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def undo():
    if len(Transação.trns_undo) == 0:
        print('\nNenhuma operação para desfazer!')
        input()
        return

    transação = Transação.trns_ultima_undo.pop()
    aux_func = Empregado.localizar_empregado(transação[1])
    if transação[0] == 'Adicionar':
        aux_func.ativo = False
        Transação.limbo.append(Empregado.empregados.pop(transação[1] - 1))
        Empregado.id_empregado -= 1

    elif transação[0] == 'Remover':
        aux_func.ativo = True

    elif transação[0] == 'Editar':
        trns = Transação.trns_efetuada_undo.pop()
        Transação.trns_efetuada_redo.append(trns)
        for indice in range(len(Transação.trns_efetuada_undo) - 1, -1, -1):
            if Transação.trns_efetuada_undo[indice].id_empregado == trns.id_empregado:
                restaurar = Transação.trns_efetuada_undo[indice]
                break
        aux_func.restaurar(restaurar)

    elif transação[0] == 'Venda':
        for indice in range(len(Venda.vendas) - 1, -1, -1):
            if Venda.vendas[indice].id_empregado == transação[1]:
                Venda.vendas[indice].ativo = False
                break

    elif transação[0] == 'Ponto':
        for indice in range(len(CartãoPonto.pontos) - 1, -1, -1):
            if CartãoPonto.pontos[indice].id_empregado == transação[1]:
                CartãoPonto.pontos[indice].ativo = False
                break

    elif transação[0] == 'Taxa':
        for indice in range(len(TaxaDeServiço.taxas) - 1, -1, -1):
            if TaxaDeServiço.taxas[indice].id_empregado == transação[1]:
                TaxaDeServiço.taxas[indice].ativo = False
                break

    Transação.trns_redo.append(Transação.trns_undo.pop())
    Transação.trns_ultima_redo.append(transação)
    print('\nOperação desfeita com sucesso!')
    input()


def redo():
    if len(Transação.trns_redo) == 0:
        print('\nNenhuma operação para refazer!')
        input()
        return

    transação = Transação.trns_ultima_redo.pop()
    if transação[0] == 'Adicionar':
        Empregado.empregados.insert(transação[1] - 1, Transação.limbo.pop())
        aux_func = Empregado.localizar_empregado(transação[1])
        aux_func.ativo = True
        Empregado.id_empregado += 1
    
    aux_func = Empregado.localizar_empregado(transação[1])

    if transação[0] == 'Remover':
        aux_func.ativo = False

    elif transação[0] == 'Editar':
        restaurar = Transação.trns_efetuada_redo.pop()
        aux_func.restaurar(restaurar)
        Transação.trns_efetuada_undo.append(restaurar)

    elif transação[0] == 'Venda':
        for indice in range(len(Venda.vendas) - 1, -1, -1):
            if Venda.vendas[indice].id_empregado == transação[1]:
                Venda.vendas[indice].ativo = True
                break

    elif transação[0] == 'Ponto':
        for indice in range(len(CartãoPonto.pontos) - 1, -1, -1):
            if CartãoPonto.pontos[indice].id_empregado == transação[1]:
                CartãoPonto.pontos[indice].ativo = True
                break

    elif transação[0] == 'Taxa':
        for indice in range(len(TaxaDeServiço.taxas) - 1, -1, -1):
            if TaxaDeServiço.taxas[indice].id_empregado == transação[1]:
                TaxaDeServiço.taxas[indice].ativo = True
                break
    
    Transação.trns_undo.append(Transação.trns_redo.pop())
    Transação.trns_ultima_undo.append(transação)
    print('\nOperação refeita com sucesso!')
    input()


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""                        PROGRAMA PRINCIPAL                        """
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


while True:
    menu_principal()
    opção = func_entrada(int, '', limite=True, lim_inf=1, lim_sup=9)

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
