import tkinter as tk
import time


root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")

# ENTER NUMBERS

def enter_number(number):
    
    if number == "=":
        try:
            expression = entry.get()
            result = eval(expression)
            print(result)
            entry.delete(0, tk.END)
            entry.insert(0, str(result))
            
        except ZeroDivisionError:
            entry.delete(0, tk.END)
            entry.insert(0, "Cannot divide by 0")
            
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(0, "Expression Error")
            
    elif number == "C":
        entry.delete(0, tk.END)
    else:
        current_text = entry.get()
        
        if current_text in ["Cannot divide by 0", "Expression Error"]:
            entry.delete(0, tk.END)
        
        entry.insert(tk.END, number)    
    

# Buttons
layout = [
    (0, 0, "1"), (0, 1, "2"), (0, 2, "3"), (0, 4, "+"),
    (1, 0, "4"), (1, 1, "5"), (1, 2, "6"), (1, 4, "-"),
    (2, 0, "7"), (2, 1, "8"), (2, 2, "9"), (2, 4, "*"),
    (3, 0, "C"),(3, 1, "0"),(3, 2, "="),(3, 4, "/")
]

frame = tk.Frame(root)
frame.pack(side="bottom", fill="both", padx=10, pady=10, expand=True)

entry = tk.Entry(root, font=("Helvetica", 50, "bold"), justify="right")
entry.pack(fill="both", ipadx=30, ipady=50)

for i in range(4):
    frame.columnconfigure(i, weight=1)
    frame.rowconfigure(i, weight=1)

for row, column, number in layout:
    buttons = tk.Button(frame, text=number, command=lambda n=number: enter_number(n), font=("Helvetica", 20, "bold"))
    buttons.grid(row=row, column=column, sticky="nsew", padx=5, pady=5)




if __name__ == "__main__":
    root.mainloop()
