#TUPLE
this_tuple = (1, 2, 3)
print(this_tuple)
this_tuple = this_tuple[0:2]
print(this_tuple)
print(this_tuple[0])

#DICTIONARY, sorta like an object
#mind you: KEY also ''

customer = {'name': 'Déborah', 'age': 35, 'pets': ['Bela', 'Trix', 'Fiona'], 'esposa': ('Lu')}
print(customer)
print(customer['name'])

customer_list = [customer, {'name': 'second customer', 'age': 'second age'}]
print(customer_list)
print(customer_list[1])
print(customer_list[1]['name'])

