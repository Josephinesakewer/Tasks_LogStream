# Напишите программу, которая принимает от пользователя список 
# чисел и степень возведения этих чисел. 
# Выведите в консоль список этих чисел, 
# возведенных в степень, инициализируемую ранее.  
# В случае, если пользователь передаст строку в список, 
# то умножьте её на степень. 
# Дополнительно проверьте работу с отрицательными числами.

x = int(input("Введите количество элементов списке: "))
y = int(input("Введите степень возведения чисел: "))
z = list(input("Введите число: "))

l = []
for i in z:
    if len(z) <= x:
        if (i.isdigit()):
            num = int(i)
            l.append(num**y)
        if (type(i) == str):
            l.append(i*y)
print(" Оригинальный список: ",z)
print(l)

#for i in z:
    #if (x <= len(l)):
        #if (i.isdigit()):
            #l.append(i**y)
        #if (type(i) == str):
            #l.append(i*y)
#print(" Оригинальный список: ",z)
#print(l)