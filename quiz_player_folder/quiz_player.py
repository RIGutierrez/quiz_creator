import tkinter as tk
from tkinter import messagebox
import random

def load_questions(filename="input_questions_answer.txt"):
    questions = []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()

        current_question = ""
        current_choices = {}
        current_answer = ""

        for line in lines:
            line = line.strip()

            if line.startswith("Question:"):
                current_question = line.replace("Question:", "").strip()
                current_choices = {}
            elif line.startswith(("a)", "b)", "c)", "d)")):
                key = line[0]
                value = line[2:].strip()
                current_choices[key] = value
            elif line.startswith("Answer Key:"):
                current_answer = line.replace("Answer Key:", "").strip()
            elif line.startswith("-" * 5):
                questions.append({
                    "question": current_question,
                    "choices": current_choices,
                    "answer": current_answer
                })

    except FileNotFoundError:
        print("'input_questions_answer.txt' not found. Please run the quiz creator.py")

    return questions   

class UI:
    def __init__(self, master):
        root.configure(background='black')
        self.master = master
        self.master.title("QUIZ PLAYER")
        self.master.geometry("500x400")
        self.score = 0
        self.total = 0
        self.questions = load_questions()
        self.current_question = None

        self.question_label = tk.Label(master, text="", font=("Arial", 14), wraplength=480, justify="left")
        self.question_label.pack(pady=20)

        self.buttons = {}
        for key in ['a', 'b', 'c', 'd']:
            btn = tk.Button(master, text="", font=("Arial", 12), width=30)
            btn.pack(pady=5)
            self.buttons[key] = btn

        self.score_label = tk.Label(master, text="Score: 0/0", font=("Arial", 12))
        self.score_label.pack(pady=10)

        self.next_button = tk.Button(master, text="Next Question", font=("Arial", 12))
        self.next_button.pack(pady=10)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = UI(root)
    root.mainloop()