import tkinter as tk
from tkinter import messagebox
import random

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.create_widgets()
        self.word_list = [
            "PYTHON", "TKINTER", "HANGMAN", "DEVELOPER", "PROGRAMMING", "ALGORITHM", 
            "DATABASE", "APPLICATION", "MACHINE", "LEARNING", "ARTIFICIAL", "INTELLIGENCE",
            "COMPUTER", "SCIENCE", "TECHNOLOGY", "INNOVATION", "ENGINEERING", "SOFTWARE",
            "HARDWARE", "DEBUGGING", "SCRIPT", "CODE", "DEBUG", "FUNCTION", "VARIABLE", 
            "OBJECT", "CLASS", "MODULE", "PACKET", "NETWORK", "SECURITY", "ENCRYPTION", 
            "DECRYPTION", "SERVER", "CLIENT", "USER", "INTERFACE", "ALGORITHM", "RECURSION",
            "SYNCHRONIZATION", "MULTITHREADING", "CONCURRENCY", "PARALLEL", "COMPUTATION",
            "DEBUGGER", "EXCEPTION", "FRAMEWORK", "LIBRARY", "API", "JSON", "XML", 
            "WEB", "SERVER", "CLIENT", "REQUEST", "RESPONSE", "ENDPOINT", "ROUTING", 
            "URL", "SESSION", "COOKIE", "AUTHENTICATION", "AUTHORIZATION", "TOKEN", "LOGIN",
            "LOGOUT", "PERMISSION", "DATABASE", "SQL", "NOSQL", "QUERY", "INDEX", 
            "TRANSACTION", "BACKUP", "RESTORE", "REPLICATION", "SHARDING", "OPTIMIZATION",
            "SCALABILITY", "ARCHITECTURE", "DESIGN", "PATTERN", "BEST", "PRACTICES"
        ]
        self.reset_game()

    def create_widgets(self):
        # Headline
        self.headline = tk.Label(self.root, text="All the words are computer science related", 
                                 font=("Courier", 16, "bold"), fg="white", bg="black")
        self.headline.pack(fill=tk.X, pady=10)

        # Word Display
        self.word_display = tk.Label(self.root, text="", font=("Courier", 28, "bold"), fg="blue")
        self.word_display.pack(pady=20)

        # Hangman Canvas
        self.hangman_canvas = tk.Canvas(self.root, width=200, height=200, bg="white")
        self.hangman_canvas.pack(pady=20)

        # Guessed Letters Display
        self.guessed_letters_display = tk.Label(self.root, text="Guessed Letters:", font=("Courier", 18), fg="red")
        self.guessed_letters_display.pack(pady=10)

        # Hint Display
        self.hint_display = tk.Label(self.root, text="Hint: (3 remaining)", font=("Courier", 14), fg="green")
        self.hint_display.pack(pady=10)

        # Entry and Buttons
        self.entry = tk.Entry(self.root, font=("Arial", 18))
        self.entry.pack(pady=10)
        self.submit_button = tk.Button(self.root, text="Submit Guess", command=self.submit_guess)
        self.submit_button.pack(pady=10)

        self.hint_button = tk.Button(self.root, text="Get Hint", command=self.give_hint)
        self.hint_button.pack(pady=10)

        self.restart_button = tk.Button(self.root, text="Restart Game", command=self.reset_game)
        self.restart_button.pack(pady=10)
        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.quit)
        self.exit_button.pack(pady=10)

    def reset_game(self):
        self.word = random.choice(self.word_list)
        self.guessed_letters = set()
        self.attempts = 0
        self.max_attempts = 6
        self.hints_remaining = 3
        self.update_word_display()
        self.hint_display.config(text=f"Hint: ({self.hints_remaining} remaining)")
        self.draw_hangman(self.attempts)

    def update_word_display(self):
        display_word = ' '.join([letter if letter in self.guessed_letters else '_' for letter in self.word])
        self.word_display.config(text=display_word)

    def submit_guess(self):
        guess = self.entry.get().upper()
        if guess and len(guess) == 1 and guess.isalpha():
            if guess in self.guessed_letters:
                messagebox.showinfo("Info", "You already guessed that letter.")
            elif guess in self.word:
                self.guessed_letters.add(guess)
                self.update_word_display()
                if set(self.word) == self.guessed_letters:
                    messagebox.showinfo("Congratulations", "You won!")
                    self.reset_game()
            else:
                self.attempts += 1
                self.draw_hangman(self.attempts)
                if self.attempts >= self.max_attempts:
                    messagebox.showinfo("Game Over", f"You lost! The word was {self.word}.")
                    self.reset_game()
        else:
            messagebox.showwarning("Invalid Input", "Please enter a single letter.")

    def give_hint(self):
        if self.hints_remaining > 0:
            unguessed_letters = [letter for letter in self.word if letter not in self.guessed_letters]
            if unguessed_letters:
                hint_letter = random.choice(unguessed_letters)
                self.hint_display.config(text=f"Hint: {hint_letter} ({self.hints_remaining - 1} remaining)")
                self.hints_remaining -= 1
            else:
                self.hint_display.config(text="No more hints available!")
        else:
            self.hint_display.config(text="No more hints available!")

    def draw_hangman(self, stage):
        self.hangman_canvas.delete("all")
        if stage >= 1:
            self.hangman_canvas.create_line(100, 150, 100, 50, width=2)
            self.hangman_canvas.create_line(50, 50, 150, 50, width=2)
        if stage >= 2:
            self.hangman_canvas.create_line(150, 50, 150, 80, width=2)
        if stage >= 3:
            self.hangman_canvas.create_oval(130, 80, 170, 120, width=2)
        if stage >= 4:
            self.hangman_canvas.create_line(150, 120, 150, 150, width=2)
        if stage >= 5:
            self.hangman_canvas.create_line(130, 150, 170, 150, width=2)
        if stage >= 6:
            self.hangman_canvas.create_line(130, 80, 150, 60, width=2)
            self.hangman_canvas.create_line(150, 60, 170, 80, width=2)

if __name__ == "__main__":
    root = tk.Tk()
    app = HangmanGame(root)
    root.mainloop()
