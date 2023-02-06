hello = '| Шифр Цезаря |'
print('-' * len(hello), hello, '-' * len(hello), sep='\n')


# ===========Запрашиваемые у пользователя данные===========#


# Проверка запрашиваемых у пользователя данные
def checking_data_user(data):
    while True:
        if data.lower() in ['ш', 'рус', '1']:
            return True
        elif data.lower() in ['д', 'eng', '2']:
            return False
        else:
            print('Вы ввели некорректные данные! Попробуйте снова:')
            data = input()
            continue


# Направление: шифрование или дешифрование
def encryption_direction():
    direction = input('Направление: шифрование или дешифрование\nШ (1) / Д (2):')
    flag_direction = checking_data_user(direction)
    return flag_direction  # True - шифрование, False - дешифрование


# Язык алфавита: русский или английский
def encryption_language():
    language = input('Язык алфавита: русский или английский\nРус (1) / Eng (2):')
    flag_language = checking_data_user(language)  # True - русский, False - английский
    # Количество символов в алфавите
    if flag_language:   # True - русский
        number_symbols_alphabet = 32
    else:                       # False - английский
        number_symbols_alphabet = 26
    return number_symbols_alphabet  # Количество символов алфавита


# Проверка Шаг сдвига (со сдвигом вправо)
def step_shift_check():
    step = input('Шаг сдвига. Введите целое число:\n')
    while True:
        if step.isdigit():
            step = int(step)
            return step
        else:
            print('Вы ввели некорректные данные! Попробуйте снова:')
            step = input()
            continue


# ===================Процесс шифрования====================#


def encryption_process():
    # Запрашиваем у пользователя строку для шифрования
    string_to_encrypt = input('Введите текст:\n')
    if encryption_direction_:  # Направление: шифрование - True
        for symbol in string_to_encrypt:  # перебираем элементы строки s
            if symbol in ' ,.!#$%&*+-=?@^_':
                print(symbol, end='')
            else:
                position_ascii = ord(symbol)  # определяем позицию в ascii
                position_ascii_moved = position_ascii + step_shift  # сдвиг вправо
                # русский словарь
                if amount_symbols_alphabet == 32:
                    if 192 <= position_ascii <= 223 and position_ascii_moved > 223:
                        position_ascii_moved -= amount_symbols_alphabet
                    elif 224 <= position_ascii <= 255 and position_ascii_moved > 255:
                        position_ascii_moved -= amount_symbols_alphabet
                    print(chr(position_ascii_moved), end='')
                # английский словарь
                elif amount_symbols_alphabet == 26:
                    if 65 <= position_ascii <= 90 and position_ascii_moved > 90:
                        position_ascii_moved -= amount_symbols_alphabet
                    elif 97 <= position_ascii <= 122 and position_ascii_moved > 122:
                        position_ascii_moved -= amount_symbols_alphabet
                    print(chr(position_ascii_moved), end='')

    elif not encryption_direction_:  # дешифрование - False
        for symbol in string_to_encrypt:  # перебираем элементы строки s
            if symbol in ' ,.!#$%&*+-=?@^_':
                print(symbol, end='')
            else:
                position_ascii = ord(symbol)  # определяем позицию в ascii
                position_ascii_moved = position_ascii - step_shift  # сдвиг влево
                # русский словарь
                if amount_symbols_alphabet == 32:
                    if 192 <= position_ascii <= 223 and position_ascii_moved < 192:
                        position_ascii_moved += amount_symbols_alphabet
                    elif 224 <= position_ascii <= 255 and position_ascii_moved < 224:
                        position_ascii_moved += amount_symbols_alphabet
                    print(chr(position_ascii_moved), end='')
                # английский словарь
                elif amount_symbols_alphabet == 26:
                    if 65 <= position_ascii <= 90 and position_ascii_moved < 65:
                        position_ascii_moved += amount_symbols_alphabet
                    elif 97 <= position_ascii <= 122 and position_ascii_moved < 97:
                        position_ascii_moved += amount_symbols_alphabet
                    print(chr(position_ascii_moved), end='')


encryption_direction_ = encryption_direction()  # направление
amount_symbols_alphabet = encryption_language()  # количество символов в словаре
step_shift = step_shift_check()  # шаг сдвига

encryption_process()
