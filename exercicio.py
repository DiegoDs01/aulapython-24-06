n1 = float(input('Digite um número '))
n2 = float(input('Digite outro número '))
n3 = float(input('Digite outro número '))
n4 = float(input('Digite outro número '))

media = (n1+n2+n3+n4)/4

print("A média é {}" .format(media))

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



in1 = input('Digite uma palavra ')
in2 = input('Digite uma letra ')

count = in1.count(in2)

print(count)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

qtd_notas = int(input("Digite o numero de notas"))

soma = 0

fot i in range(qtd_notas):
    soma += int(input("Digite a nota"))
print(soma/qtd_notas)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

num1 = float(input('Digite um número '))
num2 = float(input('Digite outro número '))

soma = (num1 + num2)
sub = (num1 - num2)
mult = (num1 * num2)
div = (num1 / num2)

print("O resultado de {} + {} é = {}" .format(num1, num2, soma))
print("O resultado de {} - {} é = {}" .format(num1, num2, sub))
print("O resultado de {} x {} é = {}" .format(num1, num2, mult))
print("O resultado de {} : {} é = {}" .format(num1, num2, div))

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

