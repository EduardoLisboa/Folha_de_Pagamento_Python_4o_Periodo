from empregado import Empregado
from transação import Transação

meses = {1 : 'Janeiro', 2 : 'Fevereiro', 3 : 'Março',
        4 : 'Abril', 5 : 'Maio', 6 : 'Junho',
        7 : 'Julho', 8 : 'Agosto', 9 : 'Setembro',
        10 : 'Outubro', 11 : 'Novembro', 12 : 'Dezembro'}

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
        continuar = True
        if TaxaDeServiço.taxas:
            for taxa in TaxaDeServiço.taxas:
                if taxa.ativo:
                    continuar = True
                    print(f'\nValor da taxa: {taxa.valor:.2f}')
                    print(f'Nome: {Empregado.empregados[taxa.id_empregado - 1].nome}')
                    print(f'ID: {taxa.id_empregado}')
                    print(f'Mês da taxa: {meses[taxa.mes]}')
        else: print('\nNão há taxas de serviço cadastradas!')
        if not continuar: print('\nNão há taxas de serviço cadastradas!')
        input()