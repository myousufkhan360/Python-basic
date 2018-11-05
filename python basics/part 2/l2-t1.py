list_a = ['Animal A' , 'Animal B' , 'Animal C' ]
list_b = ['Plant A' , 'Plant B' , 'Plant C' ]
list_c = [4 , 10 ,6 , 24 , 18]

print("Animals" + str(list_a))
print("Plants" + str(list_b))
print("Numbers" + str(list_c))

print("Length of list_a = "+ str(len(list_a)))

list_d = list_a + list_b
print("Combines animals and plants" + str(list_d))

print("animals(2)" + str(list_a[2]))

list_b = 'Different plant'
print("plants(2) modified" +str(list_b[2]))


list_a.append('New animal')
print("Appended list_a" + str(list_a))

print(list_c)
print("Searching for number 24")
print(24 in list_c)

print("Searching for number 64")
print(64 in list_c)

print(list_c)
print("acess each element")
sum = 0

for n in list_c:
    sum = sum + n
print("sum = "+str(sum))

print("*************************************************")



print("Showing the animals partial [3:]")
print(list_a[3:])

print("Showing the animals partial [:5]")
print(list_a[:5])

print("show all animals")
print(list_a[:])

t_list = list_a[2:5]
print("Animal [2:5]")
print(t_list)

list_a.remove("Animal A")
list_a.remove("Animal B")

print("Removed Animal A and Animal B")
print(list_a)

print("Sorting numbers")
print(sorted(list_c))

name = "Yousuf"
home_phone = ['phone A' , 'phone B']
cell_phone = ['cell A' , 'cell B']
phone_data = [name , home_phone , cell_phone]
print(phone_data)
