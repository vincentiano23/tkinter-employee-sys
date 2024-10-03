import tkinter as tk
from tkinter import messagebox, Listbox, Scrollbar, Frame, StringVar
from datetime import datetime
from tkinter.ttk import Combobox

employees = []


def add_employee():
    name = name_entry.get()
    age = age_combobox.get()
    position = position_combobox.get()
    arrival_time = arrival_time_entry.get()
    departure_time = departure_time_entry.get()
    employee_id = id_entry.get()
    
    if name and age and position and arrival_time and departure_time and employee_id:
        if int(age) < 18:
            messagebox.showwarning("Age Restriction", "Employee must be 18 years or older.")
            return
        employees.append({
            'name': name,
            'age': age, 
            'position': position,
            'arrival_time': arrival_time,
            'departure_time': departure_time,
            'employee_id': employee_id
            })
        update_employee_list()
        clear_entries()
    else:
        messagebox.showwarning("Input Error", "Please fill all fields")


def update_employee_list():
    employee_list.delete(0, tk.END)  
    for emp in employees:
        employee_list.insert(tk.END, f"{emp['name']} (ID:{emp['employee_id']}) - {emp['position']} - Arrival: {emp['arrival_time']} - Departure: {emp['departure_time']}")
def delete_employee():
    try:
        selected_index = employee_list.curselection()[0]
        employees.pop(selected_index)
        update_employee_list()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select an employee to delete")

def clear_entries():
    name_entry.delete(0, tk.END)
    age_combobox.delete(0, tk.END)
    position_combobox.delete(0, tk.END)
    arrival_time_entry.delete(0, tk.END)
    departure_time_entry.delete(0, tk.END)
    id_entry.delete(0, tk.END)



app = tk.Tk()
app.title("Employee Management System")
app.geometry("400x400")
app.config(bg="#f1f1f1")


input_frame = Frame(app, bg="#f0f0f0")
input_frame.pack(pady=10)

name_label = tk.Label(input_frame, text="Name:", bg="#f0f0f0")
name_label.grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(input_frame, width=25)
name_entry.grid(row=0, column=1, padx=5, pady=5)

age_label = tk.Label(input_frame, text="Age:", bg="#f0f0f0")
age_label.grid(row=1, column=0, padx=5, pady=5)
age_combobox = Combobox(input_frame, width=23)
age_combobox['values'] = [str(i) for i in range(18, 66)]  
age_combobox.grid(row=1, column=1, padx=5, pady=5)

position_label = tk.Label(input_frame, text="Position:", bg="#f0f0f0")
position_label.grid(row=2, column=0, padx=5, pady=5)
position_combobox = Combobox(input_frame, width=23)
position_combobox['values'] = ('Cleaner', 'Cook', 'Head of Cleaners', 'Head of Cooks')
position_combobox.grid(row=2, column=1, padx=5, pady=5)

arrival_time_label = tk.Label(input_frame, text="Arrival Time (HH:MM):", bg="#f0f0f0")
arrival_time_label.grid(row=3, column=0, padx=5, pady=5)
arrival_time_entry = tk.Entry(input_frame, width=25)
arrival_time_entry.grid(row=3, column=1, padx=5, pady=5)

departure_time_label = tk.Label(input_frame, text="Departure Time (HH:MM):", bg="#f0f0f0")
departure_time_label.grid(row=4, column=0, padx=5, pady=5)
departure_time_entry = tk.Entry(input_frame, width=25)
departure_time_entry.grid(row=4, column=1, padx=5, pady=5)

id_label = tk.Label(input_frame, text="Employee ID:", bg="#f0f0f0")
id_label.grid(row=5, column=0, padx=5, pady=5)
id_entry = tk.Entry(input_frame, width=25)
id_entry.grid(row=5, column=1, padx=5, pady=5)


button_frame = Frame(app, bg="#f0f0f0")
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Employee", command=add_employee, bg="#4CAF50", fg="white")
add_button.grid(row=0, column=0, padx=10)

delete_button = tk.Button(button_frame, text="Delete Employee", command=delete_employee, bg="#f44336", fg="white")
delete_button.grid(row=0, column=1, padx=10)

employee_frame = Frame(app, bg="#f0f0f0")
employee_frame.pack(pady=10)

employee_list = Listbox(employee_frame, width=50, height=10)
employee_list.pack(side=tk.LEFT)

scrollbar = Scrollbar(employee_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

employee_list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=employee_list.yview)


app.mainloop()
