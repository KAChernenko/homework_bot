class EndPointIsNotAvailiable(Exception):
    """Обработка исключения при недоступности ENDPOINT API."""
    pass


class InvalidResponseCode(Exception):
    """Не верный код ответа."""
    pass


class ConnectinError(Exception):
    """Не верный код ответа."""
    pass


class NotForSending(Exception):
    """Не для пересылки в тг."""
    pass


class EmptyResponseFromAPI(Exception):
    """Пустой ответ от API"""
    pass


class TelegramError(Exception):
    "Ошибка отправки"
    pass