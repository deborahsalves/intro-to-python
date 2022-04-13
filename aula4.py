# if you wanna complete a number w zeros to the left

a = 2.2

print(f"Com zeros à esquerda: {a:04.2f}") #will print 0002.20

# if else
# 4.1 - Lê dois valores e mostra qual é o maior
# No Python a estrutura de decisão é o if

b = int(input("Digite o primeiro número: "))
c = int(input("Digite o segundo número: "))

if b > c:
    print("O primeiro número é maior")
if c > b:
    print("O segundo número é maior")

# else
# 4.2 Escreva um programa que pergunte a velocidadedo carro de um usuário.
# Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado.
# Nesse caso exiba o valor da multa, cobrando R$ 5,00 por km acima de 80 km/h.

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
# 4.3 Escreva um programa que leia três números e que imprima o maior e o menor.

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

# 4.4 Escreva um programa que pergunte o salário do funcionário e calcule o 
# valor do aumento. Para salários superiores a R$ 1.250,00, calcule um aumento 
# de 10%. Para os inferiores ou iguais de 15%.

wage = float(input("Digite seu salário: "))

if wage > 1250.00:
    pay_raise = wage * 0.10
    print(f"Seu aumento é de R$ {pay_raise:.2f}.")
else:
    pay_raise = wage * 0.15
    print(f"Seu aumento é de R$ {pay_raise:.2f}.")

# 4.5 Escreva um programa que solicite a idade do carro e retorne se é novo 
# ou velho. 

from datetime import date
car_year = int(input("Digite o ano do seu carro: "))
current_year = (date.today()).year
car_age = current_year - car_year

if car_age >= 10:
    print(f"Seu carro tem {car_age} e é velho")
else:
    print(f"Seu carro tem {car_age} e é novo")
    
# Exercício 4.6 - Escreva um programa que pergunte a distância que um 
# passageiro deseja percorrer em km. Calcule o preço da passagem cobrando 
# R$ 0,50 por km para viagens até de 200 km, e R$ 0,45 para viagens mais longas.

distance = float(input("Quantos quilômetros deseja percorrer? "))

if distance <= 200:
    price = distance * 0.5
    print(f"Sua viagem custará R$ {price:.2f}.")
else:
    price = distance * 0.45
    print(f"Sua viagem custará R$ {price:.2f}.")

# 4.7 Estruturas aninhadas 
# Escreva um programa que solicite a categoria de um produto e de acordo com 
# a categoria digitada mostre o preço respectivo do produto.

category = int(input("Qual a categoria do produto que deseja consultar? 1 Bebidas; 2 Lanches; 3 Sobremesas "))

if category != 1 and category != 2 and category != 3:
    print("Opção inválida. A categoria não existe.")
else:
    if category == 1:
        price = 2
        print(f"Preço: R$ {price:.2f}.")
    if category == 2:
        price = 4
        print(f"Preço: R$ {price:.2f}.")
    if category == 3:
        price = 6
        print(f"Preço: R$ {price:.2f}.")

# 4.8 Escreva um programa que leia dois números e que pergunte qual operação você 
# deseja realizar.
# Você deve poder calcular a soma (+), subritração(-), multiplicação (*) e 
# divisão(/).
# Exiba o resultado da operação solicitada.

first_number = float(input("Digite o primeiro número: "))
second_number = float(input("Digite o segundo número: "))
operator = int(input("Que operação deseja realizar com os números? 1 soma | 2 subtração | 3 multiplicação | 4 divisão "))

if operator != 1 and operator != 2 and operator != 3 and operator != 4:
    print(f"Operação inválida.")
elif operator == 4 and second_number == 0:
    print(f"Seu segundo número é 0. Não é possível fazer divisão por zero.")
else:
    if operator == 1:
        result = first_number + second_number
        print(f"{first_number:.2f} + {second_number:.2f} = {result:.2f}")
    if operator == 2:
        result = first_number - second_number
        print(f"{first_number:.2f} - {second_number:.2f} = {result:.2f}")
    if operator == 3:
        result = first_number * second_number
        print(f"{first_number:.2f} * {second_number:.2f} = {result:.2f}")
    if operator == 4:
        result = first_number / second_number
        print(f"{first_number:.2f} / {second_number:.2f} = {result:.2f}")

# Exercício 4.9 Escreva um programa para aprovar o empréstimo bancário para 
# compra de uma casa.
# O programa deve perguntar o valor da casa a comprar, o salário e a quantidade 
# de anos a pagar.
# O valor da prestação mensal não pode ser superior a 30% do salário. 
# Calcule o valor da prestação como sendo o valor da casa a comprar dividido 
# pelo número de meses a pagar.

client_wage = float(input("Qual seu salário atual? "))
house_price = int(input("Quanto custa o imóvel que deseja comprar? "))
mortgage_years = int(input("Em quantos anos deseja quitar a compra? "))
mortgage_months = mortgage_years * 12
monthly_payment = house_price / mortgage_months
limit = client_wage * 3/10

if monthly_payment > limit:
    print(f"Infelizmente seu financiamento foi negado. Sua prestação máxima é de R$ {limit:.2f}, porém as informações fornecidas resultaram em uma prestação de R$ {monthly_payment:.2f}.")
else:
    print(f"Seu financiamento foi aprovado! Sua prestação será de R$ {monthly_payment:.2f}.")
