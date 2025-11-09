import random
import mysql.connector
from datetime import datetime

# ---------- DATABASE CONNECTION ----------
def connect_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",          # <-- change this to your MySQL username
            password="123456",    # <-- change this to your MySQL password
            database="boardGameHub"
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Database connection error: {err}")
        return None


# ---------- PLAYER MANAGEMENT ----------
def register_player():
    conn = connect_db()
    if conn is None:
        return

    cursor = conn.cursor()
    while True:
        player_id = input("Enter Player ID (e.g. P001): ")
        name = input("Enter Player Name: ")

        try:
            cursor.execute("INSERT INTO players (player_id, name) VALUES (%s, %s)", (player_id, name))
            conn.commit()
            print(f"Player {name} registered successfully!\n")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cont = input("Register another player? (y/n): ").lower()
            if cont != 'y':
                break

    cursor.close()
    conn.close()


def update_player():
    conn = connect_db()
    if conn is None:
        return
    cursor = conn.cursor()

    player_id = input("Enter Player ID to update: ")
    new_name = input("Enter new player name: ")

    cursor.execute("UPDATE players SET name=%s WHERE player_id=%s", (new_name, player_id))
    conn.commit()

    if cursor.rowcount > 0:
        print("Player name updated successfully!\n")
    else:
        print("Player ID not found.\n")

    cursor.close()
    conn.close()


def delete_player():
    conn = connect_db()
    if conn is None:
        return
    cursor = conn.cursor()

    player_id = input("Enter Player ID to delete: ")
    cursor.execute("DELETE FROM players WHERE player_id=%s", (player_id,))
    conn.commit()

    if cursor.rowcount > 0:
        print("Player deleted successfully!\n")
    else:
        print("Player ID not found.\n")

    cursor.close()
    conn.close()


def list_players():
    conn = connect_db()
    if conn is None:
        return []
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM players")
    players = cursor.fetchall()
    cursor.close()
    conn.close()
    return players


# ---------- GAME LOGIC ----------
SNAKES = {16: 6, 48: 30, 64: 60, 79: 19, 93: 68, 95: 24, 97: 76}
LADDERS = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}


def roll_dice():
    try:
        return random.randint(1, 6)
    except Exception as e:
        print(f"Dice roll error: {e}")
        return 1


def play_game():
    players = list_players()
    if len(players) < 2:
        print("At least 2 players are required to start a game.\n")
        return

    positions = {pid: 0 for pid, _ in players}
    winner = None

    print("\n🎲 Game Start! 🎲\n")
    while not winner:
        for pid, name in players:
            input(f"{name}'s turn. Press Enter to roll the dice...")
            dice = roll_dice()
            print(f"{name} rolled a {dice}!")

            positions[pid] += dice
            if positions[pid] > 100:
                positions[pid] = 100

            if positions[pid] in SNAKES:
                print(f"Oh no! {name} got bitten by a snake!")
                positions[pid] = SNAKES[positions[pid]]
            elif positions[pid] in LADDERS:
                print(f"Yay! {name} climbed a ladder!")
                positions[pid] = LADDERS[positions[pid]]

            print(f"{name} is now at position {positions[pid]}\n")

            if positions[pid] == 100:
                winner = name
                break

    print(f"🏆 {winner} wins the game! 🏆\n")

    # Record game result in DB
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO games (winner, date_played) VALUES (%s, %s)", (winner, datetime.now()))
        conn.commit()
        cursor.close()
        conn.close()


# ---------- DISPLAY PROGRESS & STATISTICS ----------
def display_progress():
    players = list_players()
    if not players:
        print("No players registered.\n")
        return
    print("\nCurrent Players:\n----------------")
    for pid, name in players:
        print(f"{pid}: {name}")
    print("----------------\n")


def show_statistics():
    conn = connect_db()
    if conn is None:
        return
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*), GROUP_CONCAT(winner SEPARATOR ', ') FROM games")
    result = cursor.fetchone()

    print("\n📊 Game Statistics 📊")
    print(f"Total Games Played: {result[0]}")
    print(f"Winners: {result[1] if result[1] else 'No games played yet'}\n")

    cursor.close()
    conn.close()


# ---------- MAIN MENU ----------
def main_menu():
    while True:
        print("""
===== Snake and Ladder Game System =====
1. Register Player
2. Update Player Info
3. Delete Player
4. Display Players
5. Play Game
6. Game Statistics
7. Exit
========================================
        """)

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number.\n")
            continue

        if choice == 1:
            register_player()
        elif choice == 2:
            update_player()
        elif choice == 3:
            delete_player()
        elif choice == 4:
            display_progress()
        elif choice == 5:
            play_game()
        elif choice == 6:
            show_statistics()
        elif choice == 7:
            print("Exiting system... Goodbye!")
            break
        else:
            print("Invalid option! Please try again.\n")


# ---------- MAIN EXECUTION ----------
if __name__ == "__main__":
    print("Welcome to BoardGame Hub: Snake and Ladder System")
    main_menu()
