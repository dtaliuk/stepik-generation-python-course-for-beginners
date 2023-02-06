from random import choice

answer = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом', 'Мне кажется '
                                                                                                        '- да',
          'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да', 'Пока неясно, попробуй снова',
          'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать', 'Сконцентрируйся и спроси опять',
          'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет', 'Перспективы не очень хорошие',
          'Весьма сомнительно']

user_greeting = '| Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос |'
print('-' * len(user_greeting), user_greeting, '-' * len(user_greeting), sep='\n')


user_name = input('- Как я могу к Вам обращаться?\n')
print('- Приветствую,', user_name.capitalize())


# Основной цикл программы
while True:
    user_question = input(f'- {user_name.capitalize()}, какой вопрос тебя тревожит?\n')
    print(f'- {choice(answer)}')
    print('Может быть хочешь еще что-нибудь узнать? Твоя судьба у меня на ладони.')
    othe_question = input('Да (Y) / Нет (N):')
    if othe_question.lower() in ['да', 'y']:
        continue
    elif othe_question.lower() in ['нет', 'n']:
        see_you = '| Возвращайся если возникнут вопросы! |'
        print('-' * len(see_you), see_you, '-' * len(see_you), sep='\n')
        break
    else:
        while True:
            print('Нерешительный ответ. Всё-таки будешь спрашивать или нет?')
            clarifying_question = input('Ну же, Да или Нет?')
            if clarifying_question in ['да', 'y']:
                break
            elif clarifying_question.lower() in ['нет', 'n']:
                see_you = '| Возвращайся если возникнут вопросы! |'
                print('-' * len(see_you), see_you, '-' * len(see_you), sep='\n')
                break
            else:
                continue
