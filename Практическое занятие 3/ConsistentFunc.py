from ShannonFanoFunc import ShannonFano as Fano, Symbol

class CoderFunc():   
    def encoder(phrase: str, syms: list[Symbol]):
        # Кодировщик

        # Делаем замену символа в соотв. с нашим бинарным алфавитом (кодировкой)
        for sym in syms:
            phrase = phrase.replace(sym.key, '+' + sym.bincode + '+')

        # Избавляемся от технической реализации
        phrase = phrase.replace('++', ' ').replace('+', '')
        return phrase

    def decoder(phrase: str, syms: list[Symbol]):
        # Декодер

        for sym in syms:
            phrase = phrase.replace(sym.bincode, sym.key)

        return phrase

