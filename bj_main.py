from bj_func import Deck, player_input, current_count, replay

print("Welcome to the BlackJack Table!")
balance = 0

while True:
    bet = int(input("Enter your bet amount: "))

    mydeck = Deck()
    mydeck.shuffle()

    mydeck.deal_list = []
    mydeck.player_list = []

    mydeck.deal()
    print(f"Dealer drew a {mydeck.deal_list[-1]}")
    mydeck.player_deal()
    mydeck.player_deal()
    print(f"You drew {mydeck.player_list[-1]} and {mydeck.player_list[-2]}")

    player_score = current_count(mydeck.player_list)
    print(f"You currently have {player_score}")

    selection = player_input()
    while selection == "Y" and player_score < 21:
        mydeck.player_deal()
        print(f"You drew {mydeck.player_list[-1]}")
        player_score = current_count(mydeck.player_list)
        print(f"You currently have {player_score}")
        if player_score >= 21:
            break
        selection = player_input()

    dealer_score = current_count(mydeck.deal_list)
    while dealer_score < 17 and player_score <= 21:
        mydeck.deal()
        print(f"Dealer drew a {mydeck.deal_list[-1]}")
        dealer_score = current_count(mydeck.deal_list)
        print(f"Dealer has {dealer_score}")

    if player_score > 21:
        print("You Bust! You Lose!")
        balance -= bet
    elif dealer_score > 21:
        print("Dealer Busts! You Win!")
        balance += bet
    elif player_score == dealer_score:
        print("It's a Push! No one wins.")
    elif player_score > dealer_score:
        print("You Win!")
        balance += bet
    else:
        print("You Lose!")
        balance -= bet

    print(f"Your table balance is $ {balance}")

    if not replay():
        print("Thank you for playing!")
        break
