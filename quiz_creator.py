import json

# ask user for question and choices
question = input("Enter your quiz question: ")

choices = {}
for letter in ['a', 'b', 'c', 'd']:
    choices[letter] = input(f"Enter choice {letter.upper()}: ")

# ask for correct answer
while True:
    answer = input("Enter the correct answer (a/b/c/d): ").lower()
    if answer in choices:
        break
    print("Invalid input. Please enter one of a, b, c, or d.")

# save the question, choices, and answer key as json
filename = "input_questions_answer.jsonl"
with open(filename, "a", encoding="utf-8") as file:
    file.write()