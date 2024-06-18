#5 ROCK PAPER SCISSORS GAME

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    player1_wins = 0
    player2_wins = 0

    while player1_wins < 2 and player2_wins < 2:
        player1_choice = input("Player 1, choose rock, paper, or scissors: ").lower().strip()
        player2_choice = input("Player 2, choose rock, paper, or scissors: ").lower().strip()

        print(f"Player 1 chose: {player1_choice}")
        print(f"Player 2 chose: {player2_choice}")

        if player1_choice == player2_choice:
            print("It's a tie!")
        elif (player1_choice == "rock" and player2_choice == "scissors") or \
             (player1_choice == "paper" and player2_choice == "rock") or \
             (player1_choice == "scissors" and player2_choice == "paper"):
            player1_wins += 1
            print("Player 1 wins this round!")
        else:
            player2_wins += 1
            print("Player 2 wins this round!")

    if player1_wins == 2:
        print("Player 1 wins the game!")
    else:
        print("Player 2 wins the game!")

# Run the rock-paper-scissors game between two players
rock_paper_scissors()