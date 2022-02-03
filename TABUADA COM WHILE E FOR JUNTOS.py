tabuada = 1
while tabuada <= 10:
    print('Qual Tabuada= {}'.format(tabuada))
    for i in range(1,11,1):
        print('{} X {} = {}'.format(tabuada, i, tabuada * i))
    tabuada += 1