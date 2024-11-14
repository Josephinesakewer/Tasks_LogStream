x = input("Введите число или exit для выхода ") 
while True:
    x = input("Введите число или exit для выхода\n") 
    if (x.isdigit()):
        length = len(x) 
        print(x,"len ",length)
       #continue
    elif x == 'exit':
        break
    else:
        print("Несоответствие типа данных ")
    



    
        
    





