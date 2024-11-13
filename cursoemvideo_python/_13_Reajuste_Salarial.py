SA = float(input('digite o salario atual do funcionario: '))
AU = float(input('digite a porcentagem de aumento para o funcionario: '))
SN = SA + (SA / 100 * AU)
print(f'seu salario atual é de {SA} mas com um aumento de {AU}% a partir de agora será de {SN}!!!')