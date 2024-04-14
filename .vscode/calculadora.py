n1 = float(input('Digite um numero: '))
n2 = float(input('Digite um numero: '))
print('digite a operação que deseja realizar (+, -, *, /)')
operação = str(input(': ')).strip()

#if operação == "+":
#    r = n1 + n2
#    print(f'o resultado foi {r:.2f}')
#if operação == "-":
#    r = n1 - n2
#    print(f'o resultado foi {r:.2f}')
#if operação == "*":
#    r = n1 * n2
#    print(f'o resultado foi {r:.2f}')
#if operação == "/":
#    r = n1 / n2
#    print(f'o resultado foi {r:.2f}')

match operação:
    case '+':
        r = n1 + n2
        print(f' o resultado foi {r:.2f}')
    case '-':
        r = n1 - n2
        print(f' o resultado foi {r:.2f}')
    case '*':
        r = n1 * n2
        print(f' o resultado foi {r:.2f}')
    case '/':
        r = n1 / n2
        print(f' o resultado foi {r:.2f}')