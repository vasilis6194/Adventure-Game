import time
import random


def delay_print(message):
    print(message)
    time.sleep(2)


def game_intro(villain):
    delay_print("You are on a quest to find Pokemon in the city, "
                "amidst towering buildings and broad streets.")
    delay_print(f"Rumor has it that {villain} is lurking around here, "
                "causing fear among the locals.")
    delay_print("Ahead of you is a house, just 50 meters away.")
    delay_print("To your right, there's a Yu-Gi-Oh card shop.")
    delay_print("In your hand, you clutch your trusty (but not very powerful) "
                "Pokeball containing Bulbasaur.")


def get_user_choice(option1, option2, prompt):
    while True:
        choice = input(prompt)
        if choice in (option1, option2):
            break
    return choice


def city_street(pokemon, villain):
    delay_print("\nEnter 1 to knock on the door of the house.")
    delay_print("Enter 2 to go into the Yu-Gi-Oh card shop.")
    delay_print("What would you like to do?")
    choice = get_user_choice("1", "2", "(Please enter 1 or 2.)\n")
    if choice == "1":
        explore_house(pokemon, villain)
    elif choice == "2":
        explore_shop(pokemon, villain)


def engage_battle(option1, option2, pokemon, villain):
    choice = get_user_choice("1", "2", "Do you want to"
                             " (1) fight or (2) run away?")
    if choice == option1:
        if "Charizard" in pokemon:
            delay_print(
                f"As {villain} moves to attack, you "
                "release your new Pokemon."
            )
            delay_print(
                "Charizard breathes fire with such "
                "intensity that it melts everything."
            )
            delay_print(f"{villain} is terrified by the"
                        " sight of this orange beast.")
            delay_print(
                "You, your Bulbasaur, and all the other "
                "Pokemon trainers are now safe from "
                f"{villain}."
            )
        else:
            delay_print(
                f"Bulbasaur fights bravely but is no match for {villain}."
            )
            delay_print("You have been defeated and Bulbasaur is scared.")
    elif choice == option2:
        delay_print(
            "Knowing you're not strong enough,"
            " you flee back to the city's wide streets."
        )
        city_street(pokemon, villain)


def explore_house(pokemon, villain):
    delay_print("You approach the door of the house.")
    delay_print(
        f"As you are about to knock, the"
        " door opens and {villain} steps out."
    )
    delay_print(f"Eep! This is {villain}'s house!")
    delay_print(f"{villain} attacks you.")
    if "Charizard" not in pokemon:
        delay_print(
            "You realize you are not prepared"
            " for this battle with just Bulbasaur."
        )
    engage_battle("1", "2", pokemon, villain)


def explore_shop(pokemon, villain):
    delay_print("You enter the Yu-Gi-Oh card shop.")
    if "Charizard" in pokemon:
        delay_print(
            "You've been here before, and Charizard is all you need right now."
        )
    else:
        delay_print("You are impressed by the shop's"
                    " design and can't help but smile.")
        delay_print("You hear a strange noise coming from the upper floor.")
        delay_print("You go upstairs and see something unbelievable.")
        delay_print("A powerful dragon is roaring"
                    " and looking directly at you.")
        delay_print(
            "You quickly use the MasterBall "
            "from your backpack to catch Charizard."
        )
        pokemon.append("Charizard")
    delay_print("You walk back out to the city's broad streets.")
    city_street(pokemon, villain)


def replay_game():
    choice = get_user_choice(
        "y", "n", "Would you like to play again? (y/n)"
    )
    if choice == "y":
        delay_print("Great! Restarting the game...")
        start_game()
    elif choice == "n":
        delay_print("Thanks for playing! See you next time.")


def start_game():
    villain = random.choice(["Team Rocket", "Giovanni",
                            "James", "Jessie", "Meowth"])
    pokemon = []
    game_intro(villain)
    city_street(pokemon, villain)
    replay_game()


start_game()
