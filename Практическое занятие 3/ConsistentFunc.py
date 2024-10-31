from ShannonFanoFunc import ShannonFano as Fano, Symbol

class CoderFunc():   
    def encoder(phrase: str, syms: list[Symbol]):
        '''
        Кодирование фразы по известному алфавиту
            `phrase: str` - фраза (набор символов)
            `syms: list[Symbol]` - алфавит кодировок
        '''

        # Делаем замену символа на бинарный код в соотв. с алфавитом (кодировкой)
        for sym in syms:
            phrase = phrase.replace(sym.key, '+' + sym.bincode + '+')

        # Избавляемся от технической реализации
        phrase = phrase.replace('++', ' ').replace('+', '')
        return phrase

    def decoder(phrase: str, syms: list[Symbol]):
        '''
        Декодирование фразы по известному алфавиту
            `phrase: str` - фраза (набор бинарных кодов)
            `syms: list[Symbol]` - алфавит кодировок
        '''

        # Делаем замену бинарного кода на символ в соотв. с алфавитом (кодировкой)
        for sym in syms:
            phrase = phrase.replace(sym.bincode, sym.key)

        return phrase

