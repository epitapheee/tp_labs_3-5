# Класс кнопки (Button), представляет один тип продукта
class Button:
    def __init__(self, os_type):
        self.os_type = os_type

    def paint(self):
        print(f"You have created a {self.os_type} button.")


# Класс чекбокса (Checkbox), представляет другой тип продукта
class Checkbox:
    def __init__(self, os_type):
        self.os_type = os_type

    def paint(self):
        print(f"You have created a {self.os_type} checkbox.")


# Абстрактная фабрика для создания продуктов (Button и Checkbox)
class GUIFactory:
    def __init__(self, os_type):
        self.os_type = os_type

    def create_button(self):
        return Button(self.os_type)

    def create_checkbox(self):
        return Checkbox(self.os_type)


# Клиентский класс, использующий фабрику для создания и работы с продуктами
class Application:
    def __init__(self, factory):
        self.button = factory.create_button()
        self.checkbox = factory.create_checkbox()

    def paint(self):
        self.button.paint()
        self.checkbox.paint()

# Пример использования
if __name__ == "__main__":
    print("Using Windows factory:")
    app1 = Application(GUIFactory("Windows"))
    app1.paint()

    print("\nUsing Mac factory:")
    app2 = Application(GUIFactory("Mac"))
    app2.paint()