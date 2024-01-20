from tkinter import *
from tkinter import ttk
import math

root = Tk()
root.title("Calculator")
root.geometry("+500+80")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

styles = ttk.Style()
styles.theme_use('clam')
styles.configure('main_frame.TFrame', background="#DBDBDB")

main_frame = ttk.Frame(root, style="main_frame.TFrame")
main_frame.grid(column=0, row=0, sticky=(W, N, E, S))

main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)
main_frame.columnconfigure(2, weight=1)
main_frame.columnconfigure(3, weight=1)

main_frame.rowconfigure(0, weight=1)
main_frame.rowconfigure(1, weight=1)
main_frame.rowconfigure(2, weight=1)
main_frame.rowconfigure(3, weight=1)
main_frame.rowconfigure(4, weight=1)
main_frame.rowconfigure(5, weight=1)
main_frame.rowconfigure(6, weight=1)
main_frame.rowconfigure(7, weight=1)

# styles label
style_label_1 = ttk.Style()
style_label_1.configure('Label1.TLabel', font='arial 15', anchor="e")

style_label_2 = ttk.Style()
style_label_2.configure('Label2.TLabel', font='arial 40', anchor="e")

input_1 = StringVar()
label_input_1 = ttk.Label(main_frame, textvariable=input_1, style='Label1.TLabel')
label_input_1.grid(column=0, row=0, columnspan=4, sticky=(W, N, E, S))

input_2 = StringVar()
label_input_2 = ttk.Label(main_frame, textvariable=input_2, style='Label2.TLabel')
label_input_2.grid(column=0, row=1, columnspan=4, sticky=(W, N, E, S))

# styles button
style_button_numbers = ttk.Style()
style_button_numbers.configure('Button_numbers.TButton', font='arial 22', width=5, background="#FFFFFF", relief="flat")
style_button_numbers.map('Button_numbers.TButton', background=[('active', '#B9B9B9')])

style_button_delete = ttk.Style()
style_button_delete.configure('Button_delete.TButton', font='arial 22', width=5, background="#CECECE", relief="flat")
style_button_delete.map('Button_delete.TButton', foreground=[('active', '#FF0000')], background=[('active', '#858585')])

style_button_remaining = ttk.Style()
style_button_remaining.configure('Button_remaining.TButton', font='arial 22', width=5, background="#CECECE", relief="flat")
style_button_remaining.map('Button_remaining.TButton', background=[('active', '#858585')])


button_0 = ttk.Button(main_frame, text="0", style='Button_numbers.TButton')
button_1 = ttk.Button(main_frame, text="1", style='Button_numbers.TButton')
button_2 = ttk.Button(main_frame, text="2", style='Button_numbers.TButton')
button_3 = ttk.Button(main_frame, text="3", style='Button_numbers.TButton')
button_4 = ttk.Button(main_frame, text="4", style='Button_numbers.TButton')
button_5 = ttk.Button(main_frame, text="5", style='Button_numbers.TButton')
button_6 = ttk.Button(main_frame, text="6", style='Button_numbers.TButton')
button_7 = ttk.Button(main_frame, text="7", style='Button_numbers.TButton')
button_8 = ttk.Button(main_frame, text="8", style='Button_numbers.TButton')
button_9 = ttk.Button(main_frame, text="9", style='Button_numbers.TButton')

button_delete = ttk.Button(main_frame, text=chr(9003), style='Button_delete.TButton')
button_delete_all = ttk.Button(main_frame, text="C", style='Button_delete.TButton')
button_parenthesis_1 = ttk.Button(main_frame, text="(", style='Button_remaining.TButton')
button_parenthesis_2 = ttk.Button(main_frame, text=")", style='Button_remaining.TButton')
button_point = ttk.Button(main_frame, text=".", style='Button_remaining.TButton')

button_divicion = ttk.Button(main_frame, text=chr(247), style='Button_remaining.TButton')
button_multiplication = ttk.Button(main_frame, text="x", style='Button_remaining.TButton')
button_subtraction = ttk.Button(main_frame, text="-", style='Button_remaining.TButton')
button_add = ttk.Button(main_frame, text="+", style='Button_remaining.TButton')

button_equal = ttk.Button(main_frame, text="=", style='Button_remaining.TButton')
button_square_root = ttk.Button(main_frame, text="√", style='Button_remaining.TButton')

button_parenthesis_1.grid(column=0, row=2, sticky=(W, N, E, S))
button_parenthesis_2.grid(column=1, row=2, sticky=(W, N, E, S))
button_delete_all.grid(column=2, row=2, sticky=(W, N, E, S))
button_delete.grid(column=3, row=2, sticky=(W, N, E, S))

button_7.grid(column=0, row=3, sticky=(W, N, E, S))
button_8.grid(column=1, row=3, sticky=(W, N, E, S))
button_9.grid(column=2, row=3, sticky=(W, N, E, S))
button_divicion.grid(column=3, row=3, sticky=(W, N, E, S))

button_4.grid(column=0, row=4, sticky=(W, N, E, S))
button_5.grid(column=1, row=4, sticky=(W, N, E, S))
button_6.grid(column=2, row=4, sticky=(W, N, E, S))
button_multiplication.grid(column=3, row=4, sticky=(W, N, E, S))

button_1.grid(column=0, row=5, sticky=(W, N, E, S))
button_2.grid(column=1, row=5, sticky=(W, N, E, S))
button_3.grid(column=2, row=5, sticky=(W, N, E, S))
button_add.grid(column=3, row=5, sticky=(W, N, E, S))

button_0.grid(column=0, row=6, columnspan=2, sticky=(W, N, E, S))
button_point.grid(column=2, row=6, sticky=(W, N, E, S))
button_subtraction.grid(column=3, row=6, sticky=(W, N, E, S))

button_equal.grid(column=0, row=7, columnspan=3, sticky=(W, N, E, S))
button_square_root.grid(column=3, row=7, sticky=(W, N, E, S))

for child in main_frame.winfo_children():
    child.grid_configure(ipady=10, padx=1, pady=1)

root.mainloop()