def find_min(salaries):
    mini=salaries[0]
    for sal in salaries:
        if sal<mini:
            mini=sal
    return mini

def find_max(salaries):
    maxi=salaries[0]
    for sal in salaries:
        if sal>maxi:
            maxi=sal
    return maxi

def find_total(salaries):
    total=0
    for sal in salaries:
        total+=sal
    return total

salaries=[7000,4000,5000,2000,3000]
print(find_min(salaries))
print(find_max(salaries))
print(find_total(salaries))