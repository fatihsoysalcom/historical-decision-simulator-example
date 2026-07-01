#!/usr/bin/env python3

import sys

def run_simulation():
    # Initial state of the player/kingdom
    player_state = {
        "gold": 1000,
        "food": 500,
        "morale": 70,
        "reputation": 60
    }

    print("\n--- The Lord's Dilemma: A Famine Strikes! ---")
    print("You are Lord Kael, ruler of the fertile lands of Eldoria. A harsh winter has passed, and your granaries are dangerously low. Your people face starvation.\n")

    # Display current state
    print("Current Status:")
    print(f"  Gold: {player_state['gold']}")
    print(f"  Food: {player_state['food']}")
    print(f"  Morale: {player_state['morale']} (out of 100)")
    print(f"  Reputation: {player_state['reputation']} (out of 100)\n")

    print("What is your decision, Lord Kael?\n")
    print("1. Open the Royal Vaults: Distribute emergency gold to buy food from neighboring lands. (Cost: 300 Gold, Gain: 200 Food, +10 Morale)")
    print("2. Impose a New Tax: Levy a temporary tax on all citizens to fund food purchases. (Cost: -15 Morale, Gain: 400 Gold, +100 Food)")
    print("3. Seek Aid from the Northern Kingdom: Send envoys to your old ally, King Theron, for immediate food relief. (Cost: -15 Reputation, Gain: 300 Food)")
    print("4. Do Nothing: Hope for an early spring and divine intervention. (Risk: -30 Morale, -10 Reputation, High chance of disaster)\n")

    # Decision-making loop
    while True:
        choice = input("Enter your choice (1, 2, 3, or 4): ").strip()
        if choice in ['1', '2', '3', '4']:
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

    # Process the decision and update state - This is where the core simulation logic resides
    print("\n--- Consequences of Your Decision ---")
    if choice == '1':
        player_state['gold'] -= 300
        player_state['food'] += 200
        player_state['morale'] += 10
        print("You opened the Royal Vaults. Your people are grateful for your generosity, though your treasury is lighter.")
    elif choice == '2':
        player_state['gold'] += 400
        player_state['food'] += 100
        player_state['morale'] -= 15
        print("You imposed a new tax. While food is secured, your people grumble about the burden.")
    elif choice == '3':
        player_state['reputation'] -= 15
        player_state['food'] += 300
        print("You sought aid from King Theron. He sent food, but your kingdom's reliance on others has slightly diminished your standing.")
    elif choice == '4':
        player_state['morale'] -= 30
        player_state['reputation'] -= 10
        # Introduce a random element for 'Do Nothing' to simulate risk
        import random
        if random.random() < 0.6: # 60% chance of severe consequences
            player_state['food'] -= 150 # Further food loss
            player_state['morale'] -= 20 # Even lower morale
            print("You did nothing. The famine worsened, and your people's despair grew. Whispers of rebellion can be heard.")
        else:
            print("You did nothing. Miraculously, an early spring arrived, and the worst of the famine was averted, though morale suffered.")

    # Ensure stats don't go below zero or above 100 for morale/reputation
    player_state['gold'] = max(0, player_state['gold'])
    player_state['food'] = max(0, player_state['food'])
    player_state['morale'] = max(0, min(100, player_state['morale']))
    player_state['reputation'] = max(0, min(100, player_state['reputation']))

    print("\n--- End of the Crisis ---")
    print("After your decision, the state of Eldoria is as follows:")
    print(f"  Gold: {player_state['gold']}")
    print(f"  Food: {player_state['food']}")
    print(f"  Morale: {player_state['morale']} (out of 100)")
    print(f"  Reputation: {player_state['reputation']} (out of 100)\n")

    # Final outcome based on overall state
    if player_state['morale'] < 30 or player_state['food'] < 100:
        print("Your kingdom is in a dire state. The future looks bleak, and your reign is in peril.")
    elif player_state['morale'] > 80 and player_state['food'] > 400:
        print("Your wise decision has saved Eldoria! Your people prosper, and your name will be remembered for generations.")
    else:
        print("Eldoria has weathered the storm, but challenges remain. Your leadership will continue to be tested.")

    print("\nThank you for playing!")

if __name__ == "__main__":
    try:
        run_simulation()
    except KeyboardInterrupt:
        print("\nSimulation interrupted. Goodbye!")
        sys.exit(0)
