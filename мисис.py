'''
print(1)
x = int(input('Введите возраст'))
if x > 14:
    print('Добро пожаловать!')
if x == 14:
    print('Вам 14 лет! Поздравляю!')
if x < 14:
    print('Вам ещё рано!55')

secret = 'n$1~f^1}Om1eaN}'
x = input('Введите пароль:')
if x == secret:
    print('Доступ разрешен!') 
else: 
    print('Неверный пароль!')

symbol = input("Введите символ: ")
if symbol.isalpha():
    print("Это буква")
elif symbol.isdigit():
    print("Это цифра")
else:
    print("Это не буква и не цифра")

x = int(input('Введите стоимость товара'))
if x > 1000:
    p = 0.1 * x
    print(x - p)
if x > 500:
    p = 0.05 * x
    print(x - p)
else:
    print(x)

print(2)
summ = 0
for i in range(5):
    x = int(input('Введите число'))
    summ += x
print(summ)

fac = 1
x = int(input('Введите число'))
for i in range(1, x+1):
    fac *= i

print(fac)

count = 0
x = int(input('Введите число'))
for i in range(1, x+1):
    if x % i == 0:
        count += 1

if count <= 2:
    print('Простое')
else:
    print('Не простое')


word = input()
vowels = 0 #гласные
for letter in word:
    if letter.isalpha():
        if letter.lower() in 'aeiouyауоыиэяюёе':
            vowels += 1
            
 
print(vowels)

print(3)
def check_password(pas): 
    l_let = 'qwertyuiopasdfghjklzxcvbnm' 
    u_let = l_let.upper() 
    digits = '1234567890' 
    length_flag = len(pas) >= 8  
    l_let_flag, u_let_flag, digits_flag = False, False, False 
    for i in pas: 
        if i in l_let: 
            l_let_flag = True 
        if i in u_let: 
            u_let_flag = True 
        if i in digits: 
            digits_flag = True 
    return True if (length_flag and l_let_flag and u_let_flag and digits_flag) else False
'''
def print_average(arr):
    summa = 0
    for i in range(len(arr)):
        summa+=arr[i]
    srednee=summa/len(arr)
    return srednee
print(print_average([3, 4, 5, 6]))

