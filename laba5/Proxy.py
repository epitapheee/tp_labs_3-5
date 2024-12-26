class RealSubject:
    def request(self):
        print("Выполнение запроса реального объекта.")

class Proxy:
    def __init__(self, real_subject):
        self._real_subject = real_subject
        self._authenticated = False

    def authenticate(self, password):
        self._authenticated = password == "secure_password"
        print("Доступ {}".format("предоставлен" if self._authenticated else "запрещен"))

    def request(self):
        if self._authenticated:
            self._real_subject.request()
        else:
            print("Доступ запрещен. Выполните аутентификацию.")

# Использование
real_subject = RealSubject()
proxy = Proxy(real_subject)

proxy.request()
proxy.authenticate("wrong_password")
proxy.request()
proxy.authenticate("secure_password")
proxy.request()