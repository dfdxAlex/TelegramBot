hi = 'Добро пожаловать в наш калькулятор'
print(hi)
a = int(input('Введите сторону A:'))
b = int(input('Введите сторону B:'))
s = a * b
print ("Площать прямоугольника: ", s)

with open('s.txt', 'w', encoding='utf-8') as file:
    file.write(hi)
    file.write('\r')
    file.write(str(a))
    file.write('\r')
    file.write(str(b))
    file.write('\r')
    file.write(str(s))

input('Нажмите любую кнопку для завершения программы')

# 6565032988:AAEzsed1fOAHkE5aHWJhOljkLn5_yqFooEM

# https://core.telegram.org/bots/api

