#functions
def my_sum(num1, num2):
    return num1 + num2
num1 = int(input("Insira o primeiro número a adicionar: "))
num2 = int(input("Insira o segundo número a adicionar: "))
print(f"{num1} + {num2} = {my_sum(num1, num2)}")

def is_even(num):
    if num % 2 == 0:
        return "even"
    else:
        return "not even"
def is_uneven(num):
    if num % 2 != 0:
        return "uneven"
    else:
        return "not uneven"
def is_or_not_even(num):
    print(is_even(num))
    print(is_uneven(num))
num3 = int(input("Insira um número para ver se é par ou ímpar: "))
is_or_not_even(num3)

## but we've got built-in methods for that

list1 = [1, 2, 3, 4]
print(f"A soma é {sum(list1)}")

print(f"O menor é o {min(list1)} \ne o maior é o {max(list1)}")

global_var = 5
def change_and_print():
    global global_var
    global_var = 3
    print(f"Dentro da função, global_var foi mudada para {global_var}")
print(f"FORA da função, global_var é {global_var}")
change_and_print()
print(f"Só que a função muda a global: agora fora de novo, global_var segue mudada para {global_var}")

#what if I don't call the keyword global within the function?

another_global = 5
print(f"Here's another global variable: {another_global}")

def change_again_with_reassigning():
    another_global = 3
    print(f"What's returned when global_var is reassigned? {another_global}")
change_again_with_reassigning()

#if you're reassining, it will work. but if you try to modify it, it wont

def change_again_with_operation():
    global another_global
    another_global += 3
    print(f"To make operations, you need to use the 'global' keyword: {another_global}")
change_again_with_operation()

#recursive function

#def fatorial(num):
 #   if num == 1 or num == 0:
  #      return 

#data validation
num4 = int(input("Entre com um número até 5: "))
def validate(num):
    return True if num <= 5 else False
validated = validate(num4)

#BTW, o ternário não vai retornar direto :(
#print(f"Você digitou {num4}") if {validated} else print(f"Seu número não é até 5") 
print(f"Você digitou {num4} e deu {validated}") 

#lambda function = annonymous function, but single line only

annon = lambda arg: arg if arg <= 5 else "Wrong!"
num5 = int(input("Let's go again: Entre com um número até 5: "))
print(f"Será que deu bom? {annon(num5)}")

# and you've got try/catch, except it's try/except, because you can return based on the error:
folks = ['Nic', 'Pri', 'Deh']
for attempts in range(3):
    try:
        print("Com except")
        i = int(input("Digite o índice para pessoa: 0-Nic, 1-Pri, 2-Deh: "))
        print(folks[i])
    except ValueError:
        print("Você tem que digitar algum número!")
    except IndexError:
        print("Valor errado. Tem ser de -3 a 2:")

#MIND YOU: it will NOT try again!
#HERE, though, you used the input() INSIDE a for..in PRECISELY to give your user a few attempts

#and you also can use the default error messages, without having to anticipate possible errors:
for attempt in range(2):
    try:
        print("Com Exception")
        i = int(input("Try again: 0-Nic, 1-Pri, 2-Deh: "))
        print(folks[i])
    except Exception as name_it_what_you_want:
        print(f"Algo de errado aconteceu: {name_it_what_you_want}")

#and you CAN combine both:

for attempt in range(2):
    try:
        print(f"Combinando except e Exception")
        print(f"attempt #{attempt}")
        i = int(input("Try once again: 0-Nic, 1-Pri, 2-Deh: "))
        print(folks[i])
    except IndexError:
        print("Valor errado. Tem ser de -3 a 2:")
    except Exception as name_it_what_you_want:
        print(f"Algo de errado aconteceu: {name_it_what_you_want}")

#it just handles the thing with the Exception, it aint elif + else, it's just straight to else :(

#you can personalize the message, though:

for attempt in range(2):
    try:
        print(f"Com raise")
        i = int(input("Try once more: 0-Nic, 1-Pri, 2-Deh: "))
        print(folks[i])
#    except Exception:
# SOMETHING IS WRONG FROM HERE ON THOUGH :(
#        raise IndexError("Valor errado. Tem ser de -3 a 2:")
#        raise ValueError("Você tem que digitar algum número!")
#        print(f"Algo de errado aconteceu: {name_it_what_you_want}")

# what you CAN do is try again even if the validation fails
# you use the keyword FINALLY

for attempt in range(2):
    try:
        print("Com finally")
        i = int(input("Try yet another time: 0-Nic, 1-Pri, 2-Deh: "))
        print(folks[i])
    except IndexError:
        print("Valor errado. Tem ser de -3 a 2:")
    finally:
        print(f"This will run after try and/or except: tentativa {attempt + 1}")

# MODULE: import some other file
# MIND YOU though, that it'll RUN, top to bottom o.O
import aula11module

name = input("Digite seu nome para usar a função importada via módulo: ")

#this wont work: imported_function(name)
#the correct way, to avoid clashing of names, is calling the file.fn

aula11module.imported_function(name)

### READ SLIDES FROM 41 THROUGH 58