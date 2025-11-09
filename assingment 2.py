import random

players = {}

def register_player():
    name = input("Enter player name: ")
    if name in players:
        print("Player already registered!")
    else:
        players[name] = {"score": 0, "games_played": 0}
        print(f"Player '{name}' registered successfully!")

def play_game():
    name = input("Enter player name: ")
    if name in players:
        print(f"Starting game for {name}...")
        score = random.randint(0, 100)
        players[name]["score"] += score
        players[name]["games_played"] += 1
        print(f"{name} scored {score} points!")
    else:
        print("Player not found! Please register first.")

def update_player():
    name = input("Enter player name to update: ")
    if name in players:
        new_name = input("Enter new name: ")
        players[new_name] = players.pop(name)
        print(f"Player name updated to '{new_name}'!")
    else:
        print("Player not found!")

def delete_player():
    name = input("Enter player name to delete: ")
    if name in players:
        del players[name]
        print(f"Player '{name}' deleted successfully!")
    else:
        print("Player not found!")

def game_statistics():
    if players:
        print("\n--- Game Statistics ---")
        for name, info in players.items():
            print(f"Name: {name}, Score: {info['score']}, Games Played: {info['games_played']}")
    else:
        print("No player data available.")

while True:
    print("\n=== Game Menu ===")
    print("1. Register Player")
    print("2. Play Game")
    print("3. Update Player Info")
    print("4. Delete Player Record")
    print("5. Game Statistics")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        register_player()
    elif choice == "2":
        play_game()
    elif choice == "3":
        update_player()
    elif choice == "4":
        delete_player()
    elif choice == "5":
        game_statistics()
    elif choice == "6":
        print("Exiting program... thank you for playing bye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
