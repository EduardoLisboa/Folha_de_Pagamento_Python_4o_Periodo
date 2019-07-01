from empregado import Empregado

class TaxaDeServiço():
    taxas = []

    def __init__(self):
        self.valor = float
        self.mes = int
        self.ativo = bool
        self.id_empregado = int


    @staticmethod
    def mostrar_taxas_serviço():
        print('\n-=-=- TAXAS REGISTRADAS -=-=-', end='')
        if TaxaDeServiço.taxas:
            for taxa in TaxaDeServiço.taxas:
                if taxa.ativo:
                    print(f'\nValor da taxa: {taxa.valor:.2f}')
                    print(f'Nome: {Empregado.empregados[taxa.id_empregado - 1].nome}')
                    print(f'ID: {taxa.id_empregado}')
                    print(f'Mês da taxa: {meses[taxa.mes]}')
        else: print('\nNão há taxas de serviço cadastradas!')