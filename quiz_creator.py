import os

# clear screen for cleaner look when typing questions
os.system('cls' if os.name == 'nt' else 'clear')

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

# save the question, choices, and answer key as txt
filename = "input_questions_answer.txt"

with open(filename, "a", encoding="utf-8") as file:
    file.write(f"Q: {data['question']}\n")
    for key in ['a', 'b', 'c', 'd']:
        file.write(f"{key}) {data['choices'][key]}\n")
    file.write(f"Answer: {data['answer']}\n")
    file.write("-" * 30 + "\n\n")

print("\nYour inputted question has been recorded\n")

# use def and make a main loop
# add return function for question to return data as dictionary
# take parameters for saving question
# call main()