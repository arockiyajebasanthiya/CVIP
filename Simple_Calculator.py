#QuickCalc

#Import tkinter as th
import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, master):
        #Initialize the GUI window
        self.master = master
        master.title("Calculator")
        
        #Initialize a StringVar to store the result
        self.result_var = tk.StringVar()
        self.result_var.set("")
        
        #Create an entery widget to display
        self.entry = tk.Entry(master, textvariable=self.result_var, font=('Arial', 14), justify='right')
        self.entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]

        row_val, col_val = 1, 0
        
        #Add buttons to the GUI
        for button_text in buttons:
            button = tk.Button(master, text=button_text, padx=20, pady=20, font=('Arial', 14),
                               command=lambda ch=button_text: self.on_button_click(ch))
            button.grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, value):
        
        #Handle button clicks
        if value == '=':
            try:
                result = eval(self.result_var.get())
                self.result_var.set(str(result))
            except Exception as e:
                messagebox.showerror("Error", f"Invalid Expression\n{e}")
                self.result_var.set("")
        elif value == 'C':            #Clear the entry 
            self.result_var.set("")
        else:
            #Update the screen with clicked button
            current_text = self.result_var.get()
            self.result_var.set(current_text + value)
#Run the GUI application
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
