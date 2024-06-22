import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import secrets
import string

# Function to generate password
def generate_password():
    try:
        # Get the desired length of the password
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("Warning", "Password length should be at least 4.")
            return
        
        if pronounceable.get():
            password = generate_pronounceable_password(length)
        else:
            # Define the character sets based on user selections
            characters = ""
            if use_letters.get():
                characters += string.ascii_letters
            if use_digits.get():
                characters += string.digits
            if use_punctuation.get():
                characters += string.punctuation

            # Ensure at least one character set is selected
            if not characters:
                messagebox.showwarning("Warning", "Select at least one character type.")
                return

            # Generate a random password
            password = ''.join(secrets.choice(characters) for _ in range(length))

        # Display the password
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
        
        # Calculate and display password strength
        strength = calculate_strength(password)
        strength_label.config(text=f"Strength: {strength}/5")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for the password length.")

# Function to generate pronounceable password
def generate_pronounceable_password(length):
    vowels = 'aeiou'
    consonants = ''.join(set(string.ascii_lowercase) - set(vowels))
    password = ''
    for i in range(length):
        if i % 2 == 0:
            password += secrets.choice(consonants)
        else:
            password += secrets.choice(vowels)
    return password

# Function to calculate password strength
def calculate_strength(password):
    strength = 0
    if len(password) >= 8:
        strength += 1
    if any(char.islower() for char in password):
        strength += 1
    if any(char.isupper() for char in password):
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char in string.punctuation for char in password):
        strength += 1
    return strength

# Set up the main application window
root = tk.Tk()
root.title("Password Generator by samar")
root.geometry("450x550")
root.resizable(False, False)
root.config(bg="#f9f9f9")

# Style the widgets
style = ttk.Style()
style.configure('TLabel', font=('Comic Sans MS', 12), background="#f9f9f9", foreground="#4b2e83", padding=10)
style.configure('TEntry', font=('Comic Sans MS', 12), foreground="#4b2e83", padding=10)
style.configure('TCheckbutton', font=('Comic Sans MS', 12), background="#f9f9f9", foreground="#4b2e83")

# Create a vibrant frame for the input and options
frame = ttk.Frame(root, padding="20 20 20 20", style='TFrame')
frame.pack(fill='both', expand=True)

# Create a label for the length input
length_label = ttk.Label(frame, text="Password Length:", style='TLabel')
length_label.grid(column=0, row=0, sticky='w', padx=10, pady=10)

# Create an entry widget for the length input
length_entry = ttk.Entry(frame, width=10, style='TEntry')
length_entry.grid(column=1, row=0, padx=10, pady=10)

# Create checkboxes for complexity options
use_letters = tk.BooleanVar(value=True)
use_digits = tk.BooleanVar(value=True)
use_punctuation = tk.BooleanVar(value=True)
pronounceable = tk.BooleanVar(value=False)

letters_check = ttk.Checkbutton(frame, text="Include Letters", variable=use_letters, style='TCheckbutton')
letters_check.grid(column=0, row=1, sticky='w', padx=10, pady=5)

digits_check = ttk.Checkbutton(frame, text="Include Digits", variable=use_digits, style='TCheckbutton')
digits_check.grid(column=0, row=2, sticky='w', padx=10, pady=5)

punctuation_check = ttk.Checkbutton(frame, text="Include Punctuation", variable=use_punctuation, style='TCheckbutton')
punctuation_check.grid(column=0, row=3, sticky='w', padx=10, pady=5)

pronounceable_check = ttk.Checkbutton(frame, text="Generate Pronounceable", variable=pronounceable, style='TCheckbutton')
pronounceable_check.grid(column=0, row=4, sticky='w', padx=10, pady=5)

# Create a colorful button to generate the password
generate_button = tk.Button(frame, text="Generate Password", command=generate_password, font=('Comic Sans MS', 12, 'bold'), bg="#ff5a5f", fg="white", activebackground="#ff6f61", activeforeground="white", bd=0, padx=10, pady=10)
generate_button.grid(column=0, row=5, columnspan=2, padx=10, pady=20)

# Create an entry widget to display the generated password
password_entry = ttk.Entry(frame, width=40, style='TEntry')
password_entry.grid(column=0, row=6, columnspan=2, padx=10, pady=5)

# Create a label to display the password strength
strength_label = ttk.Label(frame, text="Strength: 0/5", style='TLabel')
strength_label.grid(column=0, row=7, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()
