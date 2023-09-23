import json

class BackgammonGameState:
    def __init__(self):
        # Load the starting position from the JSON structure
        with open("newgame.json", "r") as file:
            self.board = json.load(file)["board"]

    def display_board(self):
        # Display the current state of the board
        for i, point in enumerate(self.board):
            player = point["player"]
            count = point["count"]
            print(f"Point {i + 1}: {player} - {count} stone(s)")

if __name__ == "__main__":
    # Create a new game state
    new_game_state = BackgammonGameState()