class Book:
    """Класс, представляющий книгу
    """

    def __init__(self, title, year, genre):
        self.name = title
        self.year = year
        self.genre = genre
        """Конструктор

        Задание: сохраните title, year и genre в виде
        атрибутов объекта self
        """

    def __repr__(self):
        return 'Book( ({!r}), ({!r}), ({!r}))'.format(self.name, self.year, self.genre)

        """Возвращает внутреннее строковое представление объекта
        для консоли, отладчика и т.д.

        Задание: верните строку в формате
                 Book("название", год, "жанр")
        """

    def __str__(self):
        return self.name
        """Возвращает строку, предназначенную для пользователя
        (str, print и т.д.)

        Задание: верните строку в произвольном формате
        """


# Задание: создайте несколько объектов класса Book
# и выведите их на экран

first_book = Book('Robin Hood', 1457, 'fairytales')
second_book = Book('History for everyone', 2009, 'education')
print(first_book,',', second_book)
