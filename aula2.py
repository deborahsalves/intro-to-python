#type of variable
name = "Déborah"
typeof = type(name)
print(typeof)

#it also works nested
bool = True
print(type(bool))

# since not predetermine, py variable are dynamic
what_type = 1
print(type(what_type)) #returns int
what_type = 1.2
print(type(what_type)) #returns float

# logical operators
# not > reverses value
# and
# or

it_is = True
it_is_not = False
it_might_be = 1
if (it_is):
    print(f"is it? {not it_is}")
if (it_might_be or it_is_not):
    print("it is not")
if (it_might_be and it_is):
    print("it is")
else:
    print(f"{it_might_be}")

#.lenght

nome = "Déborah"
length = len(nome)
print(length)
idade = 35
#print(len(idade)) #throws error > int não tem len() 
array = [1, 2, 3]
print(len(array))

#printing
dinheiro = 13.5
# % - posição
print("%s tem %d anos e R$ %f" % (nome, idade, dinheiro))

#.format
print("{} tem {} anos e R$ {}" .format(nome, idade, dinheiro))
print("{:12} tem {:03} anos e R$ {:5.1f}" .format(nome, idade, dinheiro))
## interpolation (literal)
print(f"{nome} tem {idade} anos e R$ {dinheiro:0.2f}")

#slicing
sliced_name = nome[0:3]
print(sliced_name)
print(name[2:])

