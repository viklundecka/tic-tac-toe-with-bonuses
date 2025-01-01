from game_logic_module import Player, TicTacToeGame
from ui_module import TicTacToeBoard

# Определяем игроков
DEFAULT_PLAYERS = (
    Player(label="X", color="blue"),
    Player(label="O", color="green"),
)

# Точка входа в приложение
def main():
    """Создать интерфейс игры и запустить цикл обработки событий."""
    game = TicTacToeGame(players=DEFAULT_PLAYERS, board_size=3)
    board = TicTacToeBoard(game)
    board.mainloop()

if __name__ == "__main__":
    main()
