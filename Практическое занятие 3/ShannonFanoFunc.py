
class Symbol():
    # Объект символа исходной строки
    def __init__(self, key: str, value: int, ver: float=0.0) -> None:
        self.key = key # символ
        self.value = value # его количество
        self.ver = ver # вероятность
        self.bincode = '' # код символа

class ShannonFano():
    # Метод Шеннона-Фано
    def __init__(self, phrase: str) -> None:
        self.phrase = phrase
        self.syms = list()
        self.count_sym = dict()

    def count_sym_all(self):
        # Расчёт частот в исходной фразе
        be_syms = []
        for sym in self.phrase:
            if sym not in be_syms: 
                be_syms.append(sym)
                self.syms.append(Symbol(sym, self.phrase.count(sym)))
        
        # Сортировка списка частот по значению в порядке убывания
        self.syms.sort(key=lambda sym: sym.value, reverse=True)

    def calculate_ver(self):
        # Расчёт общего количества символов
        syms_sum = sum(sym.value for sym in self.syms)
        for sym in self.syms:
            # Расчет вероятности для каждого символа
            sym.ver = sym.value / syms_sum

    def numer_syms(self, syms):
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


