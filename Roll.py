import random

def roll_dice():
    """Simulate rolling two six-sided dice."""
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1, die2
def main():
    """Main function to roll dice and display the result."""
    die1, die2 = roll_dice()
    print(f"You rolled a {die1} and a {die2}. Total: {die1 + die2}")
if __name__ == "__main__":
    main()
input("Press Enter to roll the dice...")