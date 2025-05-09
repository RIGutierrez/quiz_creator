import tkinter as tk
from tkinter import messagebox
import random
from playsound import playsound
import os
from PIL import Image, ImageTk

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

def play_sound(filename):
    try:
        path = os.path.join(os.path.dirname(__file__), filename)
        playsound(path)
    except Exception as error:
        print(f"[Sound Error] {error}") 


class UI:
    def __init__(self, master):
        root.configure(background='#FFCCCC')
        self.master = master
        self.master.title("QUIZ PLAYER")
        self.master.geometry("500x400")
        self.score = 0
        self.total = 0
        self.questions = load_questions()
        self.current_question = None

        self.question_label = tk.Label(
            master,
            text="",
            font=("Cooper Black", 14),
            wraplength=480,
            justify="left",
            foreground="gray20",
            background="#FFCCCC"
        )
        self.question_label.pack(pady=20)

        self.buttons = {}

        color_map = {
            'a': '#A3C4F3',
            'b': '#A0E7E5',
            'c': '#FFF6A3',
            'd': '#FFAFCC'
        }

        for key in ['a', 'b', 'c', 'd']:
            btn = tk.Button(
                master,
                text="",
                font=("Cooper Black", 12),
                width=30,
                fg="gray20",       
                bg=color_map[key],              
                activebackground="gray20",
                activeforeground="white",
                command=lambda answer_key=key: self.check_answer(answer_key)
                
            )
            btn.pack(pady=5)
            self.buttons[key] = btn

        self.score_label = tk.Label(
            master,
            text="Score: 0/0",
            font=("Cooper Black", 12),
            fg="white",
            bg="#FFCCCC"
        )
        self.score_label.pack(pady=10)

        self.next_button = tk.Button(
            master,
            text="Next Question",
            font=("Cooper Black", 12),
            command=self.next_question,
            fg="white",
            bg="gray20",
            activebackground="gray40"
        )
        self.next_button.pack(pady=10)

        self.next_question()

    def show_image_popup(self, image_path, title="Result"):
        popup = tk.Toplevel(self.master)
        popup.title(title)
        popup.configure(bg="white")

        img = Image.open(image_path)
        img = img.resize((200, 200))  # Resize for display
        photo = ImageTk.PhotoImage(img)

        label = tk.Label(popup, image=photo, bg="white")
        label.image = photo  # Keep a reference!
        label.pack(padx=20, pady=20)

        close_btn = tk.Button(popup, text="Close", command=popup.destroy)
        close_btn.pack(pady=10)

        # Center the popup window near main window
        popup.geometry("+%d+%d" % (self.master.winfo_rootx() + 100, self.master.winfo_rooty() + 100))


    def next_question(self):
        play_sound("next_button.mp3")

        if not self.questions:
            self.question_label.config(text="No questions available.")
            return

        self.current_question = random.choice(self.questions)
        question_data = self.current_question
        self.question_label.config(text=f"Q: {question_data['question']}")
        for key in ['a', 'b', 'c', 'd']:
            self.buttons[key].config(text=f"{key}) {question_data['choices'][key]}", state="normal")

    def flash_background(self, color, duration=200):
        original_color = self.master.cget("bg")
        self.master.config(bg=color)
        self.master.after(duration, lambda: self.master.config(bg=original_color))


    def check_answer(self, selected_key):
        correct = self.current_question['answer']
        if selected_key == correct:
            self.flash_background("green")
            play_sound("correct.mp3")
            messagebox.showinfo("Result", "Correct!")
            self.score += 1
        else:
            self.flash_background("red")
            play_sound("wrong.mp3")
            correct_text = self.current_question['choices'][correct]
            messagebox.showerror("Result", f"Wrong!\nCorrect answer: {correct}) {correct_text}")
              
        self.total += 1
        self.score_label.config(text=f"Score: {self.score}/{self.total}")
        for btn in self.buttons.values():
            btn.config(state="disabled")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = UI(root)
    root.mainloop()