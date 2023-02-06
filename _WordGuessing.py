from random import choice

hello = '| Угадайка слов |'
print('-' * len(hello), hello, '-' * len(hello), sep='\n')

word_list = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'раз', 'работа', 'слово', 'место', 'лицо',
             'друг', 'глаз', 'вопрос', 'дом', 'сторона', 'страна', 'мир', 'случай', 'голова', 'ребенок', 'сила',
             'конец', 'вид', 'система', 'часть', 'город']


def get_word():
    """Функция, которая возвращает случайноей слово
       из списка word_list в верхнем регистре
    """
    random_word = choice(word_list).upper()
    return random_word


def display_hangman(tries):
    """Функция, возвращающая текущее состояние
       Принимает один аргумент tries - количество
       попыток угадывания слова
       Рисует виселицу с человечком
       и пишет, сколько попыток осталось
    """
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',
        # голова, торс, обе руки, одна нога
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        ''',
        # голова, торс, обе руки
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        ''',
        # голова, торс и одна рука
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        ''',
        # голова и торс
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',
        # голова
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
        # начальное состояние
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''
    ]
    return stages[tries]


def play(word):
    """В функции будет осуществляться основная
       логика игры. Функция play() принимает в
       качестве аргумента слово word, сгенерированное
       функцией get_word().
    """
    # строка, содержащая символы '_' на каждую букву задуманного слова
    word_completion = '_' * len(word)
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток

    print('Давайте играть в угадайку слов!')
    print(display_hangman(tries))
    print(word_completion)

    while tries > 0:
        word_input = input('Введите букву или слово целиком:\n').upper()

        # Защита от дурака
        if not word_input.isalpha():
            if len(word_input) > 1:
                print('Вы ввели некорректное слово, попробуйте снова.')
                continue
            else:
                print('Вы ввели символ, не являющийся буквой, попробуйте снова.')
                continue

        # проверка, если пользователь ввел СЛОВО
        elif len(word_input) > 1:
            if word_input == word:
                guessed = True
                break
            elif word_input in guessed_words:
                print('Вы уже вводили данное слово, попробуйте снова.')
                continue
            else:
                guessed_words.append(word_input)
                tries -= 1
                print(display_hangman(tries), f'Осталось попыток: {tries}', sep='\n')
                print(word_completion)
                continue

        # проверка, если пользователь ввел БУКВУ
        elif len(word_input) == 1:
            if word_input in guessed_letters:
                print('Вы уже вводили данную букву, попробуйте снова.')
                continue

            elif word_input in word:
                word_lst = list(word)
                completion_list = list(word_completion)
                while word_lst.count(word_input) > 0:
                    index_letter = word_lst.index(word_input)
                    completion_list[index_letter] = word_input
                    word_lst[index_letter] = '_'
                    word_completion = ''.join(completion_list)
                guessed_letters.append(word_input)
                print('Угадали!!! Вы еще ближе к спасению!\n', word_completion)

            else:
                guessed_letters.append(word_input)
                tries -= 1
                print(display_hangman(tries), f'Осталось попыток: {tries}', sep='\n')
                print(word_completion)
                continue

        if word_completion == word:
            guessed = True
            break

    if guessed is True:
        print('Поздравляем, вы угадали слово!')
        print('============ WIN =============')
    elif tries == 0:
        print(display_hangman(tries), '==== GAME OVER ====', sep='\n')
        print(f'Загаданное слово: {word}')


play(get_word())

while True:
    print('\nСыграть НОВУЮ ИГРУ?')
    restart = input('Да (Y) / Нет (N):')
    if restart.lower() in ['да', 'y']:
        play(get_word())
    else:
        print('==== До встречи ====')
        break
