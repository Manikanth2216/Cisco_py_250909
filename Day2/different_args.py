def find_salaries_sum(first, second):
    return first + second 
#usage 
print(find_salaries_sum(1000,2000))
# print(find_salaries_sum(1000,2000, 3000)) #error

print(find_salaries_sum(second=2000, first=1000))
print(find_salaries_sum(first=2000, second=1000))

# 002 | variable parameters -> end of the params
# variable args is of type tuple  
def find_salaries_sum(first, second, *salaries):
    result = first + second 
    for salary in salaries:
        result += salary 
    return result 
#usage 
print(find_salaries_sum(1000,2000))
print(find_salaries_sum(1000,2000, 3000))
print(find_salaries_sum(1000,2000,3000,4000))

# 003 | many salaries min 2 salaries to find sum
# named (keywords) variable args -> args is of type dict   
def find_salaries_sum(first, second, **named_salaries):
    result = first + second 
    for keyword in named_salaries:
        result += named_salaries[keyword] 
    return result 

print(find_salaries_sum(first=1000,second=2000))
print(find_salaries_sum(first=1000,second=2000,third=3000))
print(find_salaries_sum(first=1000,second=2000,third=3000,fourth=4000))

# 004 | default args 
def find_salaries_sum(first, second, bonus=500):
    return (first + bonus) + (second + bonus)
#usage 
print(find_salaries_sum(1000,2000)) # 1000->first | 2000->second | 500->bonus == 1500 + 2500 = 4000
print(find_salaries_sum(1000,2000,100)) # 1000->first | 2000->second | 100->bonus == 1100 + 2100 = 3200