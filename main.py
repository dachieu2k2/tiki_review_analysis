import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import re

import openpyxl

from model_predict import data_after_predict


product_id = 217176777

# def load_data():
#     path = "./people.xlsx"
#     workbook = openpyxl.load_workbook(path)
#     sheet = workbook.active

#     list_values = list(sheet.values)

#     counter, finalData = data_after_predict(product_id)

#     print(list_values)
    

    


# def load_data_2():
#     path = "./people.xlsx"
#     workbook = openpyxl.load_workbook(path)
#     sheet = workbook.active

#     list_values = list(sheet.values)
#     return list_values

predict_data = {
    "NEU": 10,
    "POS": 10,
    "NEG": 10,
}

fig1, ax1 = plt.subplots()
ax1.bar(predict_data.keys(), predict_data.values())
ax1.set_title("Sales by Product")
ax1.set_xlabel("Product")
ax1.set_ylabel("Sales")
# plt.show()

# Charts data
# data = load_data_2()
# print(data)
fig2, ax2 = plt.subplots()
ax2.pie(predict_data.values(), labels=predict_data.keys(), autopct='%1.1f%%')
ax2.set_title("Product \nBreakdown")



def insert_row():
    url = test_entry.get()
        # Regular expression to find the ID
    pattern = r'-p(\d+)\.html'
    # Search for the pattern in the URL
    match = re.search(pattern, url)

    extracted_id = match.group(1)
    print(f"Extracted ID: {extracted_id}")

    finalDataArr = []
    counter, finalData = data_after_predict(extracted_id)

    finalDataArr = finalData

    predict_data = counter
    ax1.clear()
    ax1.bar(predict_data.keys(), predict_data.values())

    canvas1 = FigureCanvasTkAgg(fig1, chart_frame)
    canvas1.draw()
    canvas1.get_tk_widget().grid(row=0,column=0, pady=10,padx=10)

    ax2.clear()
    ax2.pie(predict_data.values(), labels=predict_data.keys(), autopct='%1.1f%%')


    canvas2 = FigureCanvasTkAgg(fig2, chart_frame)
    canvas2.draw()
    canvas2.get_tk_widget().grid(row=0,column=1, pady=10,padx=10)



    cols = ("Name", "Content", "Purchased", "Predict")

    for col_name in cols:
        treeview.heading(col_name, text=col_name)

    for value_tuple in finalDataArr:
        treeview.insert('', tk.END, values=value_tuple)





def toggle_mode():
    if mode_switch.instate(["selected"]):
        style.theme_use("forest-light")
    else:
        style.theme_use("forest-dark")






root = tk.Tk()

style = ttk.Style(root)
root.tk.call("source", "forest-light.tcl")
root.tk.call("source", "forest-dark.tcl")
style.theme_use("forest-dark")


frame = ttk.Frame(root, width=150, height=400)

# scrollView = ttk.Scrollbar(frame)
# scrollView.pack(side="right", fill="y")
frame.pack()

header_frame = ttk.LabelFrame(frame, text="Dashboard")
header_frame.grid(row=0, column=0, padx=20, pady=10)


# Input
test_entry = ttk.Entry(header_frame)
test_entry.insert(0, "Nhập đường dẫn: ")
test_entry.bind("<FocusIn>", lambda e: test_entry.delete('0', 'end'))
test_entry.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

# Button Insert
button = ttk.Button(header_frame, text="Analysis", command=insert_row)
button.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")


# widgets_frame = ttk.LabelFrame(frame, text="Insert Row")
# widgets_frame.grid(row=1, column=0, padx=20, pady=10)

# Input
# name_entry = ttk.Entry(widgets_frame)
# name_entry.insert(0, "Name")
# name_entry.bind("<FocusIn>", lambda e: name_entry.delete('0', 'end'))
# name_entry.grid(row=0, column=0, padx=5, pady=(0, 5), sticky="ew")

# Spinbox
# age_spinbox = ttk.Spinbox(widgets_frame, from_=18, to=100)
# age_spinbox.insert(0, "Age")
# age_spinbox.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

# Combobox
# status_combobox = ttk.Combobox(widgets_frame, values=combo_list)
# status_combobox.current(0)
# status_combobox.grid(row=2, column=0, padx=5, pady=5,  sticky="ew")

# Checkbox
# a = tk.BooleanVar()
# checkbutton = ttk.Checkbutton(widgets_frame, text="Employed", variable=a)
# checkbutton.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")

# Button Insert
# button = ttk.Button(widgets_frame, text="Insert", command=insert_row)
# button.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")

# Br
# separator = ttk.Separator(widgets_frame)
# separator.grid(row=5, column=0, padx=(20, 10), pady=10, sticky="ew")

# Switch button
# mode_switch = ttk.Checkbutton(
#     widgets_frame, text="Mode", style="Switch", command=toggle_mode)
# mode_switch.grid(row=6, column=0, padx=5, pady=10, sticky="nsew")




# plt.show()

# Chart Import to frame
chart_frame = ttk.Frame(frame, width=150, height=400)
chart_frame.grid(row=1, column=0, pady=10)

canvas1 = FigureCanvasTkAgg(fig1, chart_frame)
canvas1.draw()
canvas1.get_tk_widget().grid(row=0,column=0, pady=10,padx=10)

canvas2 = FigureCanvasTkAgg(fig2, chart_frame)
canvas2.draw()
canvas2.get_tk_widget().grid(row=0,column=1, pady=10,padx=10)

# Chart 4: Line chart of sales by year
# fig4, ax4 = plt.subplots()
# ax4.plot(list(sales_year_data.keys()), list(sales_year_data.values()))
# ax4.set_title("Sales by Year")
# ax4.set_xlabel("Year")
# ax4.set_ylabel("Sales")

# Charts display
# canvas3 = FigureCanvasTkAgg(fig3, upper_frame)
# canvas3.draw()
# canvas3.get_tk_widget().pack(side="left", fill="both", expand=True)

# lower_frame = tk.Frame(charts_frame)
# lower_frame.pack(fill="both", expand=True)

# canvas4 = FigureCanvasTkAgg(fig4, lower_frame)
# canvas4.draw()
# canvas4.get_tk_widget().pack(side="left", fill="both", expand=True)

# Table
treeFrame = ttk.Frame(frame)
treeFrame.grid(row=2, column=0, pady=10)
treeScroll = ttk.Scrollbar(treeFrame)
treeScroll.pack(side="right", fill="y")

cols = ("Name", "Content", "Purchased", "Predict")
treeview = ttk.Treeview(treeFrame, show="headings",
                        yscrollcommand=treeScroll.set, columns=cols, height=13)
treeview.column("Name", width=100)
treeview.column("Content", width=300)
treeview.column("Purchased", width=80)
treeview.column("Predict", width=50)
treeview.pack()
treeScroll.config(command=treeview.yview)

# if(product_id):
#     load_data()




root.mainloop()