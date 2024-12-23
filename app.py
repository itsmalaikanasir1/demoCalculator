import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator App")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        self.expression = ""

        # Display frame
        self.display_frame = tk.Frame(self.root)
        self.display_frame.pack(expand=True, fill="both")

        self.display = tk.Entry(self.display_frame, font=("Arial", 20), justify="right", bd=10)
        self.display.pack(expand=True, fill="both")

        # Buttons frame
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(expand=True, fill="both")

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["C", "0", "=", "+"]
        ]

        for row in buttons:
            button_row = tk.Frame(self.buttons_frame)
            button_row.pack(expand=True, fill="both")

            for button in row:
                btn = tk.Button(
                    button_row, text=button, font=("Arial", 18),
                    command=lambda b=button: self.on_button_click(b)
                )
                btn.pack(side="left", expand=True, fill="both")

    def on_button_click(self, button):
        if button == "C":
            self.expression = ""
            self.update_display()
        elif button == "=":
            try:
                result = eval(self.expression)
                self.expression = str(result)
                self.update_display()
            except Exception as e:
                messagebox.showerror("Error", "Invalid Expression")
                self.expression = ""
                self.update_display()
        else:
            self.expression += button
            self.update_display()

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
