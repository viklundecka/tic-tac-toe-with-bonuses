class TicTacToeError(Exception):
    """Базовый класс для исключений в игре."""
    pass

class InvalidMoveError(TicTacToeError):
    """Исключение для недопустимого хода."""
    def __init__(self, message="Ход недопустим. Проверьте координаты и состояние клетки."):
        super().__init__(message)

class PlayerError(TicTacToeError):
    """Исключение для ошибок, связанных с игроками."""
    def __init__(self, message="Ошибка инициализации игрока или переключения."):
        super().__init__(message)

class BoardError(TicTacToeError):
    """Исключение для ошибок игрового поля."""
    def __init__(self, message="Ошибка работы с игровым полем."):
        super().__init__(message)

# Пример использования
if __name__ == "__main__":
    try:
        raise InvalidMoveError()
    except TicTacToeError as e:
        print(f"Игра: {e}")
