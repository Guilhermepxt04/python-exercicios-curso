salario = float(input('qual o salario do funcionario?: R$ '))

if salario <= 1250:
    aumento = salario + salario / 100 * 15
    print(f'o funcionario irá passar a ganhar: R${aumento:.2f}')
if salario > 1250:
    aumento = salario + salario / 100 * 10
    print(f'o funcionario irá passar a ganhar: R${aumento:.2f}')