inicial = int(input('Qual valor deseja iniciar a contagem:'))
final = int(input('Qual valor deseja terminar a contagem'))
s1 = inicial
while (s1 <= final):
    if (s1 % 2 == 0):
       print(s1)
    s1 = s1 + 1
