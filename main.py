'''
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
 Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''


def mod(*args):
    try:
        poz_arg1 = int(input("Введите первое число "))
        poz_arg2 = int(input("Введите второе число "))
        res = poz_arg1 / poz_arg2
    except ValueError:
        return 'Ошиблись с вводом'
    except ZeroDivisionError:
        return "Вы не можете делить на ноль"
    return res
print(f'result  {mod()}')

#2

def my_func(name, surname, year, city, email, mobile):
    return ' '.join([name, surname, year, city, email, mobile])
print(my_func(surname='Shef',name='Andrey',year='1981',city='Moscow',email='online@ru',mobile='89036741111'))

#3

def my_func(x, y, z):
    arg = [x, y, z]
    my_numbers = []
    max_1 = max(arg)
    my_numbers.append(max_1)
    arg.remove(max_1)
    max_2 = max(arg)
    my_numbers.append(max_2)
    print(sum(my_numbers))
my_func(6, 4, 1)

#4

def my_func(x, y):
    return 1 / x ** abs(y)
print(my_func(3, -4))

#5

def my_sum ():
    sum_res = 0
    ex = False
    while ex == False:
        number = input('Введите число или q для выхода - ').split()

        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'й' :
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Текущяя сумма {sum_res}')
    print(f'Заключительная сумма {sum_res}')

my_sum()

#6

def int_func (*args):
    word = input("Ведите слова ")
    print(word.title())
    return
int_func()



