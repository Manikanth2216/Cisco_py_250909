lis=input("Enter the names seperated by spaces :").split(',')
lis.sort()
tup = tuple(lis)
print('List of names', lis)
print('Tuple of names', tup)

with open('names_data.txt', 'w') as writer:
    writer.write(f'List of names: {lis}\n')
    writer.write(f'Tuple of names: {tup}')

with open('names_data.txt', 'r') as reader:
    list_names = reader.readline()
    tuple_names = reader.readline()
    print(list_names)
    print(tuple_names)