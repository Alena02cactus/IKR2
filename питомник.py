class Животное:
    def __init__(self, имя, вид):
        self.имя = имя
        self.вид = вид
        self.команды = []

    def определить_класс(self):
        # Реализация определения класса животного
        pass

    def показать_команды(self):
        print(f"Команды для {self.имя}:")
        for команда in self.команды:
            print(команда)

    def обучить_командам(self, новая_команда):
        self.команды.append(новая_команда)


class Счетчик:
    def __init__(self):
        self.счетчик = 0

    def add(self):
        self.счетчик += 1

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None or self.счетчик > 0:
            raise Exception("Работа с объектом типа Счетчик была не в ресурсном блоке try или ресурс остался открыт")


# Пример использования
try:
    with Счетчик() as счетчик:
        счетчик.add()
        счетчик.add()
except Exception as e:
    print(e)

пес = Животное("Шарик", "собака")
пес.обучить_командам("Сидеть")
пес.обучить_командам("Лежать")
пес.показать_команды()
