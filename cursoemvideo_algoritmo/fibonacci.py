number_1 = 0
number_2 = 1
count = 3
limite = int(input('até quanto quer ver?: '))

print(number_1)
print(number_2)

def fibonaci(number_1, number_2):
    next_number = number_1 + number_2 
    return number_2 , next_number

while count <= limite:
    number_1 ,  number_2 = fibonaci(number_1, number_2)
    print(number_2)
    count = count + 1