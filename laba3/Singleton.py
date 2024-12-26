class Singleton:
    instance = None  # Хранит ссылку на единственный экземпляр класса

    def __new__(cls):
        if cls.instance is None:  # Проверяем, создан ли уже экземпляр
            cls.instance = super().__new__(cls)  # Создаём экземпляр, если его нет
        return cls.instance  # Возвращаем существующий или новый экземпляр

# Проверка работы
singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 is singleton2)  # True, оба объекта ссылаются на один экземпляр