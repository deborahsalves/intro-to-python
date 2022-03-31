#Exercício 3.7 - Faça um programa que peça dois números inteiros. 
# Imprima a soma na tela.

a = int(input("Digite um número inteiro: "))
b = int(input("Digite outro número inteiro: "))

result = a + b

print(f"A soma de {a} com {b} resulta em {result}.")

#Exercício 3.8 - Escreva um programa que leia um valor em metros e 
# exiba convertido em milimetros

move_forward = input("Pressione uma tecla para prosseguir.")

metro = int(input("Informe uma medida em metros: "))

milimetro = metro * 1000

print(f"Convertido, {metro}m são {milimetro:.0f}mm.")

move_forward

#Excercício 3.9 - Escreva um programa que leia a quantidade de dias, horas, minutos
# e segundos do usuário. Calcule o total em segundos.

days = int(input("Informe o número de dias: "))
hours = int(input("Informe o número de horas: "))
minutes = int(input("Informe o número de minutos: "))
seconds = int(input("Informe o número de segundos: "))

days_in_seconds = (days * 86400)
hours_in_seconds = (hours * 3600)
minutes_in_seconds = (minutes * 60)
sum_of_time = days_in_seconds + hours_in_seconds + minutes_in_seconds + seconds

print(f"{days} dia(s), {hours} hora(s), {minutes} minuto(s) e {seconds} segundo(s) somam {sum_of_time} segundos.")

# def is_plural(arg, original_str):
#     return original_str + 's' if (arg > 1) else original_str

# print(f"{days} {is_plural(days, 'dia')} somam {days_in_seconds} segundos," \
#     f"\n{hours} {is_plural(hours, 'hora')} somam {hours_in_seconds} segundos," \
#     f"\n{minutes} {is_plural(minutes, 'minuto')} somam {minutes_in_seconds} segundos." \
#     f"\nEntão {days} {is_plural(days, 'dia')}, {hours} {is_plural(hours, 'hora')}, " \
#     f"{minutes} {is_plural(minutes, 'minuto')} e {seconds} {is_plural(seconds, 'segundo')} " \
#     f"somam {sum_of_time} {is_plural(sum_of_time, 'segundo')}.")

move_forward

#Exercício 3.11 - Faça um programa que solicite o preço de uma mercadoria
# e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.

price = float(input("Informe o preço: "))
perc_discount = float(input("Informe o desconto: "))
float_discount = perc_discount / 100

discounted_price = price - (price * float_discount)

print(f"O produto sai de {price:.2f} por {discounted_price:.2f} com o desconto de {perc_discount:.0f}%.")

move_forward

#Exercício 3.12 - Escreva um programa que calcule o tempo de uma viagem de carro.
#Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

distance = float(input("Informe quantos km até o destino: "))
avg_speed = int(input("Informe a velocidade média em km/h que você dirige: "))

eta = distance / avg_speed

print(f"Você deve levar {eta:.2f} hora(s) para percorrer {distance:.0f}km a {avg_speed}km/h.")

# import math
# if (math.floor(eta) == eta):
#     print(f"Você deve levar {eta:.0f} hora(s) para percorrer {distance:.0f}km a {avg_speed}km/h.")
# else:
#     hours_in_eta = math.floor(eta)
#     minutes_in_decimal = eta - hours_in_eta
#     minutes_in_eta = minutes_in_decimal * 60

#     print(f"hours_in_eta: {hours_in_eta} \nminutes_in_decimal: {minutes_in_decimal} \nminutes_in_eta: {minutes_in_eta}")
#     print(f"Você deve levar {hours_in_eta:.0f}h{minutes_in_eta:.0f} hora(s) para percorrer {distance:.0f}km a {avg_speed}km/h.")

# Exercícios extras
# 1. Construa um programa no qual um usuário informe a sua 
# estatura em metros e o programa converta-a para centímetros.

in_meters = float(input("Informe sua altura em metros: "))
in_centimeters = in_meters * 100.00

print(f"Em metros, você mede {in_meters:.2f}m. Em centímetros, você mede {in_centimeters:.0f}cm.")

move_forward

# 2. Construa um programa que receba do usuário a variação do 
# deslocamento de um objeto (em metros) e a variação do tempo percorrido (em segundo). Ao fim, o programa deve calcular a 
# velocidade média, em m/s, do objeto

delta_meters = float(input("Informe a variação do deslocamento de um objeto (em metros): "))
delta_time = float(input("Informe a variação do tempo percorrido (em segundos): "))

avg_speed_ms = delta_meters / delta_time

print(f"Delta d = {delta_meters:.2f}m. \nDelta t = {delta_time:.2f}s. \nVelocidade média: {avg_speed_ms:.2f}m/s")

# list or tuple? let vs const

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
print(thistuple[0])

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
print(thislist[0])

move_forward
