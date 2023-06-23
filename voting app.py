print("WELCOME TO THE VOTING APP \n")
import json

# Define the candidates and their vote counts
candidates = {
    "Alice": 0,
    "Bob": 0,
    "Charlie": 0
}

# Create a function to display the menu and get user input
def show_menu():
    print("\n===== Voting App =====")
    print("1. Vote for Alice")
    print("2. Vote for Bob")
    print("3. Vote for Charlie")
    print("4. View Results")
    print("5. Quit")
    choice = input("Enter your choice (1-5): ")
    return choice

# Create a function to handle the voting process
def vote(candidate):
    if candidate in candidates:
        candidates[candidate] += 1
        print("Vote for", candidate, "registered.")
    else:
        print("Invalid candidate.")

# Create a function to display the results
def show_results():
    print("\n===== Voting Results =====")
    for candidate, votes in candidates.items():
        print(candidate, "-", votes)

# Load any previously saved votes from a file
try:
    with open("votes.json", "r") as f:
        candidates = json.load(f)
    print("Votes loaded from file.")
except FileNotFoundError:
    print("No saved votes found.")

# Run the main loop of the program
while True:
    choice = show_menu()
    if choice == "1":
        vote("Alice")
    elif choice == "2":
        vote("Bob")
    elif choice == "3":
        vote("Charlie")
    elif choice == "4":
        show_results()
    elif choice == "5":
        # Save the votes to a file and exit the program
        with open("votes.json", "w") as f:
            json.dump(candidates, f)
        print("Votes saved to file. Exiting.")
        break
    else:
        print("Invalid choice. Try again.")
