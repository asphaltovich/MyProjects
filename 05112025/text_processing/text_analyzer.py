class TextAnalyzer: # Создание класса
    def __init__(self, text): # Инициализация полей
        self.text = text # Имя поля
        self.words = self.text.split() # Преобразование текста

    def count_words(self): # Функция подсчёта слов
        return len(self.words) # Возврат длины слов

    def longest_word(self): # Функция самого длинного слова
        if not self.words: # Если нет возвращаемого 
            return "" # Возвращается пустое 
        else: # Иначе
            return max(self.words, key=len) # Возвращается самое длинное слово

    def replace_word(self, old_word, new_word): # Функция замены слов
        self.text = self.text.replace(old_word, new_word) # заменить старое слово новым словом
        self.words = self.text.split() # Преобразование текста
        return self.text # возвращается новое слово