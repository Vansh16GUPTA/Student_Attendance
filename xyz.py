import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Attendance Tracker")

# Create a dictionary to store attendance records
attendance_records = {}

# Function to add a student
def add_student():
    name = entry_name.get()
    if name:
        attendance_records[name] = []
        tree.insert("", "end", values=(name, ""))
        entry_name.delete(0, tk.END)
    else:
        label_feedback.config(text="Please enter a valid name.")

# Function to mark attendance
def mark_attendance():
    selected_item = tree.selection()
    if selected_item:
        name = tree.item(selected_item)['values'][0]
        status = var_status.get()
        if name in attendance_records:
            attendance_records[name].append(status)
            tree.item(selected_item, values=(name, "".join(map(str, attendance_records[name]))))
            var_status.set("1")
        else:
            label_feedback.config(text=f"Student {name} not found.")
    else:
        label_feedback.config(text="Select a student to mark attendance for.")

# Function to view attendance
def view_attendance():
    view_window = tk.Toplevel(root)
    view_window.title("View Attendance")

    view_tree = ttk.Treeview(view_window, columns=("Name", "Attendance"), show="headings")
    view_tree.heading("Name", text="Name")
    view_tree.heading("Attendance", text="Attendance")
    view_tree.column("Name", width=150)
    view_tree.column("Attendance", width=150)

    for name, record in attendance_records.items():
        view_tree.insert("", "end", values=(name, "".join(map(str, record))))

    view_tree.pack()

# Create labels, entry fields, and buttons
label_name = tk.Label(root, text="Student Name:")
entry_name = tk.Entry(root)

label_status = tk.Label(root, text="Attendance (1 for present, 0 for absent):")
var_status = tk.StringVar(value="1")
entry_status = tk.Entry(root, textvariable=var_status)

button_add = tk.Button(root, text="Add Student", command=add_student)
button_mark = tk.Button(root, text="Mark Attendance", command=mark_attendance)
button_view = tk.Button(root, text="View Attendance", command=view_attendance)

label_feedback = tk.Label(root, text="")
label_feedback.config(font=('Arial', 12))

# Create a treeview widget to display attendance records
tree = ttk.Treeview(root, columns=("Name", "Attendance"), show="headings")
tree.heading("Name", text="Name")
tree.heading("Attendance", text="Attendance")
tree.column("Name", width=150)
tree.column("Attendance", width=150)

# Grid layout
label_name.grid(row=0, column=0, padx=5, pady=5)
entry_name.grid(row=0, column=1, padx=5, pady=5)
label_status.grid(row=1, column=0, padx=5, pady=5)
entry_status.grid(row=1, column=1, padx=5, pady=5)
button_add.grid(row=2, column=0, padx=5, pady=5)
button_mark.grid(row=2, column=1, padx=5, pady=5)
button_view.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
label_feedback.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
tree.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Start the main event loop
root.mainloop()
