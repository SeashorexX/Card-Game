import random

title = "Playing Card Generator".center(120) 
print(title)

print("\nGoal: Try to get the highest card\n")

rank = [2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"]
suit = ["Clubs","Diamonds","Hearts","Spades"]

def Combine(rank,suit):
    rand_rank = random.choice(rank)
    rand_suit = random.choice(suit) 
    card = (f"{rand_rank} of {rand_suit}")
    return card

while True:
    choice = input("Do you dare to try? (y/n): ").lower()

    if choice == "y":

         Player_Card = Combine(rank,suit)
         Opponent_Card = Combine(rank,suit)

         print(f"\nYour Card: {Player_Card}\n")
         print(f"Opponent Card: {Opponent_Card}\n")

         rank_values = {str(k): k for k in range(2, 11)}  
         rank_values.update({"Jack": 11, "Queen": 12, "King": 13, "Ace": 14})  
    

         player_rank = str(Player_Card.split()[0])
         opponent_rank = str(Opponent_Card.split()[0])

         if rank_values[player_rank] > rank_values[opponent_rank]:
             print("\nYou have the highest card. You Win!\n")
         elif rank_values[opponent_rank] > rank_values[player_rank]:
             print("\nYour Opponent has the highest card, You Lose\n")
         else:
             print("\nIt's a Draw!\n")

    elif choice == "n":
         print("\nThanks for Playing!\n")
         break
    else:
         print("\nInvalid choice!\n")
         

