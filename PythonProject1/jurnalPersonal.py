import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
from datetime import datetime
import json, os, shutil


JOURNAL_FILE = "jurnal.json"
BACKUP_FILE = "jurnal_backup.json"
AUTO_SAVE_INTERVAL = 5000


if os.path.exists(JOURNAL_FILE):
    with open(JOURNAL_FILE, "r", encoding="utf-8") as f:
        jurnal = json.load(f)
else:
    jurnal = {}


def backup_journal():
    if os.path.exists(JOURNAL_FILE):
        shutil.copyfile(JOURNAL_FILE, BACKUP_FILE)

def save_entry(auto=False):
    selected_date = calendar.get_date()
    time_now = datetime.now().strftime("%H:%M:%S")
    key = f"{selected_date} {time_now}"

    content = text_box.get("1.0", tk.END).strip()
    if not content:
        return

    jurnal[key] = content

    with open(JOURNAL_FILE, "w", encoding="utf-8") as f:
        json.dump(jurnal, f, ensure_ascii=False, indent=4)

    backup_journal()
    update_list_by_date(selected_date)

    if not auto:
        messagebox.showinfo("Salvat", "Notița a fost salvată.")

    schedule_auto_save()

def open_entry(event=None):
    if not entry_list.curselection():
        return

    key = entry_list.get(entry_list.curselection()[0])
    text_box.delete("1.0", tk.END)
    text_box.insert(tk.END, jurnal[key])

def delete_entry():
    if not entry_list.curselection():
        messagebox.showwarning(
            "Atenție",
            "Selectează o notiță din listă pentru a o șterge."
        )
        return

    key = entry_list.get(entry_list.curselection()[0])

    if not messagebox.askyesno(
        "Confirmare ștergere",
        f"Ștergi notița din:\n{key} ?"
    ):
        return

    del jurnal[key]

    with open(JOURNAL_FILE, "w", encoding="utf-8") as f:
        json.dump(jurnal, f, ensure_ascii=False, indent=4)

    backup_journal()

    text_box.delete("1.0", tk.END)
    update_list_by_date(calendar.get_date())

def update_list_by_date(date):
    entry_list.delete(0, tk.END)
    for key in sorted(jurnal.keys(), reverse=True):
        if key.startswith(date):
            entry_list.insert(tk.END, key)

def calendar_filter(event):
    update_list_by_date(calendar.get_date())

def search_entries():
    keyword = search_box.get().lower().strip()
    entry_list.delete(0, tk.END)

    for key, value in jurnal.items():
        if keyword in value.lower():
            entry_list.insert(tk.END, key)

def schedule_auto_save():
    root.after(AUTO_SAVE_INTERVAL, lambda: save_entry(auto=True))


root = tk.Tk()
root.title("Jurnal Personal cu Calendar")
root.geometry("1100x600")

# Text editor
text_box = tk.Text(root, wrap="word", width=70, height=30)
text_box.pack(side=tk.LEFT, padx=10, pady=10)

# Right panel
right = tk.Frame(root)
right.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=10)

tk.Button(right, text="Salvează", command=save_entry).pack(fill=tk.X, pady=4)
tk.Button(right, text="Șterge", command=delete_entry).pack(fill=tk.X, pady=4)

search_box = tk.Entry(right)
search_box.pack(fill=tk.X, pady=5)
tk.Button(right, text="Caută text", command=search_entries).pack(fill=tk.X)

calendar = Calendar(
    right,
    selectmode="day",
    date_pattern="yyyy-mm-dd"
)
calendar.pack(pady=10)
calendar.bind("<<CalendarSelected>>", calendar_filter)

entry_list = tk.Listbox(right, width=40)
entry_list.pack(fill=tk.BOTH, expand=True)
entry_list.bind("<Double-1>", open_entry)

# INIT
update_list_by_date(calendar.get_date())
schedule_auto_save()

root.mainloop()