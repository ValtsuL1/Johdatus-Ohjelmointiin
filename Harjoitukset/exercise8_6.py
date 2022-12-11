import tkinter as tk
from tkinter import ttk

result_shown = False


def add_sums(num1, num2, num3):

    sum_result = int(num1) + int(num2) + int(num3)
    result["text"] = f"Tulos: {sum_result}"


window = tk.Tk()

number1text = tk.StringVar()
number2text = tk.StringVar()
number3text = tk.StringVar()

number1_label = ttk.Label(text="Luku 1")
number1_label.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)

number1 = ttk.Entry(textvariable=number1text)
number1.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)

number2_label = ttk.Label(text="Luku 2")
number2_label.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)

number2 = ttk.Entry(textvariable=number2text)
number2.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)

number3_label = ttk.Label(text="Luku 3")
number3_label.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)

number3 = ttk.Entry(textvariable=number3text)
number3.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)

getresult_button = ttk.Button(window,
                              text="Näytä tulos",
                              command=lambda: add_sums(number1.get(), number2.get(), number3.get()))
getresult_button.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)

result = tk.Label(window, text="Tulos:")
result.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)

exit_button = ttk.Button(window, text="Lopeta", command=lambda: window.quit())
exit_button.pack(ipadx=10, ipady=10, side=tk.BOTTOM)

window.title("Laskin")

window.geometry("300x300")
window.resizable(False, False)

window.mainloop()
