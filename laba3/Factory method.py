from abc import ABC, abstractmethod


# Интерфейс для продукта (логгера)
class Logger(ABC):
    @abstractmethod
    def log(self, message: str) -> None:
        pass


# Конкретный продукт: Файловый логгер
class FileLogger(Logger):
    def log(self, message: str) -> None:
        print(f"Logging to file: {message}")


# Конкретный продукт: Консольный логгер
class ConsoleLogger(Logger):
    def log(self, message: str) -> None:
        print(f"Logging to console: {message}")


# Создатель (фабрика)
class LoggerFactory(ABC):
    @abstractmethod
    def create_logger(self) -> Logger:
        pass

    def log_message(self, message: str) -> None:
        logger = self.create_logger()
        logger.log(message)


# Конкретный создатель: Фабрика для файлового логгера
class FileLoggerFactory(LoggerFactory):
    def create_logger(self) -> Logger:
        return FileLogger()


# Конкретный создатель: Фабрика для консольного логгера
class ConsoleLoggerFactory(LoggerFactory):
    def create_logger(self) -> Logger:
        return ConsoleLogger()


# Пример использования
if __name__ == "__main__":
    # Используем фабрику для консольного логгера
    console_factory = ConsoleLoggerFactory()
    console_factory.log_message("This is a message for the console.")

    # Используем фабрику для файлового логгера
    file_factory = FileLoggerFactory()
    file_factory.log_message("This is a message for the file.")