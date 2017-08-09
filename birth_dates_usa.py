
f = open('births.csv', 'r')
birth_read = f.read()
print(birth_read)

first_parse = birth_read.split('\n')
print(first_parse[:5])

birth_list = []
for row in first_parse:
    second_parse = row.split(',')
    birth_list.append(second_parse)
birth_list = birth_list[1:]

print(birth_list[:5])

birth_list_count = []

for i in birth_list:
    day = i[3]
    birth_count = i[4]
    day_count = [day, birth_count]
    
    birth_list_count.append(day_count)
    
print(birth_list_count)

births = {}

for i in birth_list_count:
    key = i[0]
    val = int(i[1])
    if key in births:
        births[key] += val
    else:
        births[key] = val
        
print(births)


# Calculating the number of births by day






