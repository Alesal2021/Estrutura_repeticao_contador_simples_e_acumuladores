while True:
    nome = input('Nome de usuario:')
# Caso o nome de usuario nao seja alessandro volta pro loop com a função (CONTINUE)
    if nome != 'alessandro':
        continue
# Caso o nome de usuario nao digite a senha certa volta pro loop.
    senha = input('Digite sua senha:')
    if senha == 'sal098':
        break
print('Acesso autorizado')
