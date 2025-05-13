
import random

# Snakes and Ladders configuration
snakes = {
    16: 6,
    47: 26,
    49: 11,
    56: 53,
    62: 19,
    64: 60,
    87: 24,
    93: 73,
    95: 75,
    98: 78
}

ladders = {
    1: 38,
    4: 14,
    9: 31,
    21: 42,
    28: 84,
    36: 44,
    51: 67,
    71: 91,
    80: 100
}

def roll_dice():
    return random.randint(1, 6)

def move_player(position, player_name):
    input(f"{player_name}, press Enter to roll the dice...")
    dice = roll_dice()
    print(f"{player_name} rolled a {dice}")

    if position + dice > 100:
        print("Move exceeds 100. Try again next turn.")
        return position

    position += dice

    if position in snakes:
        print(f"Oh no! {player_name} got bitten by a snake and fell from {position} to {snakes[position]}")
        position = snakes[position]
    elif position in ladders:
        print(f"Yay! {player_name} climbed a ladder from {position} to {ladders[position]}")
        position = ladders[position]
    else:
        print(f"{player_name} moved to {position}")
    
    return position

def play_game():
    player1 = input("Enter Player 1 name: ")
    player2 = input("Enter Player 2 name: ")
    pos1 = 0
    pos2 = 0

    while True:
        pos1 = move_player(pos1, player1)
        if pos1 == 100:
            print(f"🎉 {player1} wins the game! 🎉")
            break

        pos2 = move_player(pos2, player2)
        if pos2 == 100:
            print(f"🎉 {player2} wins the game! 🎉")
            break

if __name__ == "__main__":
    print("🎲 Welcome to Snake and Ladder! 🎲\n")
    play_game()
