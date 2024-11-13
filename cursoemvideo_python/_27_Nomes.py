nome = str(input('digite seu nome completo: ')).strip().upper().split()
ultimo_nome = nome.pop()

print('muito prazer em te conhecer!!')
print(f'Seu primeiro nome é {nome[0]}')
print(f'Seu ultimo nome é {ultimo_nome}')
