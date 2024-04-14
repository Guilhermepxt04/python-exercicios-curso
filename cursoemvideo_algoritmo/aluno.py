
#variaveis
n1 = int(input('digite uma nota do aluno: '))
n2 = int(input('digite uma segunda nota do aluno: '))
n3 = int(input('digite uma terceira nota do aluno: '))
n4 = int(input('digite uma quarta nota do aluno: '))
m = int(n1 + n2 + n3 + n4) / 4
print(f'a media do aluno foi {m:.2f}')

#condições de aproveitamento

match m:
    case 9 | 10:
        print('O aproveitamento do aluno foi: A')
    case 7 | 8:
        print('O aproveitamento do aluno foi: B')
    case 5 | 6:
        print('O aproveitamento do aluno foi: C')
    case 3 | 4:
        print('O aproveitamento do aluno foi: D')
    case 1 | 2:
        print('O aproveitamento do aluno foi: E')
    case 0:
        print('O aproveitamento do aluno foi: F')

# condição de aprovação 

if m >= 8:
    print('o alundo está aprovado')
else:
    if m >= 4 and m < 8:
        print('o aluno está de recuperação')
    else:
        print('o alundo está reprovado')
