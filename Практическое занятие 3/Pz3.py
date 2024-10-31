from ConsistentFunc import CoderFunc as coder
from ShannonFanoFunc import ShannonFano as Fano
from prettytable import PrettyTable

# Исходная фраза
phrase = 'Информация и информационные технологии в технических системах'
phrase = phrase.lower()

# Использование метода Шеннона-Фано
fano = Fano(phrase)
fano.count_sym_all()
fano.calculate_ver()
fano.numer_syms(fano.syms)

# Использование метода последовательного кодирования
print(f'Исходная строка: {phrase}\n\nРезультат:', coder.encoder(phrase, fano.syms))

# Проверка кодирования текста при помощи декодирования
decode_phrase = coder.decoder(phrase, fano.syms)
print('\nДекодированная строка:', decode_phrase)
print('Сравнение строк:', decode_phrase == phrase)

print('\n---\n')
# Создание таблицы вероятности появления каждой из букв
# Указываем заголовки страницы
head = head = ['Буква', 'Вероятность', 'Бин код']
# Создаём объект таблицы
table = PrettyTable(head)
for sym in fano.syms:
    # Сборка таблицы
    table.add_row([sym.key, sym.ver, sym.bincode])

print(table)