"""number = [5,9,10,25,45,7,6,9]
first= number[0]
for index in number:
    if index > first:
      first = index
    
print (first)"""

string ="xxx"
string = list(string)
string.append('X')
print(string)
string = "".join(string)
print(string)


list_duplicate = [1,8,9,4,3,7,1,9,9]
list_fix = []

for item in list_duplicate:
    
    if item not in list_fix:
        list_fix.append(item)

print(list_fix)

    
# tuple
numbers= (1,2,3) #  (tipo de list) no modifica los valores
print(numbers.index(3))

# unpaking

cordinates = (1,2,3)
x=cordinates[0]
y=cordinates[1]     # egual
z=cordinates[2]

x, y, z = cordinates   # egual


