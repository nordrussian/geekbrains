# 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

a = 5
b = 3
print(a)
print(b)

o = input("Введите имя: ")
print('Привет' + o)

x = int(input("Введите переменную 1:"))
y = int(input("Введите переменную 2:"))
print(x)
print(y)

# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
n = int(input("Введите время в секундах: "))
sec = n% (24 * 3600)
hour = sec // 3600
sec %= 3600
min = sec // 60
sec %= 60
print(f'{hour}:{min}:{sec}')

# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
n = int(input("Введите число: "))
sum_n = f'{n}{n*2}{n*3}'
print(sum_n)

# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
n = int(input("Введите целое положительное число "))
max = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > max:
        max = n % 10
    if n > 9:
        continue
    else:
        print("Максимальное цифра в числе ", max)
        break

# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
revenue = int(input("Введите выручку фирмы: "))
costs = int(input("Введите издержки фирмы: "))
if revenue > costs:
    print("Фирма работает в плюс")
    percent = revenue / costs
    if percent > 1:
        print(f"Процент прибыли {percent}")
        worker = int(input("Введите кол-во сотрудников: "))
        worker_percent = percent / worker
        print(f"Процент прибыли на сотрудника {worker_percent}")
if revenue == costs:
    print("Фирма работает в ноль")
if revenue < costs:
    print("Фирма работает в убыток")

# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров. Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

a = int(input("Введите кол-во километров в первый день: "))
b = int(input("Введите желаемый результат: "))
days = 1
km = a
while km < b:
    a = a + 0.1
    days += 1
    km = days + a
print(f"Вы получите результат на {days} день")


