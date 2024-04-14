import unidecode

frase = str(input('digite uma frase: ').strip().upper())
frase = unidecode.unidecode(frase)
analise = str(input('digite uma letra para analise: ')).upper()
contador = frase.count(f'{analise}')
posição = frase.find(f'{analise}')
final = frase.rfind(f'{analise}')

print(f'A letra {analise} aparece {contador} vezes \nA primeira letra {analise} na posição {posição+1} \nA ultima letra {analise} na posição {final+1} ')
