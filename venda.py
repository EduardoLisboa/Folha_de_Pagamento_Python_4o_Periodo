from empregado import Empregado
from transação import Transação

class Venda():
    vendas = []

    def __init__(self):
        self.valor = float
        self.data_venda = int
        self.ativo = bool
        self.id_empregado = int

    
    @staticmethod
    def mostrar_vendas():
        print('\n-=-=- VENDAS EFETUADAS -=-=-', end='')
        continuar = True
        if Venda.vendas:
            for venda in Venda.vendas:
                if venda.ativo:
                    continuar = True
                    print(f'\nID Empregado: {venda.id_empregado}')
                    print(f'Nome: {Empregado.empregados[venda.id_empregado - 1].nome}')
                    print(f'Valor da venda: R${venda.valor:.2f}')
                    print(f'Data da venda: {venda.data}')
        else: print('\nNão há vendas cadastradas!')
        if not continuar: print('\nNão há vendas cadastradas!')
        input()
