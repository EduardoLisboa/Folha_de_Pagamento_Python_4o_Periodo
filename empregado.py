from datetime import timedelta
from transação import Transação

class Empregado():
    id_empregado = 0
    id_sindicato = 0
    tipo_empregado = ['Horário', 'Assalariado', 'Comissionado']
    forma_pagamento = ['Cheque correios', 'Cheque mãos', 'Depósito bancário']
    prazo_pagamento = ['Semanal', 'Mensal', 'Quinzenal']
    empregados = []

    def __init__(self, id_empregado, nome, endereço, t_empregado, f_pagamento, dia_preferido, ativo, sindicato, taxa, id_sindicato, ultimo_pagamento, proximo_pagamento, p_pagamento):
        self.id_empregado = id_empregado
        self.nome = nome
        self.endereço = endereço
        # 0 - Horário, 1 = Assalariado, 2 = Comissionado
        self.t_empregado = t_empregado

        # 0 - Cheque correios, 1 = Cheque mãos, 2 = Depósito bancário
        self.f_pagamento = f_pagamento
        self.dia_preferido = dia_preferido
        self.ativo = ativo

        self.sindicato = sindicato
        self.taxa = taxa
        self.id_sindicato = id_sindicato

        self.ultimo_pagamento = ultimo_pagamento
        self.proximo_pagamento = proximo_pagamento
        # 0 - Semanal, 1 - Mensal, 2 - Quinzenal
        self.p_pagamento = p_pagamento


    @staticmethod
    def localizar_empregado(id_emp = -1):
        if id_emp == -1:
            while True:
                id_func = str(input('Insira o ID do funcionário: '))
                if id_func.isnumeric(): break
                else: print('\nID inválido!')
            id_func = int(id_func)
            for empregado in Empregado.empregados:
                if id_func == empregado.id_empregado:
                    return empregado
            return False
        else:
            return Empregado.empregados[id_emp - 1]


    @staticmethod
    def mostrar_empregados():
        print('\n-=-=- EMPREGADOS -=-=-', end='')
        continuar = False
        for emp in Empregado.empregados:
            if emp.ativo == True:
                continuar = True
                break
        if continuar:
            for emp in Empregado.empregados:
                if emp.ativo:
                    print(f'\nNome: {emp.nome}')
                    print(f'ID: {emp.id_empregado}')
                    print(f'Endereço: {emp.endereço}')
                    print('Pertence a sindicato? ', end='')
                    print(f'Sim' if emp.sindicato else 'Não')
                    if emp.sindicato:
                        print(f'ID Sindicato: {emp.id_sindicato}')
                    if emp.t_empregado == 0:
                        print(f'Valor da hora: R${emp.valor_hora:.2f}')
                    else:
                        print(f'Salário: R${emp.salario:.2f}')
                        if emp.t_empregado == 2:
                            print(f'Comissão: {emp.comissao:.2f}%')
                    print(f'Prazo de pagamento: {Empregado.prazo_pagamento[emp.p_pagamento]}')
                    print(f'Forma de pagamento: {Empregado.forma_pagamento[emp.f_pagamento]}')
                    print(f'Próximo pagamento: {emp.proximo_pagamento}')
        else:
            print('\nNão há funcionários cadastrados!')


class Horario(Empregado):
    
    def __init__(self, id_empregado, nome, endereço, t_empregado, f_pagamento, dia_preferido, ativo, sindicato, taxa, id_sindicato, ultimo_pagamento, proximo_pagamento, p_pagamento, valor_hora):
        super().__init__(id_empregado, nome, endereço, t_empregado, f_pagamento, dia_preferido, ativo, sindicato, taxa, id_sindicato, ultimo_pagamento, proximo_pagamento, p_pagamento)
        self.valor_hora = valor_hora
        self.horas_trabalhadas = 0

    
    def duplicar(self):
        copia = Horario(self.id_empregado, self.nome, self.endereço,
        self.t_empregado, self.f_pagamento, self.dia_preferido,
        self.ativo, self.sindicato, self.taxa, self.id_sindicato,
        self.ultimo_pagamento, self.proximo_pagamento,
        self.p_pagamento, self.valor_hora)
        Transação.trns_efetuada.append(copia)
        Transação.index_efetuada += 1
    

    def restaurar(self, other):
        self.id_empregado = other.id_empregado
        self.nome = other.nome
        self.endereço = other.endereço
        self.t_empregado = other.t_empregado
        self.f_pagamento = other.f_pagamento
        self.dia_preferido = other.dia_preferido
        self.ativo = other.ativo
        self.sindicato = other.sindicato
        self.taxa = other.taxa
        self.id_sindicato = other.id_sindicato
        self.ultimo_pagamento = other.ultimo_pagamento
        self.proximo_pagamento = other.proximo_pagamento
        self.p_pagamento = other.p_pagamento
        self.valor_hora = other.valor_hora


class Assalariado(Empregado):

    def __init__(self, id_empregado, nome, endereço, t_empregado, f_pagamento, dia_preferido, ativo, sindicato, taxa, id_sindicato, ultimo_pagamento, proximo_pagamento, p_pagamento, salario):
        super().__init__(id_empregado, nome, endereço, t_empregado, f_pagamento, dia_preferido, ativo, sindicato, taxa, id_sindicato, ultimo_pagamento, proximo_pagamento, p_pagamento)
        self.salario = salario


    def duplicar(self):
        copia = Assalariado(self.id_empregado, self.nome, self.endereço,
        self.t_empregado, self.f_pagamento, self.dia_preferido,
        self.ativo, self.sindicato, self.taxa, self.id_sindicato,
        self.ultimo_pagamento, self.proximo_pagamento,
        self.p_pagamento, self.salario)
        Transação.trns_efetuada.append(copia)
        Transação.index_efetuada += 1


    def restaurar(self, other):
        self.id_empregado = other.id_empregado
        self.nome = other.nome
        self.endereço = other.endereço
        self.t_empregado = other.t_empregado
        self.f_pagamento = other.f_pagamento
        self.dia_preferido = other.dia_preferido
        self.ativo = other.ativo
        self.sindicato = other.sindicato
        self.taxa = other.taxa
        self.id_sindicato = other.id_sindicato
        self.ultimo_pagamento = other.ultimo_pagamento
        self.proximo_pagamento = other.proximo_pagamento
        self.p_pagamento = other.p_pagamento
        self.salario = other.salario


class Comissionado(Empregado):

    def __init__(self, id_empregado, nome, endereço, t_empregado, f_pagamento, dia_preferido, ativo, sindicato, taxa, id_sindicato, ultimo_pagamento, proximo_pagamento, p_pagamento, salario, comissao):
        super().__init__(id_empregado, nome, endereço, t_empregado, f_pagamento, dia_preferido, ativo, sindicato, taxa, id_sindicato, ultimo_pagamento, proximo_pagamento, p_pagamento)
        self.salario = salario
        self.comissao = comissao
    

    def duplicar(self):
        copia = Comissionado(self.id_empregado, self.nome, self.endereço,
        self.t_empregado, self.f_pagamento, self.dia_preferido,
        self.ativo, self.sindicato, self.taxa, self.id_sindicato,
        self.ultimo_pagamento, self.proximo_pagamento,
        self.p_pagamento, self.salario, self.comissao)
        Transação.trns_efetuada.append(copia)
        Transação.index_efetuada += 1

    
    def restaurar(self, other):
        self.id_empregado = other.id_empregado
        self.nome = other.nome
        self.endereço = other.endereço
        self.t_empregado = other.t_empregado
        self.f_pagamento = other.f_pagamento
        self.dia_preferido = other.dia_preferido
        self.ativo = other.ativo
        self.sindicato = other.sindicato
        self.taxa = other.taxa
        self.id_sindicato = other.id_sindicato
        self.ultimo_pagamento = other.ultimo_pagamento
        self.proximo_pagamento = other.proximo_pagamento
        self.p_pagamento = other.p_pagamento
        self.salario = other.salario
        self.comissao = other.comissao
