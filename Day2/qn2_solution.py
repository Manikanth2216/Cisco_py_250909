line=input('Enter line of integers : ')
lis=[int(num) for num in line.split()]
Sum = sum(lis)
Average = sum(lis)/len(lis)
print(Sum)
print(Average)

with open('Integers_sum_average.txt', 'w') as writer:
    writer.write(f'List: {lis}\n')
    writer.write(f'Sum: {Sum}\n')
    writer.write(f'Average: {Average}')

with open('Integers_sum_average.txt','r') as reader:
    line_list=reader.readline()
    line_sum=reader.readline()
    line_avg=reader.readline()
    print(line_list)
    print(line_sum)
    print(line_avg)