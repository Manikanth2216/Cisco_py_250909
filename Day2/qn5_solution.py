'''
Problem 5
Write a Python program that:

Accepts a sequence of numbers from the user.
Stores the numbers in a list and finds the maximum and minimum values.
Stores the results (list, max, min) in a file named minmax_data.txt.
Reads and prints the saved data from the file.

'''

lis=input('Enter the numbers : ').split()
maxi=max(lis)
mini=min(lis)

with open('minmax_data.txt', 'w') as writer:
    writer.write(f'List of numbers: {lis}\n')
    writer.write(f'Maximum in list: {maxi}\n')
    writer.write(f'Minimum in list: {mini}\n')

with open('minmax_data.txt', 'r') as reader:
    list_nums = reader.readline()
    list_max = reader.readline()
    list_min=reader.readline()
    print(list_nums)
    print(list_max)
    print(list_min) 