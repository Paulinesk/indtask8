print("Введите число в десятичной системе счисления: ")
while True:
    try:
        n = int(input())
        break
    except ValueError:
        print("Вы должны ввести число, попробуйте снова.")
    
print("Введите систему счисления: ")
while True:
        try:
            base = int(input())
            break
        except ValueError:
            print("Системой счисления может быть только целое число.")
            
if (base < 0):
    print("Системой счисления может быть только неотрицательное число.")
else:
    pass
result = ''
if (n < 0):
    print("Данная программа переводит только неотрицательные числа.")
else:
    pass
while n > 0:
    result = str(n % base) + result
    n //= base
print(result)