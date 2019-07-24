def func_entrada(tipo, msg, limite = False, lim_inf = -1, lim_sup = -1):
    while True:
        try:
            entrada = tipo(input(msg))
        except KeyboardInterrupt:
            print('\nAté logo!\n')
            exit()
        except ValueError:
            print('Entrada inválida!\n')
        else:
            if tipo == str:
                aux = entrada.split()
                continuar = True
                for palavra in aux:
                    if not palavra.isalnum():
                        continuar = False
                        break
                if continuar:
                    entrada = entrada.title()
                    break
                else: print('Entrada inválida!\n')

            else: 
                if not limite: break
                else:
                    if lim_inf <= entrada <= lim_sup: break
                    else: print('Valor inválido!\n')

    return entrada
