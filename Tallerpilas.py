import tkinter as tk
from tkinter import ttk, messagebox


historial = [
    ("Google",   "https://www.google.com/?hl=es", "10:15:00 - 24/08/2026"),
    ("GitHub",   "https://github.com/",            "10:15:00 - 24/08/2026"),
    ("YouTube",  "https://www.youtube.com/",        "10:15:00 - 24/08/2026"),
]


class Historial:
    def __init__(self, root):          # ✅ FIX 1: __init__ not _init_
        self.root = root
        self.root.title("Historial WebLine")
        self.root.geometry("620x340")
        self.root.resizable(True, True)

        # ── Title ──────────────────────────────────────────────────
        titulo = tk.Label(                         # ✅ FIX 2: Label not label
            self.root,
            text="📋  Historial WebLine",
            font=("Arial", 13, "bold")
        )
        titulo.pack(pady=10)

        # ── Table frame ────────────────────────────────────────────
        frame_table = tk.Frame(self.root)          # ✅ FIX 3: Frame not frame
        frame_table.pack(fill=tk.BOTH, expand=True, padx=20)

        columns = ("Title", "Url", "Day and time")

        # ✅ FIX 4: use ttk.Treeview (not tk.Treeview — it doesn't exist)
        self.table = ttk.Treeview(
            frame_table, columns=columns, show="headings"
        )

        # ✅ FIX 5: self.table (lowercase) everywhere — was mixed Table/table
        self.table.heading("Title",        text="Title")
        self.table.heading("Url",          text="URL")
        self.table.heading("Day and time", text="Day and time")

        self.table.column("Title",        width=120, anchor="w")
        self.table.column("Url",          width=280, anchor="w")
        self.table.column("Day and time", width=160, anchor="center")

        # ✅ FIX 6: scrollbar must attach to self.table.yview, not self.root.yview
        scrollbar = tk.Scrollbar(
            frame_table, orient=tk.VERTICAL, command=self.table.yview
        )
        self.table.configure(yscrollcommand=scrollbar.set)  # ✅ FIX 7: yscrollcommand not yscroll

        self.table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.load_data()

        # ── Buttons ────────────────────────────────────────────────
        frame_buttons = tk.Frame(self.root)
        frame_buttons.pack(pady=10)

        btn_delete = tk.Button(
            frame_buttons, text="Delete",
            command=self.delete_selected,
            bg="red", fg="white", width=10
        )
        btn_delete.pack(side=tk.LEFT, padx=5)

        btn_clear = tk.Button(
            frame_buttons, text="Clear All",
            command=self.clear_table,
            bg="blue", fg="white", width=10
        )
        btn_clear.pack(side=tk.LEFT, padx=5)

    # ── Load initial data ──────────────────────────────────────────
    def load_data(self):                           # ✅ FIX 8: consistent snake_case
        for item in historial:
            self.table.insert("", tk.END, values=item)

    # ── Delete selected row ────────────────────────────────────────
    def delete_selected(self):
        selected_item = self.table.selection()
        if selected_item:
            self.table.delete(selected_item)
            messagebox.showinfo("Delete", "Selected item deleted successfully.")
        else:
            messagebox.showwarning("Delete", "Please select an item to delete.")

    # ── Clear all rows ─────────────────────────────────────────────
    def clear_table(self):
        self.table.delete(*self.table.get_children())
        messagebox.showinfo("Clear", "Table cleared successfully.")



if __name__ == "__main__":
    root = tk.Tk()
    app = Historial(root)
    root.mainloop()