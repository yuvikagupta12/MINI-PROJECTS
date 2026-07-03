import random
import customtkinter as ctxt

# Set up the visual theme
ctxt.set_appearance_mode("dark")
ctxt.set_default_color_theme("blue")

class GuessGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("400x350")
        self.root.resizable(False, False)
        
        # Game variables
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        
        # Title Label
        self.title_label = ctxt.CTkLabel(
            root, 
            text="I am thinking of a number\nbetween 1 and 100.", 
            font=("Arial", 18, "bold")
        )
        self.title_label.pack(pady=20)
        
        # Input Field
        self.entry = ctxt.CTkEntry(
            root, 
            placeholder_text="Enter your guess", 
            width=150,
            justify="center"
        )
        self.entry.pack(pady=10)
        
        # Submit Button
        self.guess_button = ctxt.CTkButton(
            root, 
            text="Submit Guess", 
            command=self.check_guess
        )
        self.guess_button.pack(pady=10)
        
        # Feedback Label
        self.feedback_label = ctxt.CTkLabel(
            root, 
            text="Take your first guess!", 
            font=("Arial", 14)
        )
        self.feedback_label.pack(pady=20)
        
        # Reset Button (Hidden at start)
        self.reset_button = ctxt.CTkButton(
            root, 
            text="Play Again", 
            command=self.reset_game,
            fg_color="green",
            hover_color="darkgreen"
        )

    def check_guess(self):
        user_input = self.entry.get()
        
        # Validate that input is a number
        if not user_input.isdigit():
            self.feedback_label.configure(text="Please enter a valid number!", text_color="red")
            return
            
        guess = int(user_input)
        self.attempts += 1
        self.entry.delete(0, 'end') # Clear input field
        
        # Game logic
        if guess < self.secret_number:
            self.feedback_label.configure(text="Too low! Try a higher number.", text_color="orange")
        elif guess > self.secret_number:
            self.feedback_label.configure(text="Too high! Try a lower number.", text_color="orange")
        else:
            self.feedback_label.configure(
                text=f"🎉 Correct! You got it in {self.attempts} attempts!", 
                text_color="lightgreen"
            )
            self.end_game()

    def end_game(self):
        self.guess_button.configure(state="disabled")
        self.entry.configure(state="disabled")
        self.reset_button.pack(pady=10)

    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.entry.configure(state="normal")
        self.guess_button.configure(state="normal")
        self.feedback_label.configure(text="Take your first guess!", text_color="white")
        self.reset_button.pack_forget()

# Run the application
if __name__ == "__main__":
    window = ctxt.CTk()
    game = GuessGame(window)
    window.mainloop()
