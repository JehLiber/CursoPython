primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')


# if  primeiro_valor > segundo_valor: 
#    print('primeiro_valor=', primeiro_valor, 'é maior do que o segundo_valor=',segundo_valor)
#else: 
#    print('segundo_valor=',segundo_valor, 'é maior do que o primeiro_valor=',primeiro_valor)
#


if primeiro_valor >= segundo_valor:
    print(
        f'{primeiro_valor=} é maior ou igual'
        f'ao que {segundo_valor}'
    )
else:
    print(
        f'{segundo_valor=} é maior '
        f'do que {primeiro_valor=}'
    )    