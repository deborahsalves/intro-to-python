# Using [:] to COPY is slicing from begin to end
# But you could just really slice

name = "joão"
print(name[0:3])
print(name[1:3])

#works for lists as weel

my_list = [1, 2, 3, 4]
print(my_list[0:3])

#you can use different data types within the same list
mixed_list = [1, "Déborah", False]
for i in mixed_list:
    print(f"Item: {i}")

# FOR..IN is meant to iterate through lists

for each_item in my_list:
    print(f"This item: {each_item}")

#to get a list's index, use [] and the index

another_list = [5, 6, 7, 8]
print(f"the second left to right is: {another_list[1]}")

#you can also count backwards, starting (last element) with -1

print(f"the second to last is: {another_list[-2]}")

# to add elements to a list, you can "push" with .append()
another_list.append("at the end")
print(another_list)
# you can "splice" with .insert(index, added)
another_list.insert(0, "at the beginning") 
print(another_list)
# and you can concatenate with .extend
to_concatenate = ["con", "ca", "te", "na", "te"]
another_list.extend(to_concatenate)
print(another_list)

# what about TUPLE? you can't mutate it, though it sorta works like a list

my_tuple = (2, "Salves", True)
for value in my_tuple:
    print(f"This value: {value}")

# this will throw an error
# my_tuple.append("at the end")
print(my_tuple)

# a DOCSTRING is NOT a comment (it's a docstring)
'''Hey, I'm a DOCSTRING'''
# Hey, nice to meet you, I'm a comment


#to define a funcion, use DEF keyword

def my_function(args):
    print(f"{args} + 1 = {args+1}")

my_function(3)