import tkinter as tk
from tkinter import messagebox, ttk

# Sample data structure
contacts = []

# Functions
def add_contact():
    name = entry_name.get().strip()
    phone = entry_phone.get().strip()
    email = entry_email.get().strip()
    address = entry_address.get().strip()

    if name and phone:
        contacts.append({
            'name': name,
            'phone': phone,
            'email': email,
            'address': address
        })
        messagebox.showinfo("Success", "Contact added successfully!")
        clear_entries()
        view_contacts()
    else:
        messagebox.showwarning("Warning", "Name and phone number are required!")

def view_contacts():
    listbox_contacts.delete(0, tk.END)
    for contact in contacts:
        listbox_contacts.insert(tk.END, f"{contact['name']} - {contact['phone']}")

def search_contact():
    search_query = entry_search.get().strip().lower()
    listbox_contacts.delete(0, tk.END)
    for contact in contacts:
        if search_query in contact['name'].lower() or search_query in contact['phone']:
            listbox_contacts.insert(tk.END, f"{contact['name']} - {contact['phone']}")

def delete_contact():
    selected = listbox_contacts.curselection()
    if selected:
        index = selected[0]
        contacts.pop(index)
        view_contacts()
        messagebox.showinfo("Success", "Contact deleted successfully!")
    else:
        messagebox.showwarning("Warning", "Please select a contact to delete")

def update_contact():
    selected = listbox_contacts.curselection()
    if selected:
        index = selected[0]
        contacts[index]['name'] = entry_name.get().strip()
        contacts[index]['phone'] = entry_phone.get().strip()
        contacts[index]['email'] = entry_email.get().strip()
        contacts[index]['address'] = entry_address.get().strip()
        view_contacts()
        messagebox.showinfo("Success", "Contact updated successfully!")
    else:
        messagebox.showwarning("Warning", "Please select a contact to update")

def on_select(event):
    selected = listbox_contacts.curselection()
    if selected:
        index = selected[0]
        contact = contacts[index]
        entry_name.delete(0, tk.END)
        entry_name.insert(0, contact['name'])
        entry_phone.delete(0, tk.END)
        entry_phone.insert(0, contact['phone'])
        entry_email.delete(0, tk.END)
        entry_email.insert(0, contact['email'])
        entry_address.delete(0, tk.END)
        entry_address.insert(0, contact['address'])

def clear_entries():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)

# GUI
root = tk.Tk()
root.title("Contact Management System")
root.geometry("700x600")  # Set window size
root.configure(bg="#f5f5f5")

# Fonts and Styles
style = ttk.Style(root)
style.theme_use('clam')
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TEntry", font=("Helvetica", 12), padding=5)
style.configure("TButton", font=("Helvetica", 12), padding=5)
style.configure("TListbox", font=("Helvetica", 12), padding=5)

# Title Frame
title_frame = tk.Frame(root, bg="#333", pady=10)
title_frame.pack(fill="x")
tk.Label(title_frame, text="Contact Management System", font=("Helvetica", 18, "bold"), bg="#333", fg="white").pack()

# Form Frame
form_frame = tk.Frame(root, bg="#f5f5f5", padx=10, pady=10)
form_frame.pack(pady=10, fill="x")

# Form Fields
tk.Label(form_frame, text="Store Name:", font=("Helvetica", 12), bg="#f5f5f5").grid(row=0, column=0, sticky="e", padx=5, pady=5)
entry_name = ttk.Entry(form_frame, width=30)
entry_name.grid(row=0, column=1, padx=5, pady=5)

tk.Label(form_frame, text="Phone Number:", font=("Helvetica", 12), bg="#f5f5f5").grid(row=1, column=0, sticky="e", padx=5, pady=5)
entry_phone = ttk.Entry(form_frame, width=30)
entry_phone.grid(row=1, column=1, padx=5, pady=5)

tk.Label(form_frame, text="Email:", font=("Helvetica", 12), bg="#f5f5f5").grid(row=2, column=0, sticky="e", padx=5, pady=5)
entry_email = ttk.Entry(form_frame, width=30)
entry_email.grid(row=2, column=1, padx=5, pady=5)

tk.Label(form_frame, text="Address:", font=("Helvetica", 12), bg="#f5f5f5").grid(row=3, column=0, sticky="e", padx=5, pady=5)
entry_address = ttk.Entry(form_frame, width=30)
entry_address.grid(row=3, column=1, padx=5, pady=5)

# Buttons
button_frame = tk.Frame(form_frame, bg="#f5f5f5")
button_frame.grid(row=4, column=0, columnspan=2, pady=10)

button_add = ttk.Button(button_frame, text="Add Contact", command=add_contact, style="TButton")
button_add.grid(row=0, column=0, padx=5)

button_update = ttk.Button(button_frame, text="Update Contact", command=update_contact, style="TButton")
button_update.grid(row=0, column=1, padx=5)

# Contact List
list_frame = tk.Frame(root, bg="#f5f5f5", padx=10, pady=10)
list_frame.pack(pady=10, fill="both", expand=True)

listbox_contacts = tk.Listbox(list_frame, font=("Helvetica", 12), width=50, height=15, selectbackground="#4a90e2", relief="flat")
listbox_contacts.pack(side="left", fill="both", expand=True)
listbox_contacts.bind('<<ListboxSelect>>', on_select)

# Scrollbar for Listbox
scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=listbox_contacts.yview)
scrollbar.pack(side="right", fill="y")
listbox_contacts.config(yscrollcommand=scrollbar.set)

# Search and Delete
search_frame = tk.Frame(root, bg="#f5f5f5", padx=10, pady=10)
search_frame.pack(pady=10, fill="x")

entry_search = ttk.Entry(search_frame, width=30)
entry_search.pack(side="left", padx=5)
button_search = ttk.Button(search_frame, text="Search", command=search_contact, style="TButton")
button_search.pack(side="left", padx=5)

button_delete = ttk.Button(search_frame, text="Delete", command=delete_contact, style="TButton")
button_delete.pack(side="left", padx=5)

view_contacts()  # Initialize the contact list display

# Placeholder styling
placeholder_style = ttk.Style()
placeholder_style.configure("TPlaceholder.TEntry", foreground="#888")

def set_placeholder(widget, text):
    """Set placeholder text in entry widget."""
    widget.insert(0, text)
    widget.configure(style="TPlaceholder.TEntry")

def remove_placeholder(event):
    """Remove placeholder text on focus."""
    if event.widget.get() == "Search by name or phone...":
        event.widget.delete(0, tk.END)
        event.widget.configure(style="TEntry")

def add_placeholder(event):
    """Add placeholder text on focus out if entry is empty."""
    if not event.widget.get():
        set_placeholder(event.widget, "Search by name or phone...")

entry_search.bind("<FocusIn>", remove_placeholder)
entry_search.bind("<FocusOut>", add_placeholder)
set_placeholder(entry_search, "Search by name or phone...")

root.mainloop()
