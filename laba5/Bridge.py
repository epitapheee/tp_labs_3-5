# Реализация (Implementation)
class Implementation:
    def operation(self):
        pass

class ConcreteImplementationA(Implementation):
    def operation(self):
        return "Implementation A"

class ConcreteImplementationB(Implementation):
    def operation(self):
        return "Implementation B"

# Абстракция (Abstraction)
class Abstraction:
    def __init__(self, implementation: Implementation):
        self.implementation = implementation

    def operation(self):
        return f"Abstraction: {self.implementation.operation()}"

# Использование
impl_a = ConcreteImplementationA()
impl_b = ConcreteImplementationB()

abstraction1 = Abstraction(impl_a)
abstraction2 = Abstraction(impl_b)

print(abstraction1.operation())  # Abstraction: Implementation A
print(abstraction2.operation())  # Abstraction: Implementation B