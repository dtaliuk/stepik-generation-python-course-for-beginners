import random

hello = '| Генератор безопасных паролей  |'
print('-' * len(hello), hello, '-' * len(hello), sep='\n')

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = '!#$%&*+-=?@^_'

chars = ''


''' Считывание пользовательских данных'''
# Количество паролей для генерации
while True:
    num_of_pass_to_generate = input('Введите количество паролей для генерации:\n')
    if num_of_pass_to_generate.isdigit():
        num_of_pass_to_generate = int(num_of_pass_to_generate)
        break
    else:
        print('Вы ввели некорректные данные. Попробуйте снова')
        continue

# Длина одного пароля
while True:
    length_of_one_pass = input('Какая длина пароля должна быть:\n')
    if length_of_one_pass.isdigit():
        length_of_one_pass = int(length_of_one_pass)
        break
    else:
        print('Вы ввели некорректные данные. Попробуйте снова')
        continue


# Проверка данных пользователя
def checking_data_user(data):
    while True:
        if data.lower() in ['да', 'y']:
            return True
        elif data.lower() in ['нет', 'n']:
            return False
        else:
            print('Вы ввели некорректные данные. Попробуйте снова')
            data = input('Да(Y) / Нет (N):')
            continue


# Включать ли: цифры, прописные буквы, строчные буквы, символы
# Исключать ли неоднозначные символы "il1Lo0O"
def reading_user_data():
    include_numbers = input('Включать ли цифры?\nДа(Y) / Нет (N):')  # [0]
    flag_num = checking_data_user(include_numbers)
    include_lower_letters = input('Включать ли прописные буквы?\nДа(Y) / Нет (N):')  # [1]
    flag_lower = checking_data_user(include_lower_letters)
    include_upper_letters = input('Включать ли строчные буквы?\nДа(Y) / Нет (N):')  # [2]
    flag_upper = checking_data_user(include_upper_letters)
    include_symbols = input('Включать ли символы?\nДа(Y) / Нет (N):')  # [3]
    flag_symbols = checking_data_user(include_symbols)
    include_il1Lo0O = input('Исключать ли неоднозначные символы "il1Lo0O"?\nДа(Y) / Нет (N):')  # [4]
    flag_il1Lo0O = checking_data_user(include_il1Lo0O)
    return [flag_num, flag_lower, flag_upper, flag_symbols, flag_il1Lo0O]


# список соответствия (список, какие буквы включать, а какие нет)
accord_list = reading_user_data()


'''Настройка генерируемых паролей'''


# Настройка генерируемых паролей
def gen_pass_settings():
    global chars
    if accord_list[0] is True:
        chars += digits
    if accord_list[1] is True:
        chars += uppercase_letters
    if accord_list[2] is True:
        chars += lowercase_letters
    if accord_list[3] is True:
        chars += punctuation
    if accord_list[4]:
        if len(chars) > 0:
            for c in 'il1Lo0O':
                chars = chars.replace(c, '')
        else:
            empty_list = 'empty character list'
            return empty_list
    elif not accord_list[4]:
        empty_list = 'empty character list'
        return empty_list
    return chars


'''Генерации пароля'''


def generate_password():
    if gen_pass_settings() == 'empty character list':
        print('\nВы исключили все допустимые символы для пароля.')
        try_again = input('Желаете попробовать снова?\nДа(Y) / Нет (N):')
        flag_try_again = checking_data_user(try_again)
        if flag_try_again:
            gen_pass_settings()
        else:
            leave = '| Спасибо, что воспользовались нашими услугами |'
            return print('-' * len(leave), leave, '-' * len(leave), sep='\n')

    else:
        for _ in range(num_of_pass_to_generate):
            random_generated_password = ''
            for _ in range(length_of_one_pass):
                pass_symbol = random.choice(gen_pass_settings())
                random_generated_password += pass_symbol
            print(random_generated_password)


generate_password()
