x = int(input("Введите число\n")) 
sum_negative = 0
sum_positive = 0 
for i in range(-x,x+2,1):
    print(" ",i)
  
    if (i >= 0):
        sum_positive += i
    else:
        sum_negative += i

print("sum_negative",sum_negative)
print("sum_positive",sum_positive)
