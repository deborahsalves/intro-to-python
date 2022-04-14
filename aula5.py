# repetitions
x = 1
while x <= 100:
    print(x)
    x += 1

move_forward = input("pressione Enter para seguir.")

# tabuada de 5

times_five = 0

while times_five <= 10:
    print(f"{times_five} * 5 = {times_five * 5}")
    times_five += 1

move_forward = input("pressione Enter para seguir.")

# or, using commas:

times_three = 0

while times_three <= 10:
    print(times_three, "* 3 =", (times_three * 3))
    times_three += 1

# relinquishing control :lol:
x = 0
times_what = int(input("Qual tabuada você quer ver? "))

while x <= 10:
    print(x, "*", times_what, "=", (x * times_what))
    x += 1

move_forward = input("pressione Enter para seguir.")

# 5.3 Faça um programa para escrever a contagem progressiva do lançamento de 
# um foguete.
# O programa deve imprimir 10, 9, 8...1, 0 e fogo! na tela.

countdown = 10

while (countdown >= 0):
    print(countdown)
    countdown -= 1
print("fogo!")

move_forward = input("pressione Enter para seguir.")

# Exercício 5.5 - Modifique o programa anterior para imprimir de 1 até o 
# número digitado pelo usuário, mas, dessa vez, apenas os números ímpares.

count = 1
count_end = int(input("Até quanto você quer contar os números ímpares? "))

while (count <= count_end):
    print(count)
    count += 2

move_forward = input("pressione Enter para seguir.")

# Reescreva o programa anterior para escrever os 
# 10 primeiros múltiplos de 3.
#positive :P

count = 0
count_end = 10

while (count <= count_end):
    print(count*3)
    count += 1

move_forward = input("pressione Enter para seguir.")

# Exercício_ 5.7 - Tabuada com valores iniciais e finais informados pelo usuário

times_what = int(input("Você quer a tabuada de qual número? "))
table_start = int(input("A partir de qual múltiplo você quer a tabuada? "))
current_line = table_start
table_end = int(input("Até qual múltiplo você quer a tabuada? "))

while (current_line >= table_start and current_line <= table_end):
    print(f"{current_line} * {times_what} = {current_line * times_what}")
    current_line += 1

move_forward = input("pressione Enter para seguir.")

# Exercício5.8_ Multiplicação com somas sucessivas
# Escreva um programa que leia dois números. Imprima o resultado da multiplicação 
# do primeiro pelo segundo.
# Utilize apenas os operadores de soma e subtração para calcular o resultado. 
# Lembre-se de que podemos entender
# a multiplicação de dois números como somas sucessivas de um deles.
# Assim, 4 × 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.

first_num = int(input("Digite um número inteiro positivo: "))
second_num = int(input("Digite outro número inteiro positivo: "))
counter = 0
print_string = f"{first_num}"

#coudnt use the repeat function :(
#print(print_string, repeat(second_num - 1))

while(counter < (second_num - 1)):
    print_string += f" + {first_num}"
    counter += 1
print(f"{print_string} = {first_num * second_num}")

move_forward = input("pressione Enter para seguir.")

# Exercício 05-09: Divisão por subtrações sucessivas
# Escreva um programa que leia dois números. Imprima a divisão inteira do 
# primeiro pelo segundo, assim como o 
# resto da divisão. Utilize apenas os operadores de soma e subtração para 
# calcular o resultado. Lembre-se de que 
# podemos entender o quociente da divisão de dois números como a quantidade 
# de vezes que podemos retirar o divisor do
# dividendo. Logo, 20 ÷ 4 = 5, uma vez que podemos subtrair 4 cinco vezes de 20.

divided = int(input("Qual número deseja dividir? "))
divisor = int(input("Por qual número será a divisão? "))
current_rest = divided
counter = 1

while (current_rest > 0):
    print(f"{counter}x: {current_rest} - {divisor} = {current_rest - divisor}.")
    current_rest -= divisor
    counter += 1
print(f"{divided} / {divisor} = {(divided / divisor):.0f}")

move_forward = input("pressione Enter para seguir.")

# Exercício5.10 - Aceitar respostas com letras maiúsculas ou minúsculas

# ****Acumuladores****************
# Escreva um programa que pergunte o depósito inicial e a taxa de juros 
# de uma poupança. 
# Exiba os valores mês a mês para os 24 primeiros meses. 
# Escreva o total ganho com juros no período.

initial_deposit = float(input("Valor do depósito inicial: "))
interest_rate = float(input("Qualo a taxa de juros mensal? "))
current_balance = initial_deposit
counter = 0

while(counter < 24):
    current_balance += current_balance * interest_rate/100
    print(f"Saldo no mês {counter+1}: R$ {current_balance:.2f}")
    counter += 1

move_forward = input("pressione Enter para seguir.")

# Exercício 05-12: Cálculo do juros de uma poupança com depósito 
# Altere o programa anterior de forma a perguntar também o valor depositado 
# mensalmente.
# Esse valor será depositado no início de cada mês, e você deve considerá-lo 
# para o cálculo de juros do mês seguinte.

initial_deposit = float(input("Qual o saldo inicial da conta? "))
monthly_increase = float(input("Qual o valor do depósito mensal? "))
interest_rate = float(input("Qual a taxa de rendimento? "))
current_balance = initial_deposit
counter = 0

while (counter < 24):
    current_balance += monthly_increase 
    current_balance += current_balance * interest_rate/100
    print(f"Saldo no mês {counter+1}: R$ {current_balance:.2f}")
    counter += 1

move_forward = input("pressione Enter para seguir.")

# Exercício 05-13: Cálculo do pagamento de uma dívida com pagamentos mensais
# Escreva um programa que pergunte o valor inicial de uma dívida e o juro mensal. 
# Pergunte também o valor mensal que será pago. Imprima o número de meses para 
# que a dívida seja paga, o total pago e o total de juros pago.

initial_debt = float(input("Qual o valor atual da dívida? "))
interest_rate = float(input("Qual o juro mensal? "))
monthly_amortization = float(input("Qual o valor mensal da parcela? "))
total_paid = 0
current_debt = initial_debt
counter = 0

#just so I dont run into a loop w fake numbers
if (monthly_amortization < current_debt * interest_rate):
    current_debt = 0
    print("You'll never end your debt and you've broken the app.")

while(current_debt > 0):
    counter += 1
    current_debt += current_debt * interest_rate/100
    if (current_debt < monthly_amortization):
        monthly_amortization = current_debt
    total_paid += monthly_amortization
    print(f"Mês {counter}: pago R$ {monthly_amortization:.2f} do saldo devedor de R$ {current_debt:.2f}")
    current_debt -= monthly_amortization

if (monthly_amortization < initial_debt * interest_rate):
    print("Nope. I've blocked you from breaking my app.")
else:
    print(f"Você levará {counter} meses para quitar sua dívida inicial de R$ {initial_debt:.2f}, e terá pago R$ {total_paid:.2f} ao final do contrato – ou seja, pagará R$ {total_paid - initial_debt:.2f} em juros.")

move_forward = input("pressione Enter para seguir.")

# Exercício5.14 Lendo números inteiros do teclado e parando quando zero é entrado
# Escreva um programa que leia números inteiros do teclado. O programa deve 
# ler os 
# números até que o usuário digite 0 (zero). No final da execução, exiba a 
# quantidade 
# de números digitados, assim como a soma e a média aritmética.

user_input = int(input("Digite um número inteiro: "))
input_counter = 0
input_sum = 0

while(user_input != 0):
    input_counter += 1
    input_sum += user_input
    user_input = user_input = int(input("Digite um número inteiro: "))

input_avg = input_sum / input_counter
print(f"Você digitou {input_counter} números inteiros maiores do que zero. Eles somam {input_sum} e a média deles é {input_avg:.2f}.")
