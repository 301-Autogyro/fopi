class Symbol():
    '''
    **Объект символа исходной строки**
        `key: str` - символ (буква)
        `value: int` - частота встречаемости символа
        `ver: float` - вероятность символа
        `bincode: str` - бинарный (двоичный) код символа
    '''

    def __init__(self, key: str, value: int, ver: float=0.0, bincode: str='') -> None:
        self.key = key # символ
        self.value = value # его количество
        self.ver = ver # вероятность
        self.bincode = bincode # код символа

class ShannonFano():
    '''
    ### Описание
    **Шеннона — Фано** — один из первых алгоритмов сжатия, который впервые сформулировали американские учёные Клод Шеннон и Роберт Фано.

    **Принцип работы:** алгоритм использует коды переменной длины: часто встречающийся символ кодируется кодом меньшей длины, редко встречающийся — кодом большей длины
     
    ### Методы (функции):
        - count_sym_all(phrase: str)
        - calculate_ver()
        - numer_syms(syms: list(Symbol))
    '''

    def __init__(self, phrase: str) -> None:
        self.phrase = phrase
        self.syms = list()
        self.count_sym = dict()

    def count_sym_all(self):
        '''
        Расчёт частоты встречаемости символа
        '''

        # Расчёт частот в исходной фразе
        be_syms = list()
        for sym in self.phrase: 
            if sym not in be_syms: 
                be_syms.append(sym)
                self.syms.append(Symbol(sym, self.phrase.count(sym)))
        
        # Сортировка списка частот по значению в порядке убывания
        self.syms.sort(key=lambda sym: sym.value, reverse=True)

    def calculate_ver(self):
        '''
        Расчёт вероятностей для каждого символа
        '''
        # Расчёт общего количества символов
        sym: Symbol
        syms_sum = sum(sym.value for sym in self.syms)
        for sym in self.syms:
            # Расчет вероятности для каждого символа
            sym.ver = sym.value / syms_sum

    def numer_syms(self, syms: list[Symbol]):
        '''
        Кодирование алфавита фразы с использованием логики дерева Шеннона–Фано
            `syms: list[Symbol]` - список объектов символов (букв)
        '''
        if len(syms) > 1:
            # Нахождение оптимального разделения списка
            sum_ver = sum(sym.ver for sym in syms)
            best_difference = sum_ver
            best_index = 0

            current_sum = 0
            for i, sym in enumerate(syms):
                current_sum += sym.ver
                difference = abs((sum_ver - current_sum) - current_sum)
                if difference < best_difference:
                    best_difference = difference
                    best_index = i + 1

            left = [sym for sym in syms[:best_index]]
            right = [sym for sym in syms[best_index:]]

            # Добавление бинарных кодов
            for sym in left:
                sym.bincode += '0'
            for sym in right:
                sym.bincode += '1'

            # Рекурсивное применение функции к обеим группам
            self.numer_syms(left)
            self.numer_syms(right)


