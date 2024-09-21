import tkinter as tk

class SimpleCalculator:
    def __init__(self, master):
        print('Master in __init__ is', master, id(master), type(root))
        self.master = master
        self.master.title("Simple Calculator")
        
        # Entry widget for input
        self.entry = tk.Entry(master, width=100, borderwidth=15)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        # Label widget for displaying history
        self.history_label = tk.Label(master, text="没有历史记录", justify=tk.RIGHT)
        self.history_label.grid(row=6, column=0, columnspan=4, sticky="w", padx=10)
        
                        #上面的row是6，column是0，columnspan是4，sticky是“w”,padx是10
        # History data
        self.history = []

        # Adding buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        for (text, row, col) in buttons:
            button_command = lambda cmd=text: self.click(cmd)
            tk.Button(master, text=text, width=10, command=button_command).grid(row=row, column=col)

    def click(self, value):
        if value == '=':
            try:
                result = eval(self.entry.get())
                self.update_history(self.entry.get() + " = " + str(result))
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
        else:
            self.entry.insert(tk.END, value)

    def update_history(self, record):
        # Update history to show last three calculations
        if len(self.history) >= 10:
            self.history.pop(0)
        self.history.append(record)
        self.history_label.config(text="\n".join(self.history))

# Main window
root = tk.Tk()
print('Root node content', root, id(root), type(root))
app = SimpleCalculator(root)
root.mainloop()
