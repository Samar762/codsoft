import tkinter as tk
from tkinter import PhotoImage
import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "user"
    else:
        return "computer"

# Function to update the result and score
def play(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)

    # Update the result label
    user_choice_label.config(image=images[user_choice])
    computer_choice_label.config(image=images[computer_choice])
    if result == "tie":
        outcome_label.config(text="It's a tie!", fg="gray")
    elif result == "user":
        outcome_label.config(text="You win!", fg="green")
        user_score += 1
    else:
        outcome_label.config(text="Computer wins!", fg="red")
        computer_score += 1

    # Update the score labels
    user_score_label.config(text=f"Your Score: {user_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")

# Function to reset the game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_score_label.config(text=f"Your Score: {user_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")
    outcome_label.config(text="")
    user_choice_label.config(image=empty_image)
    computer_choice_label.config(image=empty_image)

# Set up the main application window
root = tk.Tk()
root.title("Rock-Paper-Scissors")
root.geometry("420x350")
root.configure(bg="#f4f4f4")
root.resizable(False, False)

# Create a list of choices
choices = ['rock', 'paper', 'scissors']

# Load images for choices
images = {
    'rock': PhotoImage(file="rock.png"),
    'paper': PhotoImage(file="paper.png"),
    'scissors': PhotoImage(file="scissors.png")
}
empty_image = PhotoImage(file="empty.png")  # An empty image to show when no choice is made

# Initialize scores
user_score = 0
computer_score = 0

# Create and place labels
welcome_label = tk.Label(root, text="Rock-Paper-Scissors Game", font=("Helvetica", 16, "bold"), bg="#f4f4f4")
welcome_label.pack(pady=10)

frame = tk.Frame(root, bg="#f4f4f4")
frame.pack(pady=10)

user_choice_label = tk.Label(frame, text="", bg="#f4f4f4", image=empty_image)
user_choice_label.grid(row=0, column=0, padx=20)

vs_label = tk.Label(frame, text="VS", font=("Helvetica", 16, "bold"), bg="#f4f4f4")
vs_label.grid(row=0, column=1, padx=20)

computer_choice_label = tk.Label(frame, text="", bg="#f4f4f4", image=empty_image)
computer_choice_label.grid(row=0, column=2, padx=20)

outcome_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"), bg="#f4f4f4")
outcome_label.pack(pady=5)

score_frame = tk.Frame(root, bg="#f4f4f4")
score_frame.pack(pady=10)

user_score_label = tk.Label(score_frame, text=f"Your Score: {user_score}", font=("Helvetica", 12), bg="#f4f4f4")
user_score_label.grid(row=0, column=0, padx=10)

reset_button = tk.Button(score_frame, text="Reset", font=("Helvetica", 10), bg="#ffcccc", command=reset_game)
reset_button.grid(row=0, column=1, padx=10)

computer_score_label = tk.Label(score_frame, text=f"Computer Score: {computer_score}", font=("Helvetica", 12), bg="#f4f4f4")
computer_score_label.grid(row=0, column=2, padx=10)

# Create and place buttons
button_frame = tk.Frame(root, bg="#f4f4f4")
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock", image=images['rock'], compound="top", command=lambda: play('rock'))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="Paper", image=images['paper'], compound="top", command=lambda: play('paper'))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, text="Scissors", image=images['scissors'], compound="top", command=lambda: play('scissors'))
scissors_button.grid(row=0, column=2, padx=10)

# Start the Tkinter event loop
root.mainloop()
