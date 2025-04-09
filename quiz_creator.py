# ask user for question, choices, answer
question = input("Enter your quiz question: ")

choices = {}
for letter in ['a', 'b', 'c', 'd']:
    choices[letter] = input(f"Enter choice {letter.upper()}: ")