# if you wanna complete a number w zeros to the left

a = 2.2

print(f"Com zeros à esquerda: {a:04.2f}") #will print 0002.20

# if else

b = int(input("Digite o primeiro número: "))
c = int(input("Digite o segundo número: "))

if b > c:
    print("O primeiro número é maior")
if c > b:
    print("O segundo número é maior")

# else
# multa de 5R$ de acima de 80km/h

speed = float(input("Informe a velocidade: "))

if speed > 80:
    ticket = (speed - 80) * 5
    print(f"Você passou a {speed:.2f}km/h. Sua multa é de {ticket:.2f}")
else:
    print(f"Você passou a {speed:.2f}km/h")

# elif

d = int(input("Digite o primeiro número: "))
e = int(input("Digite o segundo número: "))

if d > e:
    print("O primeiro número é maior")
elif d < e:
    print("O segundo número é maior")
else:
    print("Os números são iguais")

# and/or
# print smaller and greater

number_one = int(input("Digite o primeiro número: "))
number_two = int(input("Digite o segundo número: "))
number_three = int(input("Digite o terceiro número: "))

if number_one > number_two and number_one > number_three:
    print("O primeiro número é o maior")
if number_two > number_one and number_two > number_three:
    print("O segundo número é o maior")
if number_three > number_one and number_three > number_two:
    print("O terceiro número é o maior")
if number_one < number_two and number_one < number_three:
    print("O primeiro número é o menor")
if number_two < number_one and number_two < number_three:
    print("O segundo número é o menor")
if number_three < number_one and number_three < number_two:
    print("O terceiro número é o menor")
else:
    print("Todos são iguais.")

# aumento de salário. se salário >1250, 10%; se menor, 15%

wage = float(input("Digite seu salário: "))

if wage > 1250.00:
    pay_raise = wage * 0.10
    print(f"Seu aumento é de R$ {pay_raise:.2f}.")
else:
    pay_raise = wage * 0.15
    print(f"Seu aumento é de R$ {pay_raise:.2f}.")

# idade do carro. retorna se é novo ou velho
from datetime import date
car_year = int(input("Digite o ano do seu carro: "))
print(f"car_year: {car_year}")
current_year = (date.today()).year
print(f"current_year: {current_year}")
car_age = current_year - car_year

if car_age >= 10:
    print(f"Seu carro tem {car_age} e é velho")
else:
    print(f"Seu carro tem {car_age} e é novo")
    

