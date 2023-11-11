import random
import string
from words import words
from tkinter import *
from tkinter import messagebox

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman_gui():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6

    root = Tk()
    root.title("Hangman")

    # Create a canvas to draw the hangman
    canvas = Canvas(root, width=300, height=400)
    canvas.pack()

    def draw_hangman():
        if lives == 6:
            canvas.create_line(100, 200, 150, 200)
        elif lives == 5:
            canvas.create_line(150, 200, 150, 100)
        elif lives == 4:
            canvas.create_line(150, 100, 120, 70)
        elif lives == 3:
            canvas.create_line(150, 100, 180, 70)
        elif lives == 2:
            canvas.create_line(150, 150, 120, 180)
        elif lives == 1:
            canvas.create_line(150, 150, 180, 180)

    draw_hangman()

    # Create a label to display the lives left
    lives_label = Label(root, text="Lives: " + str(lives))
    lives_label.pack()

    # Create a label to display the used letters
    used_letters_label = Label(root, text="Used Letters: ")
    used_letters_label.pack()

    # Create a label to display the current word
    current_word = ['-' if letter.isalpha() else letter for letter in word]
    word_label = Label(root, text="Current Word: " + ' '.join(current_word))
    word_label.pack()

    def enter_letter():
        nonlocal lives
        nonlocal used_letters

        user_letter = letter_entry.get().upper()
        letter_entry.delete(0, END)

        if user_letter and user_letter.isalpha() and len(user_letter) == 1:
            if user_letter in alphabet - used_letters:
                used_letters.add(user_letter)
                if user_letter in word_letters:
                    word_letters.remove(user_letter)
                    current_word = [letter if letter in used_letters else '-' for letter in word]
                    word_label['text'] = "Current Word: " + ' '.join(current_word)
                else:
                    lives -= 1
                    lives_label['text'] = "Lives: " + str(lives)
                    draw_hangman()

                used_letters_label['text'] = "Used Letters: " + ' '.join(used_letters)

                if lives == 0:
                    messagebox.showinfo("Game over", "You lost! The word was " + word)
                    root.destroy()
                elif len(word_letters) == 0:
                    messagebox.showinfo("Congratulations", "You won! You guessed the word " + word)
                    root.destroy()
            else:
                messagebox.showinfo("Invalid letter", "Letter already used")
        else:
            messagebox.showinfo("Invalid input", "Please enter a single letter")

    # Create an entry field for the user to enter a letter
    letter_entry = Entry(root)
    letter_entry.pack()
    letter_entry.bind('<Return>', enter_letter)

    # Create a button to submit the letter
    submit_button = Button(root, text="Submit", command=enter_letter)
    submit_button.pack()

    root.mainloop()

hangman_gui()
