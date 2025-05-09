filename ="input_questions_answer.txt"
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