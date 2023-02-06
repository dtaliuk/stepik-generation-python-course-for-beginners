print('Итоговые проекты курса', '"Поколение Python": курс для начинающих', sep='\n')


while True:
	print('\nКакую программу хотите запустить? ')
	print("""1. Шифр Цезаря
2. Магический шар
3. Генератор безопасных паролей
4. Числовая угадайка
5. Угадайка слов
0. Выход """)

	questions = int(input('-> '))
	print()

	if questions == 0:
		break
	elif questions == 1:
		import _CaesarCipher
	elif questions == 2:
		import _MagicBall8
	elif questions == 3:
		import _SecurePasswordGenerator
	elif questions == 4:
		import _NumberGuessing
	elif questions == 5:
 		import _WordGuessing
