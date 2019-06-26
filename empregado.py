class Empregado():
    id_empregado = 0
    id_sindicato = 0
    tipo_empregado = ['Horário', 'Assalariado', 'Comissionado']
    forma_pagamento = ['Cheque correios', 'Cheque mãos', 'Depósito bancário']
    prazo_pagamento = ['Semanal', 'Mensal', 'Quinzenal']
    empregados = []

    def __init__(self):
        self.id_empregado = int
        self.nome = str
        self.endereço = str
        # 0 - Horário, 1 = Assalariado, 2 = Comissionado
        self.t_empregado = int
        self.salario = float
        self.comissao = float
        # 0 - Cheque correios, 1 = Cheque mãos, 2 = Depósito bancário
        self.f_pagamento = int
        self.dia_preferido = int
        self.ativo = bool

        self.sindicato = bool
        self.taxa = float
        self.id_sindicato = int

        self.ultimo_pagamento = str
        self.proximo_pagamento = str
        # 0 - Semanal, 1 - Mensal, 2 - Quinzenal
        self.p_pagamento = int

