from empregado import Empregado

class CartãoPonto():
    pontos = []

    def __init__(self):
        self.entrada = int
        self.entrando = True
        self.saída = int
        self.data = int
        self.id_empregado = int


    @staticmethod
    def mostrar_pontos():
        print('\n-=-=- CARTÕES PONTO -=-=-')
        if CartãoPonto.pontos:
            for ponto in CartãoPonto.pontos:
                print(f'\nNome: {Empregado.empregados[ponto.id_empregado - 1].nome}')
                print(f'ID: {ponto.id_empregado}')
                print(f'Data: {ponto.data}')
                print(f'Entrada: {ponto.entrada}')
                print('Funcionário ainda em serviço' if not ponto.entrando else f'Saída: {ponto.saída}')
        else: print('\nNão há pontos lançados!')