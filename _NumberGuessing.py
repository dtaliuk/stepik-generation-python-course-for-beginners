from random import randint

hello = '| Добро пожаловать в числовую угадайку |'
print('-' * len(hello), hello, '-' * len(hello), sep='\n')


# генератор случайных чисел
def random_num_generator():
    while True:
        right_border_random_num = input('Введите максимальное число для игры:\n')
        if right_border_random_num.isdigit():
            right_border_random_num = int(right_border_random_num)
            super_str = 'Отлично! Диапазон угадываемых чисел от 1 до'
            print(super_str, right_border_random_num)
            print('_' * (len(super_str) + len(str(right_border_random_num))))
            return right_border_random_num
        else:
            print('Неверное значение параметра.', end=' ')
            continue


rand_num = randint(1, random_num_generator())


# Запрашиваем данные у пользователя
def request_data_from_the_user():
    while True:
        number = input('Введите целое число:\n')
        if is_valid(number) is True:
            return int(number)
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')
            continue


# Проверка корректности введенных данных
def is_valid(num):
    # Проверяем, соответствует ли число необходимым параметрам
    # if (True and True and True)
    return num.isdigit() and int(num) in range(1, 101)


# основной блок программы
# Сравнение введенного числа с рандомным
def comparing_number_with_random():
    num, count = 0, 1
    while num != rand_num:
        num = request_data_from_the_user()
        if num < rand_num:
            count += 1
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif num > rand_num:
            count += 1
            print('Ваше число больше загаданного, попробуйте еще разок')
    print('Вы угадали, поздравляем!')
    print('Число попыток:', count)


# Повторная игра
while True:
    comparing_number_with_random()
    replay = input('\nЖелаете сыграть снова?\nДа / Нет\n')
    if replay.lower() == 'да':
        rand_num = randint(1, random_num_generator())
        continue
    else:
        end_game = '| Спасибо, что играли в Числовую угадайку. Еще увидимся... |'
        print('-' * len(end_game), end_game, '-' * len(end_game), sep='\n')
        break
