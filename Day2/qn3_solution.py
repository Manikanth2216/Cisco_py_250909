sentence=input('Enter the sentence : ')
lis=sentence.split()
tup=tuple(word.upper() for word in lis)
with open('sentence_data.txt','w') as writer:
    writer.write(f'List: {lis}\n')
    writer.write(f'Tuple: {tup}')

with open('sentence_data.txt','r') as reader:
    line_list=reader.readline()
    line_tuple=reader.readline()
    print(line_list)
    print(line_tuple)