#you can use range(total_items to limit a list length

list = []
for x in range(10):
    list.append(x)
print(list)

# .insert(index, added) really like splice? could I _delete_ an item?
list1 = [1,2,3,4]
list1.insert(-1, "") 
print(list1)
# it doesnt work, BUT it will bug with negative indexes haha
print(list1[-1])

# additionally, not a method, but:
list1 += [5]
print(list1)
# not a method but (from the ppt) works like the .extend method

# .index(element) = JS indexOf
at_what_index = list1.index(2);
print(f"at what index is the number 2 in list1? at {at_what_index}")

#.sort() > MUTATES the original array
list2 = [6, 9, 8, 7]
print(list2);

#does it take a callback?
list3 = [14, 12, 11, 10]
def greaterThan(first, second):
    first > second+2 
#list3.sort(greaterThan(first, second))
print(list3)
#it doesnt o.O at least not w those arg calls... 
def plusTwo(item):
    return item + 2
print(plusTwo(3))
print(plusTwo(1))
list3.sort(key=plusTwo);
print(list3)
#hmm this does. documentation says the callback must have a single argument 
# and return the comparison constant

#we got reverse, which sorts Z>A

list3.reverse()
print(list3)

#ahh here we go: removing items
#KEYWORD del list[index]

del list3[2];
print(list3)

#.pop(index) >> like del, but RETURNS the deleted element
poped = list3.pop(1)
print(f"poped: {poped} \nlist3: {list3}")

#.remove(item) >> removes the first instance of the item; returns ERROR if no match is found

list3.remove(10)
print(list3)
#list3.remove(15)

## COOL:
# STACKS are lists that you push/pop from the pop, w/out any indexes:
# the TOP of the stack is the last one > LIFO: last one in, first one out

stack = [0, 1, 2, 3]
print(stack)
stack.append(4)
print(stack)
stack_pop = stack.pop()
print(stack_pop)
print(stack)

# QUEUES are lists that you add new items at the end and recover the first item as the NEXT in a line

queue1 = ["first in line", 4, 5, 6]
print(queue1)
queue1.append("last in line")
print(queue1)
first_in_line = queue1.pop(0)
print(first_in_line)
print(queue1)

#and, finally!, filter and map B)
#filter(callback, array) 
list4 = [2, 4, 5, 6]
def evenNumber(number):
    return number % 2 == 0
filtered = filter(evenNumber, list4)
print(filtered)
#MIND YOU: the filter() will return a FILTER class, not a list/tupl
for item in filtered:
    print(item)
print(type(filtered))

#map(callback, array)

def cube(number):
    return number * number * number
list5 = [1, 2, 3]
mapped = map(cube, list5)
print(mapped)
#like filter(), map() will return a MAP class, not a list/tupl
for item in mapped:
    print(item)
print(type(mapped))