from empregado import Empregado
from transação import Transação

class CartãoPonto():
    pontos = []

    def __init__(self):
        self.entrada = int
        self.entrando = True
        self.saída = int
        self.data = int
        self.id_empregado = int
        self.ativo = bool


    @staticmethod
    def mostrar_pontos():
        print('\n-=-=- CARTÕES PONTO -=-=-', end='')
        continuar = True
        if CartãoPonto.pontos:
            for ponto in CartãoPonto.pontos:
                if ponto.ativo:
                    continuar = True
                    aux_func = Empregado.localizar_empregado(ponto.id_empregado)
                    print(f'\nNome: {aux_func.nome}')
                    print(f'ID: {ponto.id_empregado}')
                    print(f'Data: {ponto.data}')
                    print(f'Entrada: {ponto.entrada}')
                    print('Funcionário ainda em serviço' if not ponto.entrando else f'Saída: {ponto.saída}')
        else: print('\nNão há pontos lançados!')
        if not continuar: print('\nNão há pontos lançados!')


    @staticmethod
    def localizar_ponto(data, id_emp):
        for ponto in CartãoPonto.pontos:
            if data == ponto.data and ponto.id_empregado == id_emp and not ponto.entrando:
                return ponto
        return False