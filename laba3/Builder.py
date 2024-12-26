# Класс продукта, представляющий пиццу
class Pizza:
    def __init__(self, dough="", sauce="", topping=""):
        self.dough = dough
        self.sauce = sauce
        self.topping = topping

    def __str__(self):
        return f"Pizza(dough='{self.dough}', sauce='{self.sauce}', topping='{self.topping}')"

# Класс строителя для пошагового создания пиццы
class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_dough(self, dough):
        self.pizza.dough = dough
        return self

    def set_sauce(self, sauce):
        self.pizza.sauce = sauce
        return self

    def set_topping(self, topping):
        self.pizza.topping = topping
        return self

    def build(self):
        return self.pizza

# Пример использования строителя
if __name__ == "__main__":
    pizza = (
        PizzaBuilder()
        .set_dough("cross")
        .set_sauce("mild")
        .set_topping("ham+pineapple")
        .build()
    )

    print(pizza)