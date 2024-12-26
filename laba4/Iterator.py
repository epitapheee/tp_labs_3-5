# Итератор
class MyListIterator:
    def __init__(self, collection):
        self._collection = collection
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._collection):
            item = self._collection[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration

# Коллекция, которая использует итератор
class MyList:
    def __init__(self, data):
        self._data = data

    def __iter__(self):
        return MyListIterator(self._data)

# Пример использования
my_list = MyList([1, 2, 3, 4, 5])

for item in my_list:
    print(item)