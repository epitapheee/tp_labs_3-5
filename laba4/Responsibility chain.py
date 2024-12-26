class Handler:
    def __init__(self, successor=None):
        self.successor = successor  # следующий обработчик в цепочке

    def handle(self, request):
        if self.successor:
            self.successor.handle(request)


class ConcreteHandlerA(Handler):
    def handle(self, request):
        if request == "A":
            print("Handler A обработал запрос")
        elif self.successor:
            self.successor.handle(request)


class ConcreteHandlerB(Handler):
    def handle(self, request):
        if request == "B":
            print("Handler B обработал запрос")
        elif self.successor:
            self.successor.handle(request)


class ConcreteHandlerC(Handler):
    def handle(self, request):
        if request == "C":
            print("Handler C обработал запрос")
        elif self.successor:
            self.successor.handle(request)


# Создаем цепочку обработчиков
handler_chain = ConcreteHandlerA(ConcreteHandlerB(ConcreteHandlerC()))

# Пример обработки запросов
handler_chain.handle("A")  # Handler A обработал запрос
handler_chain.handle("B")  # Handler B обработал запрос
handler_chain.handle("C")  # Handler C обработал запрос
handler_chain.handle("D")  # Нет обработчика для запроса