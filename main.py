import tkinter as tk
from tkinter import simpledialog, messagebox

class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flashcard Quiz App")

        self.flashcards = []
        self.current_card_index = 0
        self.score = 0

        # Create GUI components
        self.question_label = tk.Label(root, text="Question will appear here", font=("Helvetica", 16))
        self.question_label.pack(pady=20)

        self.answer_entry = tk.Entry(root, font=("Helvetica", 16))
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(root, text="Submit Answer", command=self.check_answer, font=("Helvetica", 14))
        self.submit_button.pack(pady=10)

        self.next_button = tk.Button(root, text="Next Question", command=self.next_question, font=("Helvetica", 14))
        self.next_button.pack(pady=10)

        self.score_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.score_label.pack(pady=20)

        # Add flashcards
        self.add_flashcards()

    def add_flashcards(self):
        while True:
            question = simpledialog.askstring("Input", "Enter question (or type 'done' to finish):", parent=self.root)
            if question is None or question.lower() == 'done':
                break
            answer = simpledialog.askstring("Input", f"Enter answer for: {question}", parent=self.root)
            self.flashcards.append(Flashcard(question, answer))

    def next_question(self):
        if self.current_card_index < len(self.flashcards):
            current_card = self.flashcards[self.current_card_index]
            self.question_label.config(text=current_card.question)
            self.answer_entry.delete(0, tk.END)
            self.score_label.config(text="")
        else:
            messagebox.showinfo("Quiz Complete", f"Your score: {self.score}/{len(self.flashcards)}")
            self.root.quit()

    def check_answer(self):
        if self.current_card_index < len(self.flashcards):
            current_card = self.flashcards[self.current_card_index]
            user_answer = self.answer_entry.get()
            if user_answer.lower() == current_card.answer.lower():
                messagebox.showinfo("Correct!", "Your answer is correct!")
                self.score += 1
            else:
                messagebox.showinfo("Wrong", f"Wrong! The correct answer is: {current_card.answer}")

            self.current_card_index += 1
            self.next_question()

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()
