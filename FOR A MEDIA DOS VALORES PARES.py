#SOMA
s1 = 0
#QUANTIDADE
s2 = 0
for i in range(1,101):
  if (i % 2 == 0):
    s1 += i
    s2 += 1
media = s1 / s2
print('A media dos pares 1,100 e: {}'.format(media))

