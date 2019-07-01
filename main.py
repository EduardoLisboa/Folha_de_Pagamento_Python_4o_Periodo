from empregado import *
from venda import Venda
from cartãoponto import CartãoPonto
from taxaserviço import TaxaDeServiço
from menus import *
from datetime import date, timedelta, datetime

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""                          FUNÇÕES GERAIS                          """
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def checar_ano_bissexto(data):
    return True if data.year % 4 == 0 and data.year % 100 != 0 or data.year % 400 == 0 else False


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""                            EMPREGADOS                            """
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def localizar_empregado():
    while True:
        id_func = str(input('Insira o ID do funcionário: '))
        if id_func.isnumeric(): break
        else: print('\nID inválido!')
    id_func = int(id_func)
    for empregado in Empregado.empregados:
        if id_func == empregado.id_empregado:
            print('\nFuncionário localizado!')
            return empregado
    return False


def adicionar_empregado():
    print('\n-=-=- ADICIONAR -=-=-')
    ativo = True
    id_empregado = Empregado.id_empregado + 1
    Empregado.id_empregado += 1

    while True:
        ruim = False
        nome = str(input('Nome: ')).strip().title()
        for palavra in nome.split():
            if not palavra.isalpha():
                ruim = True
                break
        if not ruim: break
        else: print('\nNome inválido!')

    while True:
        ruim = False
        endereço = str(input('Endereço: ')).strip().title()
        for palavra in endereço.split():
            if not palavra.isalnum():
                ruim = True
                break
        if not ruim: break
        else: print('\nEndereço inválido!')
    
    while True:
        sindicato = str(input('Pertence a sindicato? (s/n) ')).lower().strip()[0]
        if sindicato.isalpha() and sindicato in 'ns': break
        else: print('\nResposta inválida!')
    if sindicato == 's':
        sindicato = True
        while True:
            taxa = str(input('Taxa do sindicato: R$'))
            if taxa.isnumeric() and float(taxa) > 0.0: break
            else: print('\nTaxa inválida!')
        id_sindicato = Empregado.id_sindicato + 1
        id_sindicato += 1
    elif sindicato == 'n':
        sindicato = False
        id_sindicato = -1
        taxa = -1

    while True:
        prazo_pagamento = str(input("""Prazo de pagamento
1 - Semanal
2 - Mensal
3 - Quinzenal
>> """))
        if prazo_pagamento.isnumeric() and 0 < int(prazo_pagamento) < 4: break
        else: print('\nPrazo inválido!')
    prazo_pagamento = int(prazo_pagamento) - 1

    while True:
        forma_pagamento = str(input("""Forma de pagamento
1 - Cheque correios
2 - Cheque mãos
3 - Depósito bancário
>> """))
        if forma_pagamento.isnumeric() and 0 < int(forma_pagamento) < 4: break
        else: print('\nForma de pagamento inválida!')
    forma_pagamento = int(forma_pagamento) - 1

    while True:
        dia_preferido = str(input("""Dia preferido para pagamento
2 - Segunda
3 - Terça
4 - Quarta
5 - Quinta
6 - Sexta
>> """))
        if dia_preferido.isnumeric() and 1 < int(dia_preferido) < 7: break
        else: print('\nDia inválido!')
    dia_preferido = int(dia_preferido)
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

    while True:
        tipo = str(input("""Tipo de empregado
1 - Horário
2 - Assalariado
3 - Comissionado
>> """))
        if tipo.isnumeric() and 0 < int(tipo) < 4: break
        else: print('\nOpção inválida!')
    tipo = int(tipo) - 1
    if tipo == 0:
        while True:
            valor_hora = str(input('Valor da hora: R$'))
            if valor_hora.isnumeric() and float(valor_hora) > 0.0:
                valor_hora = float(valor_hora)
                break
            else: print('\nValor inválido!')
        novo_empregado = Horario(id_empregado, nome, endereço, tipo, forma_pagamento, dia_preferido, ativo, sindicato, taxa, id_sindicato, '', proximo_pagamento, prazo_pagamento, valor_hora)

    elif tipo == 1:
        while True:
            salario = str(input('Salário: R$'))
            if salario.isnumeric() and float(salario) > 0.0:
                salario = float(salario)
                break
            else: print('\nSalário inválido!')
        novo_empregado = Assalariado(id_empregado, nome, endereço, tipo, forma_pagamento, dia_preferido, ativo, sindicato, taxa, id_sindicato, '', proximo_pagamento, prazo_pagamento, salario)

    elif tipo == 2:
        while True:
            salario = str(input('Salário: R$'))
            if salario.isnumeric() and float(salario) > 0.0:
                salario = float(salario)
                break
            else: print('\nSalário inválido!')
        while True:
            comissao = str(input('Comissão (sem o sinal de %): '))
            if comissao.isnumeric() and 0.0 < float(comissao) <= 100.0:
                comissao = float(comissao)
                break
            else: print('\nComissão inválida!')
        novo_empregado = Comissionado(id_empregado, nome, endereço, tipo, forma_pagamento, dia_preferido, ativo, sindicato, taxa, id_sindicato, '', proximo_pagamento, prazo_pagamento, salario, comissao)

    Empregado.empregados.append(novo_empregado)
    print('\nEmpregado cadastrado com sucesso!')


def remover_empregado():
    while True:
        print('\n-=-=- REMOVER -=-=-')
        aux_func = localizar_empregado()
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
            break
        elif confirmação == 'n': return 


def editar_empregado():
    while True:
        print('\n-=-=- EDITAR -=-=-')
        while True:
            aux_func = localizar_empregado()
            if not aux_func:
                print('\nNão existe funcionário com esse ID!')
            else: break

        print(f'\nNome: {aux_func.nome}')
        print(f'Endereço: {aux_func.endereço}')
        print(f'Tipo de empregado: {Empregado.tipo_empregado[aux_func.t_empregado]}')
        print('Sindicato: ', end='')
        print(f'Sim' if aux_func.sindicato else 'Não')
        print(f'Prazo de pagamento: {Empregado.prazo_pagamento[aux_func.p_pagamento]}')
        print(f'Forma de pagamento: {Empregado.forma_pagamento[aux_func.f_pagamento]}\n')

        while True:
            editar = str(input("""1 - Nome
2 - Endereço
3 - Tipo de empregado
4 - Sindicato
5 - Prazo de pagamento
6 - Forma de pagamento
7 - Retornar
>> """))
            if editar.isnumeric() and 0 < int(editar) < 8: break
            else: print('\nOpção inválida!')
        editar = int(editar)

        if editar == 1:
            while True:
                ruim = False
                aux_func.nome = str(input('\nNovo nome: ')).strip().title()
                for nome in aux_func.nome.split():
                    if not nome.isalpha():
                        ruim = True
                        break
                if not ruim: break
                else: print('\nNome inválido!')

        elif editar == 2:
            while True:
                ruim = False
                aux_func.endereço = str(input('\nNovo endereço: ')).strip().title()
                for palavra in aux_func.endereço.split():
                    if not palavra.isalnum():
                        ruim = True
                        break
                if not ruim: break
                else: print('\nEndereço inválido!')

        elif editar == 3:
            while True:
                tipo = str(input("""\nTipo de empregado
1 - Horário
2 - Assalariado
3 - Comissionado
>> """))
                if tipo.isnumeric() and 0 < int(tipo) < 4: break
                else: print('\nTipo inválido!')
            tipo = int(tipo)
            aux_func.t_empregado = tipo - 1
            if tipo == 1:
                while True:
                    aux_func.valor_hora = str(input('Valor da hora: R$'))
                    if aux_func.valor_hora.isnumeric():
                        aux_func.valor_hora = float(aux_func.valor_hora)
                        break
                    else: print('\nValor inválido!')
            elif tipo == 2 or tipo == 3:
                while True:
                    aux_func.salario = str(input('Salário: R$'))
                    if aux_func.salario.isnumeric():
                        aux_func.salario = float(aux_func.salario)
                        break
                    else: print('\nSalário inválido!')
                if tipo == 3:
                    while True:
                        aux_func.comissao = str(input('Comissão (sem o sinal de %): '))
                        if aux_func.comissao.isnumeric() and 0.0 < float(aux_func.comissao) <= 100.0:
                            aux_func.comissao = float(aux_func.comissao)
                            break
                        else: print('\nComissão inválida!')

        elif editar == 4:
            while True:
                sindicato = str(input('Pertence a sindicato? (s/n) ')).lower().strip()[0]
                if sindicato.isalpha() and sindicato in 'ns': break
                else: print('\nEntrada inválida!')
            if sindicato == 's':
                aux_func.sindicato = True
                while True:
                    aux_func.taxa = str(input('Taxa do sindicato: R$'))
                    if aux_func.taxa.isnumeric():
                        aux_func.taxa = float(aux_func.taxa)
                        break
                    else: print('\nTaxa inválida!')
                aux_func.id_sindicato = Empregado.id_sindicato + 1
                Empregado.id_sindicato += 1
            elif sindicato == 'n':
                aux_func.sindicato = False

        elif editar == 5:
            while True:
                prazo_pagamento = str(input("""Prazo de pagamento
1 - Semanal
2 - Mensal
3 - Quinzenal
>> """))
                if prazo_pagamento.isnumeric() and 0 < int(prazo_pagamento) < 4: break
                else: print('\nPrazo inválido!')
            prazo_pagamento = int(prazo_pagamento)
            aux_func.p_pagamento = prazo_pagamento - 1
            while True:
                dia_preferido = str(input("""Dia preferido para pagamento
2 - Segunda
3 - Terça
4 - Quarta
5 - Quinta
6 - Sexta
>> """))
                if dia_preferido.isnumeric() and 1 < int(dia_preferido) < 7: break
                else: print('\nDia inválido!')
            aux_func.dia_preferido = int(dia_preferido)
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
            while True:
                forma_pagamento = str(input("""Forma de pagamento
1 - Cheque correios
2 - Cheque mãos
3 - Depósito bancário
>> """))
                if forma_pagamento.isnumeric() and 0 < int(forma_pagamento) < 4: break
                else: print('\nForma de pagamento inválida!')
            forma_pagamento = int(forma_pagamento)
            aux_func.f_pagamento = forma_pagamento - 1
        elif editar == 7:
            return
    
        while True:
            continuar = str(input('Deseja editar algo mais? (s/n) ')).lower().strip()[0]
            if continuar.isalpha() and continuar in 'ns': break
            else: print('\nEntrada inválida!')
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

def localizar_ponto(data, id_emp):
    for ponto in CartãoPonto.pontos:
        if data == ponto.data and ponto.id_empregado == id_emp and not ponto.entrando:
            return ponto
    return False


def lançar_cartão_ponto(opc):
    if opc == 1:
        ponto = CartãoPonto()

        aux_func = localizar_empregado()
        if not aux_func: print('\nNão há empregados com esse ID!'); return
        print(f'\nNome: {aux_func.nome}\n')
        
        hora = datetime.now()
        hora = hora.strftime('%H:%M:%S')

        ponto.entrada = hora
        ponto.entrando = False
        data_ponto = date.today().strftime('%d/%m/%Y')
        ponto.data = data_ponto
        ponto.id_empregado = aux_func.id_empregado

        for ponto in CartãoPonto.pontos:
            if aux_func.id_empregado == ponto.id_empregado and data_ponto == ponto.data:
                print('Empregado já bateu ponto hoje!')
                return

        CartãoPonto.pontos.append(ponto)
        print('Ponto de entrada OK!\n')

    elif opc == 2:
        aux_func = localizar_empregado()
        if not aux_func: print('\nNão há empregados com esse ID!'); return
        print(f'\nNome: {aux_func.nome}\n')

        data = date.today().strftime('%d/%m/%Y')
        hora = datetime.now()
        hora_agora = hora.strftime('%H:%M:%S')
        ponto = localizar_ponto(data, aux_func.id_empregado)
        if not ponto: print('\nCartão ponto não consta no sistema!')
        else:
            ponto.saída = hora_agora
            ponto.entrando = True
            if aux_func.t_empregado == 0:
                hora_entrada = datetime(year=date.today().year, month=date.today().month, day=date.today().day, hour=int(ponto.entrada[:2]), minute=int(ponto.entrada[3:5]), second=int(ponto.entrada[6:8]))
                hora_saida = hora
                delta = int(float(hora_saida.strftime('%H.%M'))) - int(float(hora_entrada.strftime('%H.%M')))
                aux_func.horas_trabalhadas += delta
            print('Ponto de saída OK!\n')


def func_cartão_ponto():
    while True:
        menu_cartão_ponto()
        while True:
            opção = str(input())
            if opção.isnumeric() and 0 < int(opção) < 5: break
            else: print('\nOpção inválida!\n')

        opção = int(opção)

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
    while True:
        valor = str(input('Valor da venda: R$'))
        if valor.isnumeric() and float(valor) > 0.0: break
        else: print('\nValor inválido!')
    data_venda = date.today()
    print('Empregado responsável pela venda:')
    aux_func = localizar_empregado()
    if not aux_func: print('\nNão há empregados com esse ID!'); return
    venda.valor = float(valor)
    venda.ativo = True
    venda.data = data_venda.strftime('%d/%m/%Y')
    venda.id_empregado = aux_func.id_empregado

    Venda.vendas.append(venda)
    print('\nVenda registrada com sucesso!')


def func_vendas():
    while True:
        menu_vendas()
        while True:
            opção = str(input())
            if opção.isnumeric() and 0 < int(opção) < 4: break
            else: print('\nOpção inválida!\n')
        opção = int(opção)

        if opção == 1: lançar_venda()
        elif opção == 2: Venda.mostrar_vendas()
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


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""                         TAXAS DE SERVIÇO                         """
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def lançar_taxa_serviço():
    taxa = TaxaDeServiço()
    taxa.valor = float(input('Valor da taxa: R$'))
    print('Funcionário associado à taxa:')
    aux_func = localizar_empregado()
    if not aux_func: print('\nNão há empregados com esse ID!'); return
    print(f'\nNome: {aux_func.nome}')
    taxa.id_empregado = aux_func.id_empregado
    taxa.mes = date.today().month
    taxa.ativo = True

    TaxaDeServiço.taxas.append(taxa)
    print('Taxa associada com sucesso!')


def func_taxas_serviço():
    while True:
        menu_taxas_serviço()
        while True:
            opção = str(input())
            if opção.isnumeric() and 0 < int(opção) < 4: break
            else: print('\nOpção inválida!\n')
        opção = int(opção)

        if opção == 1: lançar_taxa_serviço()
        elif opção == 2: TaxaDeServiço.mostrar_taxas_serviço()
        elif opção == 3: return

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
            print('\nOpção inválida!\n>> ', end='')
    
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
