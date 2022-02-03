# A TABUADA COMEÇA COM 1
tabuada = 1
# E A TABUADA TERMINA EM 10 NO 1 WHILE NO LAÇO EXTERNO
while tabuada <= 10:
    print('Qual tabuada {}:'.format(tabuada))
    i = 1
    #AQUI E O LAÇO DE 1 A 10 INTERNO
    while i <= 10:
        print('{} X {} = {}'.format(tabuada, i, tabuada * i))
        i += 1
    # AQUI E O CONTADOR O INTERADOR (COMEÇA 1 LA EM CIMA DEPOIS ACRESCENTA 1 VAI PRA DOIS
    tabuada += 1