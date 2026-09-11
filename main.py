import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title("Notes/todos native 0.1")
root.geometry("750x900")

COLOR_BG = "#F8F9FA"       
COLOR_CARD = "#FFFFFF"       
COLOR_NAV = "#212529"        
COLOR_TEXT = "#343A40"      
COLOR_ACCENT = "#495057"    
COLOR_DANGER = "#DC3545" 

root.configure(bg=COLOR_BG)

def show_notes_screen():
    todo_screen.pack_forget()
    notes_screen.pack(expand=True, fill="both", padx=25, pady=20)

def show_todo_screen():
    notes_screen.pack_forget()
    todo_screen.pack(expand=True, fill="both", padx=25, pady=20)

def save_notes():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
        title="Save Your Notes"
    )
    
    if file_path:
        # Extract text from line 1 char 0 up to the end (minus trailing newline spacer)
        note_content = text_area.get("1.0", "end-1c")
        
        # Write content safely to the computer drive
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(note_content)

def add_todo_item():
    task_text = todo_entry.get()
    date_text = date_entry.get()

    if task_text != "":
        if date_text != "":
            final_display_text = f" [{date_text}] {task_text}"
        else:
            final_display_text = f" {task_text}"

        todo_listbox.insert(tk.END, final_display_text)

        todo_entry.delete(0, tk.END)
        date_entry.delete(0, tk.END)

def delete_todo_item():
    try:
        selected_index = todo_listbox.curselection()
        todo_listbox.delete(selected_index)
    except tk.TclError:
        pass

top_frame = tk.Frame(root, bg=COLOR_NAV, height=50)
top_frame.pack(side="top", fill="x")

# Flat navigation link elements that mimic web page toggles
notes_button = tk.Button(top_frame, text="temp-notes", font=("Segoe UI", 10, "bold"),
                         fg="white", bg=COLOR_NAV, bd=0, relief="flat", activebackground=COLOR_ACCENT, activeforeground="white", cursor="hand2")
notes_button.configure(command=show_notes_screen)
notes_button.pack(side="left", padx=20, pady=10)

todo_button = tk.Button(top_frame, text="to-dos", font=("Segoe UI", 10, "bold"),
                        fg="white", bg=COLOR_NAV, bd=0, relief="flat", activebackground=COLOR_ACCENT, activeforeground="white", cursor="hand2")
todo_button.configure(command=show_todo_screen)
todo_button.pack(side="left", padx=20, pady=10)

notes_screen = tk.Frame(root, bg=COLOR_BG)
# This module packs first, dictating it opens by default on launch
notes_screen.pack(expand=True, fill="both", padx=25, pady=20)

text_area = tk.Text(notes_screen, font=("Segoe UI", 11), fg=COLOR_TEXT, bg=COLOR_CARD, 
                    bd=0, relief="flat", padx=15, pady=15, highlightthickness=1, highlightbackground="#DEE2E6")
text_area.pack(expand=True, fill="both", pady=(0, 15))

save_button = tk.Button(notes_screen, text="Save Notes to Computer", font=("Segoe UI", 10, "bold"), 
                        fg="white", bg=COLOR_NAV, bd=0, relief="flat", cursor="hand2")
save_button.configure(command=save_notes)
save_button.pack(fill="x", ipady=6)

todo_screen = tk.Frame(root, bg=COLOR_BG)

input_frame = tk.Frame(todo_screen, bg=COLOR_BG)
input_frame.pack(fill="x", pady=(0, 15))

date_label = tk.Label(input_frame, text="Date:", font=("Segoe UI", 10), fg=COLOR_TEXT, bg=COLOR_BG)
date_label.pack(side="left", padx=(0, 5))
date_entry = tk.Entry(input_frame, font=("Segoe UI", 11), width=10, bd=0, highlightthickness=1, highlightbackground="#DEE2E6")
date_entry.pack(side="left", padx=(0, 15), ipady=4)

# Task description field segment
task_label = tk.Label(input_frame, text="Task:", font=("Segoe UI", 10), fg=COLOR_TEXT, bg=COLOR_BG)
task_label.pack(side="left", padx=(0, 5))
todo_entry = tk.Entry(input_frame, font=("Segoe UI", 11), bd=0, highlightthickness=1, highlightbackground="#DEE2E6")
todo_entry.pack(side="left", expand=True, fill="x", padx=(0, 15), ipady=4)

#control item button
add_button = tk.Button(input_frame, text="Add Task", font=("Segoe UI", 10, "bold"), 
                       fg="white", bg=COLOR_NAV, bd=0, relief="flat", cursor="hand2", padx=15)
add_button.configure(command=add_todo_item)
add_button.pack(side="right", ipady=2)

todo_listbox = tk.Listbox(todo_screen, font=("Segoe UI", 11), fg=COLOR_TEXT, bg=COLOR_CARD, 
                          bd=0, relief="flat", highlightthickness=1, highlightbackground="#DEE2E6", selectbackground="#E9ECEF", selectforeground=COLOR_TEXT)
todo_listbox.pack(expand=True, fill="both", pady=(0, 15))

# Delete element button
delete_button = tk.Button(todo_screen, text="Remove Completed Task", font=("Segoe UI", 10, "bold"), 
                          fg="white", bg=COLOR_DANGER, bd=0, relief="flat", cursor="hand2")
delete_button.configure(command=delete_todo_item)
delete_button.pack(fill="x", ipady=6)

root.mainloop()