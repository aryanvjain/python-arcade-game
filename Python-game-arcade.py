import random
import mysql.connector as q
from questions import qgk, qsports, qgeo, qtech, qs

# Connect to MySQL database
c = q.connect(host="localhost", user="root", password="Bl@hBl@h2007", database="aryan")
cur = c.cursor()

print("********************************************************ARCADE****************************************************")
print("*1. Wordle (Word Guessing) 🧩                                                                                    *")
print("*2. Rock-Paper-Scissors ✊✋✌                                                                                      *")
print("*3. GoFish (Card Game) 🃏🎴                                                                                      *")
print("*4. Quiz ❓📝                                                                                                    *")
print("*5. Handcricket 🏏                                                                                               *")
print("*6. Chopsticks ✋✋                                                                                               *")
print("*7. Typing Game ⌨️⏱                                                                                            *")
print("*8. Leader board list 🚪                                                                                                      *")
print("*9. Exit🚪                                                                                                      *")
print("******************************************************************************************************************")

# Function to play Wordle
def gamewordle():
    # Generates feedback based on the guessed word compared to the target word
    def get_feedback(guess, target):
        feedback = []  # Stores feedback as G (Green), Y (Yellow), or - (Gray)
        target_letters = list(target)

        # Check for letters in the correct position
        for i in range(len(guess)):
            if guess[i] == target[i]:
                feedback.append('G')
                target_letters[i] = None  # Mark as used
            else:
                feedback.append('-')

        # Check for correct letters in the wrong position
        for i in range(len(guess)):
            if feedback[i] == '-':
                if guess[i] in target_letters:
                    feedback[i] = 'Y'
                    target_letters[target_letters.index(guess[i])] = None
                else:
                    feedback[i] = '-'  # Incorrect letter
        return ''.join(feedback)

    # Main function for Wordle game
    def wordle():
        word_list = [ "apple", "grape", "chair", "table", "plant", "brush", "shine", "glass", "snake", "flame", "stone", "truck", 
                      "creep", "fight", "clean", "grain", "sharp", "space", "brown", "music", "frame", "dress", "shiny", "clock", 
                      "bloom", "field", "water", "liver", "flock", "score", "crowd", "round", "storm", "flute", "story", "earth" ]
        target_word = random.choice(word_list)
        attempts = 6

        print("Welcome to Wordle!")
        print("Guess the 5-letter word. You have 6 attempts.")
        print("Feedback: G=Green (correct), Y=Yellow (wrong position), -=Red (wrong letter)")

        for attempt in range(attempts):
            guess = input(f"Attempt {attempt + 1}/{attempts}: ").lower()
            if len(guess) != 5 or not guess.isalpha():
                print("Invalid input! Please enter a 5-letter word.")
                continue

            feedback = get_feedback(guess, target_word)
            print("Feedback:", feedback)

            if guess == target_word:
                print("Congratulations! You guessed the word!")
                break
        else:
            print(f"Sorry, you've used all attempts. The word was: {target_word}")

    if __name__ == "__main__":
        wordle()

# Function to play Rock-Paper-Scissors
def gamerps():
    # Prints the rules of the game
    def print_rules():
        print("Welcome to Rock, Paper, Scissors! 🎮")
        print("Here are the rules:")
        print("""
        - Rock beats Scissors.
        - Scissors beats Paper.
        - Paper beats Rock.
        """)
        print("The game will be played for 3 rounds. Let the battle begin! 🪨📄✂️")

    # Generates a random choice for the computer
    def get_computer_choice():
        choices = ["rock", "paper", "scissors"]
        return random.choice(choices)

    # Takes user input and ensures it's valid
    def get_user_choice():
        while True:
            choice = input("Enter your choice (rock, paper, or scissors): ").lower()
            if choice in ["rock", "paper", "scissors"]:
                return choice
            print("Invalid choice. Please try again!")

    # Determines the winner of a round based on the choices
    def determine_winner(user, computer):
        if user == computer:
            return "tie"
        elif (user == "rock" and computer == "scissors") or \
             (user == "scissors" and computer == "paper") or \
             (user == "paper" and computer == "rock"):
            return "user"
        else:
            return "computer"

    # Main function to manage the Rock-Paper-Scissors game
    def main():
        print_rules()
        user_score = 0
        computer_score = 0
        ties = 0

        for round_number in range(1, 4):  # Play 3 rounds
            print(f"\nRound {round_number} of 3:")
            user_choice = get_user_choice()
            computer_choice = get_computer_choice()
            print(f"\nYou chose: {user_choice}")
            print(f"Computer chose: {computer_choice}")
            result = determine_winner(user_choice, computer_choice)

            if result == "user":
                print("You win this round! 🎉")
                user_score += 1
            elif result == "computer":
                print("Computer wins this round! 💻")
                computer_score += 1
            else:
                print("This round is a tie! 🤝")
                ties += 1

        print("\nFinal Results:")
        print(f"Your Score: {user_score}")
        print(f"Computer's Score: {computer_score}")
        print(f"Ties: {ties}")

        if user_score > computer_score:
            print("Congratulations! You are the overall winner! 🏆")
        elif computer_score > user_score:
            print("Computer wins overall! Better luck next time! 💻")
        else:
            print("It's an overall tie! What a close game! 🤝")

        print("Thanks for playing! Goodbye 👋")

    if __name__ == "__main__":
        main()
import random
import mysql.connector as q
from questions import qgk, qsports, qgeo, qtech, qs

# Global variables to track turn count, winner, and username for Go Fish
global turn_count, winner, username
turn_count = 0
winner = ""
username = ""

# Function to play Go Fish
def gamegofish():
    # Print the rules of the game
    def print_rules():
        print("Hello!\n Welcome to our game Go Fish 😄\nHere are the rules for the game")
        print(""" 
        ♦ Objective: Collect sets of matching cards. 
        ♦ Setup: 
          - Deal 5 cards to the player and the computer. 
          - Place the rest as the draw pile. 
        ♦ Gameplay: 
          - Player starts, then computer. 
          - Ask for a specific rank of card. 
          - If opponent has it, they give it to you. 
          - If not, draw from the pile. 
        ♦ Creating Sets: 
          - Lay down sets of four when collected. 
        ♦ Winning: 
          - Game ends when 3 sets are collected or draw pile is empty. 
          - The player first to make 3 sets wins. 
        ♦ Note: 
          - Please use only capitals for face cards and ace (A, K, J, Q).
        """)
        global username
        username = input("Enter your name: ")

    # Create and shuffle a deck of cards
    def create_deck():
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        deck = [(rank, suit) for rank in ranks for suit in suits]
        random.shuffle(deck)
        return deck, ranks

    # Deal initial hands to the player and the computer
    def deal_cards(deck, ranks):
        player_hand = {rank: 0 for rank in ranks}
        computer_hand = {rank: 0 for rank in ranks}
        for _ in range(7):
            player_hand[deck.pop()[0]] += 1
            computer_hand[deck.pop()[0]] += 1
        return player_hand, computer_hand

    # Check for completed sets (four of a kind) in a hand
    def check_sets(hand):
        return [rank for rank, count in hand.items() if count == 4]

    # Display the player's current hand
    def display_hand(hand, player_name):
        print(f"\n{player_name}'s hand:")
        print("-" * 33)
        print("|" + "Rank".center(15) + "|" + "Count".center(15) + "|")
        print("-" * 33)
        for rank, count in hand.items():
            if count != 0:
                print("|" + str(rank).center(15) + "|" + str(count).center(15) + "|")
                print("-" * 33)

    # Handle the player's turn
    def player_turn(player_hand, computer_hand, deck, turn_count):
        rank_to_ask = input("Enter the rank to ask for: ")
        if rank_to_ask not in computer_hand or computer_hand[rank_to_ask] == 0:
            print("Go Fish!")
            if deck:
                drawn_card = deck.pop()
                player_hand[drawn_card[0]] += 1
                print("You drew", drawn_card[0])
        else:
            print("Computer gives you", rank_to_ask + "s!")
            player_hand[rank_to_ask] += computer_hand[rank_to_ask]
            computer_hand[rank_to_ask] = 0
        return turn_count + 1

    # Handle the computer's turn
    def computer_turn(player_hand, computer_hand, deck):
        rank_to_ask = random.choice([rank for rank, count in computer_hand.items() if count > 0])
        print("Computer asks for", rank_to_ask + "s!")
        if rank_to_ask not in player_hand or player_hand[rank_to_ask] == 0:
            print("Go Fish for computer!")
            if deck:
                drawn_card = deck.pop()
                computer_hand[drawn_card[0]] += 1
                print("Computer drew a card.")
        else:
            print("You give computer", rank_to_ask + "s!")
            computer_hand[rank_to_ask] += player_hand[rank_to_ask]
            player_hand[rank_to_ask] = 0

    # Main function to control the Go Fish game flow
    def main():
        global turn_count, winner, username
        

        print_rules()
        deck, ranks = create_deck()
        player_hand, computer_hand = deal_cards(deck, ranks)

        player_sets = 0
        computer_sets = 0

        # Main game loop
        while True:
            if player_sets >= 3:
                print(f"Congratulations {username}! You've collected 3 sets and won 🎉🏆🥇!")
                winner = username
                break
            elif computer_sets >= 3:
                print("Computer has collected 3 sets and won! Better luck next time 🍀")
                winner = "Computer"
                break

            display_hand(player_hand, username)
            print("Computer has", sum(computer_hand.values()), "cards.")

            player_sets += len(check_sets(player_hand))
            for rank in check_sets(player_hand):
                player_hand[rank] = 0

            turn_count = player_turn(player_hand, computer_hand, deck, turn_count)

            computer_sets += len(check_sets(computer_hand))
            for rank in check_sets(computer_hand):
                computer_hand[rank] = 0

            computer_turn(player_hand, computer_hand, deck)

        # Save results to database
        cur.execute("INSERT INTO gofish (name, turns_taken_to_win, winner) VALUES (%s, %s, %s)", (username, turn_count, winner))
        c.commit()
        
        print("Game results saved successfully.")

    main()
def gamehandcricket():
    """
    Function to play a game of Hand Cricket between a player and the computer.
    Rules and instructions are displayed, followed by a toss and gameplay.
    The player chooses to bat or bowl, and both innings are played until a winner is decided.
    """
    
    print("🎮 Welcome to Hand Cricket! Let's go over the rules and instructions: 🎉")

    # Displaying rules and instructions
    print("📜 *Rules:*")
    print("1️⃣ This is a 1v1 game between you and the computer.")
    print("2️⃣ You can choose to either bat 🏏 or bowl 🏏 first if you win the toss.")
    print("3️⃣ When batting 🏏, enter a number between 1 and 6 to play your shot.")
    print("4️⃣ When bowling 🏏, enter a number between 1 and 6 to bowl at the computer.")
    print("5️⃣ If your number matches the computer's number, it's an OUT! ❌")

    print("\n📋 *Game Flow:*")
    print("🚀 Toss Time: Decide heads or tails to start the game!")
    print("🎲 Batting 🏏: Score as many runs as you can without getting out.")
    print("🎯 Bowling 🏏: Try to get the computer OUT by matching its number.")
    print("🏁 Target: After the first innings, the other player will chase the target score.")
    print("🎯 Win: The player who scores more runs wins the match! 🏆")

    print("\n🎉 Have fun, and good luck! 🍀")

    # Main hand cricket game function
    def hand_cricket():
        """
        Handles the core logic of Hand Cricket, including the toss,
        gameplay, innings, and determining the winner.
        """
        
        username = input("Enter your name: ")

        # Initialize scores, game state, and winner
        user_score = 0
        computer_score = 0
        target = None
        game_over = False
        winner = None

        print(f"Welcome to Hand Cricket, {username}!")
        print("Let's start with a toss. Choose heads or tails.")

        # Toss logic
        toss_call = input("Enter your choice (heads/tails): ").lower()
        toss_result = random.choice(["heads", "tails"])

        # Determine toss winner and choice
        if toss_call == toss_result:
            print(f"{username}, you won the toss!")
            choice = input("Do you want to bat or bowl first? (bat/bowl): ").lower()
            user_bats_first = choice == "bat"
        else:
            print("Computer won the toss!")
            user_bats_first = random.choice([True, False])
            print("Computer chooses to", "bat first." if not user_bats_first else "bowl first.")

        # FIRST INNINGS
        if user_bats_first:
            print(f"\n{username}, you are batting first.")

            while not game_over:
                try:
                    user_input = int(input("Your shot (1-6): "))
                except:
                    print("Enter number only")
                    continue

                if user_input not in range(1, 7):
                    print("Invalid input! Choose a number between 1 and 6.")
                    continue

                computer_input = random.randint(1, 6)
                print(f"Computer bowled: {computer_input}")

                if user_input == computer_input:
                    print("Out! You are out.")
                    game_over = True
                else:
                    user_score += user_input
                    print(f"{username}'s score: {user_score}")

            target = user_score + 1
            print(f"\nComputer needs {target} to win.")

            # SECOND INNINGS (computer batting)
            game_over = False

            while not game_over:

                try:
                    user_input = int(input("Bowl (1-6): "))
                except:
                    print("Enter number only")
                    continue

                if user_input not in range(1, 7):
                    print("Invalid input!")
                    continue

                computer_input = random.randint(1, 6)
                print(f"Computer's shot: {computer_input}")

                if user_input == computer_input:
                    print("Out! Computer is out.")
                    winner = username
                    game_over = True

                else:
                    computer_score += computer_input
                    print(f"Computer score: {computer_score}")

                    if computer_score >= target:
                        print("Computer won the game.")
                        winner = "Computer"
                        game_over = True

        else:
            print("\nComputer is batting first.")

            while not game_over:

                try:
                    user_input = int(input("Bowl (1-6): "))
                except:
                    print("Enter number only")
                    continue

                if user_input not in range(1, 7):
                    print("Invalid input!")
                    continue

                computer_input = random.randint(1, 6)
                print(f"Computer's shot: {computer_input}")

                if user_input == computer_input:
                    print("Out! Computer is out.")
                    game_over = True
                else:
                    computer_score += computer_input
                    print(f"Computer score: {computer_score}")

            target = computer_score + 1
            print(f"\n{username}, you need {target} to win.")

            # SECOND INNINGS (user batting)
            game_over = False

            while not game_over:

                try:
                    user_input = int(input("Your shot (1-6): "))
                except:
                    print("Enter number only")
                    continue

                if user_input not in range(1, 7):
                    print("Invalid input!")
                    continue

                computer_input = random.randint(1, 6)
                print(f"Computer bowled: {computer_input}")

                if user_input == computer_input:
                    print("Out! You are out.")
                    winner = "Computer"
                    game_over = True

                else:
                    user_score += user_input
                    print(f"{username}'s score: {user_score}")

                    if user_score >= target:
                        print(f"Congratulations, {username}! You won the game.")
                        winner = username
                        game_over = True

        print(f"\nWinner: {winner}")
        # save result to database
        cur.execute(
            "INSERT INTO handcricket (name, player_score, computer_score, winner) VALUES (%s, %s, %s, %s)",
            (username, user_score, computer_score, winner)
        )
        c.commit()
    hand_cricket()

def gamequiz():
    def f1():
        score = 0
        asked_questions = set()
        name = input("Enter the name of the user: ")
        genre = int(input("Which genre of the quiz do you want?\n1. General Knowledge\n2. Sports\n3. Geography\n4. Technology\n5. Geopolitics\n"))
        diff = int(input("Level of difficulty:\n1. Easy\n2. Medium\n3. Tough\n"))
        
        # Map genres and difficulties
        genre_dict = {1: qgk, 2: qsports, 3: qgeo, 4: qtech, 5: qs}
        genre_names = {1: "General Knowledge", 2: "Sports", 3: "Geography", 4: "Technology", 5: "Geopolitics"}
        chosen_genre = genre_names.get(genre, "Unknown Genre")
        chosen_diff = diff - 1  # Adjust index for difficulty
        
        print(f"You have chosen the genre: {chosen_genre}")
        
        # Question loop
        for _ in range(3):
            q_dict = genre_dict[genre][chosen_diff]
            question, options = random.choice(list(q_dict.items()))
            
            # Ensure no repetition
            while question in asked_questions:
                question, options = random.choice(list(q_dict.items()))
            
            asked_questions.add(question)
            
            # Display question and options
            print(f"Question: {question}")
            print("Options:")
            print(f"a. {options[0]}")
            print(f"b. {options[1]}")
            print(f"c. {options[2]}")
            print(f"d. {options[3]}")
            
            # Get user answer
            user_answer = input("Enter your answer (a, b, c, d): ").lower()
            correct_option = options[4]
            
            # Check answer
            if user_answer in "abcd" and options["abcd".index(user_answer)] == correct_option:
                print("Your answer is correct!")
                score += 1000  # Increment score by 1000 for each correct answer
            else:
                print(f"Your answer is wrong. The correct answer is: {correct_option}")
        
        # Print final score
        print(f"Your final score is: {score}")
        cur.execute("insert into quizs (name,genre,difficulty,score) values (%s,%s,%s,%s)", (name,chosen_genre,chosen_diff,score,))    
        c.commit()
    f1()

# Main function for the typing game
def gametyping():
    import time
    import random

    # Function to get a random sentence for the typing challenge
    def get_random_sentence():
        sentences = [
            "The quick brown fox jumps over the lazy dog.",
            "Typing games improve your speed and accuracy.",
            "A journey of a thousand miles begins with a single step.",
            "Practice makes perfect, especially in typing.",
            "Python is a versatile and powerful programming language.",
        ]
        return random.choice(sentences)

    # Function to handle the typing race between two players
    def typing_race():
        winner = " "
        winnertime = 0.0

        # Get player names
        player1 = input("Enter Player 1 name: ")
        player2 = input("Enter Player 2 name: ")

        print("Welcome to the Typing Race:", player1, "vs", player2, "!")
        print("Both players will type the same sentence, and the faster, accurate typer wins.")
        print("Press Enter to start!")
        input()

        # Display the sentence to be typed
        sentence = get_random_sentence()
        print("\nHere is the sentence:")
        print(sentence)

        # Player 1's turn
        print("\n", player1, " will type first. Press Enter to begin!")
        input()
        print("\n", player1, " start typing!")
        start_time_p1 = time.time()
        user_input_p1 = input("\nPlayer 1 input: ")
        end_time_p1 = time.time()
        time_p1 = end_time_p1 - start_time_p1

        # Player 2's turn
        print("\n", player2, " your turn! Press Enter to start.")
        input()
        print("\n", player2, " start typing!")
        start_time_p2 = time.time()
        user_input_p2 = input("\nPlayer 2 input: ")
        end_time_p2 = time.time()
        time_p2 = end_time_p2 - start_time_p2

        # Display the results
        print("\n=== Results ===")
        if user_input_p1 == sentence:
            print(f"{player1}: Correct! Time: {time_p1:.2f} seconds")
        else:
            print(f"{player1}: Incorrect input! {time_p1:.2f}")

        if user_input_p2 == sentence:
            print(f"{player2}: Correct! Time: {time_p2:.2f} seconds")
        else:
            print(f"{player2}: Incorrect input! {time_p2:.2f}")

        # Determine the winner
        if user_input_p1 == sentence and user_input_p2 == sentence:
            if time_p1 < time_p2:
                print("\n", player1, " wins!")
                winnertime = float(time_p1)
                winner = player1
            elif time_p2 < time_p1:
                winnertime = float(time_p2)
                winner = player2
                print("\n", player2, " wins!")
            else:
                print("\nIt's a tie!")
                winner = "tie"
        elif user_input_p1 == sentence:
            print("\n", player1, " wins by accuracy!")
            winner = player1
        elif user_input_p2 == sentence:
            print("\n", player2, " wins by accuracy!")
            winner = player2
        else:
            print("\nNo one wins, as both players made mistakes.")
            winner = "tie"

        # Store the result in the database
        cur.execute("INSERT INTO typings (player1, player2, time_taken_first_player, time_taken_second_player, winner_time, winner) VALUES (%s, %s, %s, %s, %s, %s)", 
                    (player1, player2, time_p1, time_p2, winnertime, winner))
        c.commit()

    typing_race()
def gamechopsticks():
    print("Welcome to Chopsticks!")
    print("Rules: Each hand starts with 1 finger. Add or split fingers to knock out your opponent's hands!")
    print("Hands are out when they reach 5 or more fingers.")

    # Initialize hands
    player1 = [1, 1]  # Player 1's left and right hand
    player2 = [1, 1]  # Player 2's left and right hand

    # Function to display the current state
    def display_hands():
        print(f"\nPlayer 1: Left - {player1[0]}, Right - {player1[1]}")
        print(f"Player 2: Left - {player2[0]}, Right - {player2[1]}")

    # Function to check if a player has lost
    def is_game_over(player):
        return player[0] == 0 and player[1] == 0

    # Main game loop
    turn = 1  # 1 for Player 1, 2 for Player 2
    while True:
        display_hands()

        # Check for game over
        if is_game_over(player1):
            print("Player 2 wins!")
            break
        elif is_game_over(player2):
            print("Player 1 wins!")
            break

        # Determine current player
        if turn == 1:
            current_player = player1
            opponent = player2
            print("\nPlayer 1's turn:")
        else:
            current_player = player2
            opponent = player1
            print("\nPlayer 2's turn:")

        # Player chooses action
        action = input("Choose an action: 'attack' or 'split': ").strip().lower()

        if action == "attack":
            # Choose hands for attack
            attacker_hand = int(input("Which hand are you attacking with? (1 for Left, 2 for Right): ")) - 1
            target_hand = int(input("Which opponent hand are you attacking? (1 for Left, 2 for Right): ")) - 1

            # Check if valid hands
            if current_player[attacker_hand] == 0:
                print("You cannot attack with an inactive hand!")
                continue
            if opponent[target_hand] == 0:
                print("You cannot attack an inactive hand!")
                continue

            # Perform the attack
            opponent[target_hand] += current_player[attacker_hand]
            if opponent[target_hand] >= 5:
                opponent[target_hand] = 0  
            print("Attack successful!")

        elif action == "split":
            
            new_left = int(input("Enter new number of fingers on your left hand: "))
            new_right = int(input("Enter new number of fingers on your right hand: "))

            if new_left + new_right != sum(current_player):
                print("Invalid split! The total fingers must remain the same.")
                continue

            current_player[0] = new_left
            current_player[1] = new_right
            print("Split successful!")

        else:
            print("Invalid action! Please choose 'attack' or 'split'.")
            continue

        # Switch turns
        turn = 1 if turn == 2 else 2

# Menu to choose a game
while True:
    game = int(input("Which game do you want to play?"))
    if game == 1:
        gamewordle()
    elif game == 2:
        gamerps()
    elif game == 3:
        gamegofish()
    elif game == 4:
        gamequiz()
    elif game == 5:
        gamehandcricket()
    elif game == 6:
        gamechopsticks()
    elif game == 7:
        gametyping()
    elif game == 8:
        break
    else:
        break

# Menu to display the leaderboard
while True:
    print("Score Board List\n1.GoFish\n2.Handcricket\n3.Quiz\n4.Typing game\n5. Exit")
    leader = int(input("Which game's leaderboard do you want to see?"))
    if leader == 1:
        cur.execute("SELECT * FROM gofish ORDER BY turns_taken_to_win ASC")
        b = cur.fetchall()
        print("\nName\t\tTurns\t\tWinner")
        print("-" * 50)
        for x in b:
            print(f"{x[0]}\t\t{x[1]}\t\t{x[2]}")
    elif leader == 2:

        c.commit()

        cur.execute("SELECT name, player_score, computer_score, winner FROM handcricket ORDER BY player_score DESC")

        b = cur.fetchall()

        print("\nName\t\tPlayer_Score\tComputer_Score\tWinner")
        print("-" * 70)

        for x in b:
            print(f"{x[0]}\t\t{x[1]}\t\t{x[2]}\t\t{x[3]}")
    elif leader == 3:
        cur.execute("SELECT * FROM quizs ORDER BY score DESC")
        b = cur.fetchall()
        print("\nName\t\t\tGenre\t\t\tDifficulty\t\tScore")
        print("-" * 80)
        for x in b:
            print(f"{x[0]}\t\t\t{x[1]}\t\t\t{x[2]}\t\t{x[3]}")
    elif leader == 4:
        cur.execute("SELECT * FROM typings")
        b = cur.fetchall()
        print("\nPlayer1\t\tPlayer2\t\tPlayer_1_time\t\tPlayer_2_time\t\tWinner_time\t\tWinner")
        print("-" * 114)
        for x in b:
            print(f"{x[0]}\t\t{x[1]}\t\t{x[2]}\t\t\t{x[3]}\t\t\t{x[4]}\t\t\t{x[5]}")
    elif leader == 5:
        break
