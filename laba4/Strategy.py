# Интерфейс стратегии сортировки
class SortingStrategy:
    def sort(self, array):
        pass


# Стратегия: Сортировка пузырьком
class BubbleSortStrategy(SortingStrategy):
    def sort(self, array):
        for i in range(len(array)):
            for j in range(len(array) - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
        print("Bubble Sort:", array)


# Стратегия: Быстрая сортировка
class QuickSortStrategy(SortingStrategy):
    def sort(self, array):
        print("Quick Sort:", sorted(array))


# Класс для выбора стратегии
class Sorter:
    def __init__(self, strategy=None):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def sort_array(self, array):
        if self.strategy:
            self.strategy.sort(array)
        else:
            print("Strategy not set!")


# Пример использования
if __name__ == "__main__":
    sorter = Sorter()

    sorter.set_strategy(BubbleSortStrategy())
    sorter.sort_array([5, 3, 8, 4, 2])

    sorter.set_strategy(QuickSortStrategy())
    sorter.sort_array([5, 3, 8, 4, 2])