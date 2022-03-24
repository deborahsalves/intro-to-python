print("hello world")
print(11//3)
print(11%3)

# hash to comment
# atalho do teclado pro comment: ctrl + ;
# e o undo do comment é o mesmo atalho
"""pra passar instruções pra outres devs, usa três aspas duplas"""
# só cuida que ainda vai ser executado, mas não vai pro front :thinking:

a = 2
b = a + 1
print(a + b)
print(2 + 5)

# case sensitive
default_variable_fn_or_method_case = "snake_case"
defaultClassCase = "camelCase"

print(default_variable_fn_or_method_case)
print(defaultClassCase)

if b // a >= 1:
    print(b)
else:
    print(a)

salario = 2200
aumento = 2.5

PERCENT = 100

salario_final = salario + (salario * aumento / PERCENT)
print(salario_final)

nome = "Déborah"
sobrenome = "Salves"

#concat
print(nome + " " + sobrenome)
print(nome, sobrenome)

# Paga imposto?
salario = int(input("Digite seu salário: "))
imposto = True #capital pra BOOLEAN

if salario > 1900 and salario < 2800:
    valor_imposto = salario * (7/100)
    # print("Você deve pagar um imposto? {imposto}. O valor do imposto é de {valor_imposto}")
elif salario >= 2800 and salario < 3700:
    valor_imposto = salario * (15/100)
elif salario >= 3700 and salario < 4600:
    valor_imposto = salario * (15/100)
elif salario >= 4600:
    valor_imposto = salario * (15/100)
else:
    imposto = False
    valor_imposto = 0

print(f"Você deve pagar um imposto? {imposto}. O valor do imposto é de {valor_imposto}")

# Média de alune pra ver se foi aprovade

nota1 = 7
nota2 = 6
nota3 = 8
notas = [nota1, nota2, nota3]

media = (nota1 + nota2 + nota3) / 3
if media >= 7:
    aprovacao = True
else:
    aprovacao = False

print(f"E alune foi {'aprovado' if aprovacao else 'reprovado'}")

media2 = 0
counter = 0
for nota in notas:
    media2 += nota
    print(f"media2: {media2}")
    counter += 1
    print(f"counter: {counter}")

media2 = media2/counter
print(f"media2: {media2}")

aprovacao2 = True if media2 >= 7 else False

print(f"Você foi {'aprovado' if aprovacao2 else 'reprovado'}")


