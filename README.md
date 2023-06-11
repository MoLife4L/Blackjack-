# Blackjack-

Deck Initialization: The deck of cards is represented using a Deck class. The deck is created with all possible cards and their corresponding values using the suits and values variables. The deck is initialized, shuffled, and ready for gameplay.

Game Flow: The game follows a standard blackjack flow. The player is prompted to enter a bet amount, and a new deck is initialized and shuffled. Cards are dealt to the dealer and the player.

Player's Turn: The player is then given the option to "hit" (draw another card) or "stand" (end their turn). The player_input function handles the player's decision. If the player chooses to hit, a card is dealt to the player, and their score is updated. This process continues until the player stands or busts (score exceeds 21).

Dealer's Turn: After the player finishes their turn, it's the dealer's turn. The dealer must draw cards until their score reaches 17 or higher. The dealer's score is updated accordingly.

Ace Handling: The current_count function calculates the current score of a hand by summing the values of the cards. It also handles the special case of Aces. If the hand contains an Ace and the score exceeds 21, the function adjusts the value of the Ace from 11 to 1 until the score is no longer greater than 21.

Determining the Outcome: Once both the player and the dealer have completed their turns, the scores are compared to determine the outcome of the game. If either the player or the dealer exceeds 21 (busts), the corresponding win/lose message is displayed. Otherwise, the scores are compared, and the appropriate win/lose message is displayed.

Balance Update: The player's table balance is updated based on the outcome of the game. The balance is increased if the player wins or the dealer busts, and decreased if the player loses or busts.

Replay: After each round, the player is prompted to play again. If the player chooses to continue, the game restarts with a new bet and a reshuffled deck. If the player chooses to quit, the program exits.

