from datetime import date

menores = 0
maiores = 0

for c in range(1,8):
    birthday = int(input(f'Em que ano a {c} pessoa nasceu?: '))
    age = date.today().year - birthday
    if age < 18:
        menores += 1
    else:
        maiores += 1

print(f'Entre essas 7 pessoas existem {menores} menores de idade, e {maiores} maiores de idade')