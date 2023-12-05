#import required modules
import tkinter as tk
import difflib
import time
import random

class TypingTestApp:
    def __init__(self, master, original):
        self.master = master
        self.master.title("Welcome to the Typing Speed Challenge! Ready,set,type!")

        self.original = original
        self.user_input = tk.StringVar()
        self.accuracy_var = tk.StringVar()
        self.speed_var = tk.StringVar()
        self.errors_var = tk.StringVar()

        self.start_time = None
        self.total_errors = 0
        
        #display original text
        self.original_label = tk.Label(master, height=4,text=f"Original Text: {original}")
        self.original_label.pack()
        
        #Accept input
        self.result_label = tk.Label(master, text="Type Here")
        self.result_label.pack()

        self.entry = tk.Entry(master, textvariable=self.user_input,width=80)
        self.entry.pack(pady=10,ipadx=20,ipady=20)

        self.text_widget = tk.Text(master, height=5, wrap=tk.WORD, width=50,state=tk.DISABLED)
        self.text_widget.pack()

        self.accuracy_label = tk.Label(master, textvariable=self.accuracy_var)
        self.accuracy_label.pack()

        self.speed_label = tk.Label(master, textvariable=self.speed_var)
        self.speed_label.pack()

        self.errors_label = tk.Label(master, textvariable=self.errors_var)
        self.errors_label.pack()

        self.check_button = tk.Button(master, text="Check", command=self.check_typing)
        self.check_button.pack()

        #tags for highlighting the error
        self.text_widget.tag_configure("correct", background="white")
        self.text_widget.tag_configure("wrong", background="pink")

    def check_typing(self):
        user_input = self.user_input.get()
        self.text_widget.configure(state=tk.NORMAL)
        self.text_widget.delete("1.0", tk.END)
        self.text_widget.insert(tk.END, self.original)
        self.text_widget.configure(state=tk.DISABLED)

        typing_time = time.time() - self.start_time
        words_per_minute = (len(user_input.split()) / typing_time) * 60  # words per minute
        self.speed_var.set(f"Speed: {words_per_minute:.2f} WPM")  # Display typing speed

        diff = list(difflib.ndiff(self.original, user_input))
        pos = "1.0"

        for item in diff:
            if item.startswith(' '):
                pos = self.tag_text("correct", pos, len(item))
            elif item.startswith('-'):
                pos = self.tag_text("wrong", pos, len(item))
            elif item.startswith('+'):
                self.text_widget.insert(tk.END, item[2:], "correct")  # Add correct words directly
                pos = self.tag_text("correct", pos, len(item))

        correct_characters = sum(1 for a, b in zip(self.original, user_input) if a == b)
        accuracy = (correct_characters / len(self.original)) * 100
        self.accuracy_var.set(f"Accuracy: {accuracy:.2f}%")#display accuracy

        if user_input.strip() == self.original.strip():
            self.result_label.config(text="You typed the correct string!")

        else:
            self.total_errors += 1
            
    def tag_text(self, tag, pos, length):
        end_pos = f"{pos}+{length}c"
        self.text_widget.tag_add(tag, pos, end_pos)
        return end_pos

    def start_typing_test(self):
        self.start_time = time.time()


words = ["practice", "typing", "speed", "tester", "improve", "accuracy",  "challenge", "keyboard"]
original_string= ' '.join(random.choices(words, k=5))
root = tk.Tk()
app = TypingTestApp(root, original_string)
app.start_typing_test()
root.mainloop()

