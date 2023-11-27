a = 10 #int

b = 10.5 #float

c = "строка может быть любой" #str

d = [10, 50, 209, 876, "какая-то строка"] #массив
bag = ["apple", "pineapple", "orange"] #массив


print (a - b)

print (c[5:12]) #последовательность от одного элемента до другого

print (d[0:12]) #можно с массивами тоже
print (d[3:]) #с третьего и до конца 



for fruit in bag: 
     for bite in [0, 1, 2, 3, 4, 5]:
        print(fruit[2:]) #-1 это с конца

for fruit in bag: 
     for bite in range(len(fruit)):
        print(fruit[bite:]) #-1 это с конца
