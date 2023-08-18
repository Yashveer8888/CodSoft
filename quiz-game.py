import tkinter as tk
from tkinter import messagebox

quiz_questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["Berlin", "Madrid", "Paris", "Rome"],
        "correct_answer": "Paris"
    },
    {
        "question": "Which planet is known as the 'Red Planet'?",
        "choices": ["Venus", "Mars", "Jupiter", "Saturn"],
        "correct_answer": "Mars"
    },
    {
        "question": "Which gas do plants use for photosynthesis?",
        "choices": ["Carbon Dioxide", "Oxygen", "Hydrogen", "Nitrogen"],
        "correct_answer": "Carbon Dioxide"
    },
    {
        "question": "What is the largest mammal?",
        "choices": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
        "correct_answer": "Blue Whale"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "choices": ["Au", "Ag", "G", "Go"],
        "correct_answer": "Au"
    },
    {
        "question": "Which planet is known as the 'Morning Star' or 'Evening Star'?",
        "choices": ["Venus", "Mars", "Mercury", "Jupiter"],
        "correct_answer": "Venus"
    },
    {
        "question": "What is the smallest prime number?",
        "choices": ["0", "1", "2", "3"],
        "correct_answer": "2"
    },
    {
        "question": "Which gas gives soda its fizz?",
        "choices": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"],
        "correct_answer": "Carbon Dioxide"
    },
    {
        "question": "What is the capital of Japan?",
        "choices": ["Tokyo", "Beijing", "Seoul", "Kyoto"],
        "correct_answer": "Tokyo"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "choices": ["Mars", "Jupiter", "Saturn", "Neptune"],
        "correct_answer": "Jupiter"
    }
]

current_question = 0
score = 0

def submit_answer():
    user_answer = var.get()
    correct_answer = quiz_questions[current_question]["correct_answer"]
    
    if user_answer == quiz_questions[current_question]["choices"].index(correct_answer):
        global score
        score += 1
        feedback_label.config(text="Correct!", fg="green")
    else:
        feedback_label.config(text=f"Incorrect. The correct answer is: {correct_answer}", fg="red")
    
    next_question_button.config(state=tk.NORMAL)

def next_question():
    global current_question
    current_question += 1
    if current_question < len(quiz_questions):
        question_label.config(text=quiz_questions[current_question]["question"])
        for i, choice in enumerate(quiz_questions[current_question]["choices"]):
            radio_buttons[i].config(text=choice)
        feedback_label.config(text="")
        next_question_button.config(state=tk.DISABLED)
        var.set(-1)
    else:
        messagebox.showinfo("Quiz Finished", f"Quiz finished! Your score: {score}/{len(quiz_questions)}")
        root.destroy()

root = tk.Tk()
root.title("Quiz Game")

question_label = tk.Label(root, text=quiz_questions[current_question]["question"])
question_label.pack(pady=10)

var = tk.IntVar()
var.set(-1)

radio_buttons = []
for i, choice in enumerate(quiz_questions[current_question]["choices"]):
    radio = tk.Radiobutton(root, text=choice, variable=var, value=i)
    radio_buttons.append(radio)
    radio.pack()

submit_button = tk.Button(root, text="Submit", command=submit_answer)
submit_button.pack(pady=10)

feedback_label = tk.Label(root, text="", fg="green")
feedback_label.pack()

next_question_button = tk.Button(root, text="Next Question", command=next_question, state=tk.DISABLED)
next_question_button.pack(pady=10)

root.mainloop()
