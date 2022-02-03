soma = 0 # aqui variavel de soma que começa em 0
cont = 1 # contador começa com 1
while cont <= 5: # contador termina ate 5
    s1 = float(input('Digite a {} nota '.format(cont)))
    soma = s1 + soma # soma a nota
    cont = cont + 1 # conta de  1 em 1
media = soma / 5
print('Media final: {}'.format(media))
