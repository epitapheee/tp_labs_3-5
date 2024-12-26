# Класс с интерфейсом, несовместимым с нашим кодом
class OldSystem:
    def old_method(self):
        return "Данные из старой системы"

# Новый интерфейс, который мы хотим использовать
class NewSystem:
    def new_method(self):
        return "Данные из новой системы"

# Адаптер, который делает старый интерфейс совместимым с новым
class Adapter:
    def __init__(self, old_system):
        self.old_system = old_system

    def new_method(self):
        # Адаптируем старый метод под новый интерфейс
        return self.old_system.old_method()

# Клиентский код, использующий новый интерфейс
def client_code(system):
    print(system.new_method())

# Пример использования
if __name__ == "__main__":
    # Работа с новой системой
    new_system = NewSystem()
    client_code(new_system)

    # Работа с адаптированной старой системой
    old_system = OldSystem()
    adapted_system = Adapter(old_system)
    client_code(adapted_system)