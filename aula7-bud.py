# # 5.15 Escreva um programa para controlar uma pequena máquina registradora. 
# # Você deve solicitar ao usuário que digite o código do produto e a quantidade 
# # comprada. 
# # Utilize a tabela de códigos a seguir para obter o preço de cada produto:
# # código | preço |
# # 1        0,50
# # 2        1,00
# # 3        4,00
# # 5        7,00
# # 9        8,00
# # O programa deve exibir o total das compras depois que o usuário digitar 0.
# # Qualquer outro códogo deve gerar a mensagem de erro "Código inválido".

# control_variable = 0
# current_product = True
# current_quantity = 0
# total = 0
# while (current_product != 0 and control_variable == 0):
#     current_product = int(input("Digite o código do produto: "))
#     if (current_product == 0):
#         subtotal = 0
#         control_variable = 1
#         break
#     elif (current_product == 1):
#         subtotal = 0.5
#     elif (current_product == 2):
#         subtotal = 1
#     elif (current_product == 3):
#         subtotal = 4
#     elif (current_product == 5):
#         subtotal = 7
#     elif (current_product == 9):
#         subtotal = 8
#     else:
#         print("Código inválido")
#         break
#     current_quantity = int(input("Digite a quantidade do produto: "))
#     total += subtotal * current_quantity
#     print(f"Subtotal: R$ {total}.")
# print(f"Total: R$ {total}.")


# # Exercício 5.22 Menu de operações matemáticas 
# # Escreva um programa que exiba uma lista de opções (menu): adição, subtração, 
# # divisão, multiplicação e sair.
# # Imprima a tabuada da operação escolhida.
# # Repita até que a opção saída seja escolhida.

# chosen_operation = int(input("Escolha a operação que deseja ou sair: \n1 - Adição \n2 - Subtração \n3 - Multiplicação \n4 - Divisão \n0 - SAIR \n"))
# if (chosen_operation == 1 or chosen_operation == 2 or chosen_operation == 3 or chosen_operation == 4 or chosen_operation == 0):
#     while (chosen_operation != 0):
#         if (chosen_operation == 1):
#             chosen_operation_symbol = "+"
#         elif (chosen_operation == 2):
#             chosen_operation_symbol = "-"
#         elif (chosen_operation == 3):
#             chosen_operation_symbol = "*"
#         elif (chosen_operation == 4):
#             chosen_operation_symbol = "/"
#         chosen_number = int(input("Escolha o número para realizar a operação: "))
#         count = 0
#         while (count < 10):
#             subtotal = 0
#             if (chosen_operation == 1):
#                 subtotal = chosen_number + (count+1)
#             elif (chosen_operation == 2):
#                 subtotal = chosen_number - (count+1)
#             elif (chosen_operation == 3):
#                 subtotal = chosen_number * (count+1)
#             elif (chosen_operation == 4):
#                 subtotal = chosen_number / (count+1)
#             print(f"{chosen_number} {chosen_operation_symbol} {count+1} = {subtotal:.2f}")
#             count += 1
#         chosen_operation = int(input("Escolha a operação que deseja ou sair: \n1 - Adição \n2 - Subtração \n3 - Multiplicação \n4 - Divisão \n0 - SAIR \n"))
        
# else:
#     print("Opção inválida.")

# # Exercício 6.1 - Cálculo da média com notas digitadas 
# grades = [0, 0, 0, 0]
# grade_sum = 0
# student = 0
# while (student < len(grades)):
#     grades[student] = float(input(f"Nota de alune {student}: "))
#     grade_sum += grades[student]
#     student += 1
# avg = grade_sum / student
# print(f"Média das notas: {avg:.2f}.")

# Exercício 6.2 - Faça um programa que leia duas listas e que gere uma 
# terceira com os elementos das duas primeiras.

list_one = []
list_two = []
counter = 0
while (counter < 3):
    list_one.insert(counter, int(input("Insira um elemento na lista 1: ")))
    counter += 1
counter = 0
while (counter < 3):
    list_two.insert(counter, int(input("Insira um elemento na lista 2: ")))
    counter += 1
print(f"Lista 1: {list_one}")
print(f"Lista 2: {list_two}")
#simple add operator
list_three_a = list_one + list_two
print(f"Lista 3 usando operator: {list_three_a}")
##ISSO BOTA NO MESMO SLOT
## THIS MUTATES LIST_ONE!!!
#list_three_c = list_one
## use [:] to copy
list_three_c = list_one[:]
for i in list_two:
    list_three_c.append(i)
print(f"Lista 3 usando for...in: {list_three_c}")
list_three_b = list_one[:]
## SAME HERE
list_three_b.extend(list_two)
print(f"Lista 3 usando extend(): {list_three_b}")

