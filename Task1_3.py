x = str(input("Введите число трехзначное число, все цифры должны быть различны :\n"))
perm = []
length = len(x)
if (length!= 3):
    print("Введите трехзначное число!")
elif (length!= len(set(x))):
    print("Повторяющиеся цифры!")
for i in x:
    for j in x:
        for k in x:
            if (i != j and j !=k and i != k):
                perm.append(int(i+j+k))
print(perm)


        




