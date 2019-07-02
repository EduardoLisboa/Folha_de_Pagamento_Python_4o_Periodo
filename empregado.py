from datetime import timedelta

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
        # self.salario = float
        # self.comissao = float

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
    def localizar_empregado():
        while True:
            id_func = str(input('Insira o ID do funcionário: '))
            if id_func.isnumeric(): break
            else: print('\nID inválido!')
        id_func = int(id_func)
        for empregado in Empregado.empregados:
            if id_func == empregado.id_empregado:
                return empregado
        return False


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


class Assalariado(Empregado):

    def __init__(self, id_empregado, nome, endereço, t_empregado, f_pagamento, dia_preferido, ativo, sindicato, taxa, id_sindicato, ultimo_pagamento, proximo_pagamento, p_pagamento, salario):
        super().__init__(id_empregado, nome, endereço, t_empregado, f_pagamento, dia_preferido, ativo, sindicato, taxa, id_sindicato, ultimo_pagamento, proximo_pagamento, p_pagamento)
        self.salario = salario


class Comissionado(Empregado):

    def __init__(self, id_empregado, nome, endereço, t_empregado, f_pagamento, dia_preferido, ativo, sindicato, taxa, id_sindicato, ultimo_pagamento, proximo_pagamento, p_pagamento, salario, comissao):
        super().__init__(id_empregado, nome, endereço, t_empregado, f_pagamento, dia_preferido, ativo, sindicato, taxa, id_sindicato, ultimo_pagamento, proximo_pagamento, p_pagamento)
        self.salario = salario
        self.comissao = comissao
