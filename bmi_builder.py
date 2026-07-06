import tkinter as tk
from tkinter import filedialog, messagebox
import os
import json

class ManuscriptBuilder:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Framework Manuscript Builder")
        self.root.geometry("800x550")
        self.root.configure(bg="#f0f0f0")
        
        self.file_paths = []

        # Configure root grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)

        # Header Label
        header = tk.Label(self.root, text="Manuscript File Order:", font=("Arial", 12, "bold"), bg="#f0f0f0")
        header.grid(row=0, column=0, sticky="w", padx=15, pady=(15, 5))

        # Main Listbox
        self.listbox = tk.Listbox(self.root, selectmode=tk.SINGLE, font=("Arial", 11))
        self.listbox.grid(row=1, column=0, sticky="nsew", padx=(15, 5), pady=(0, 15))
        
        # Scrollbar
        scrollbar = tk.Scrollbar(self.root, command=self.listbox.yview)
        scrollbar.grid(row=1, column=1, sticky="ns", pady=(0, 15))
        self.listbox.config(yscrollcommand=scrollbar.set)

        # Button Panel
        btn_frame = tk.Frame(self.root, bg="#f0f0f0")
        btn_frame.grid(row=1, column=2, sticky="n", padx=15, pady=0)

        # File Management Buttons
        tk.Button(btn_frame, text="Add Files...", width=18, bg="#e0e0e0", command=self.add_files).pack(pady=5)
        tk.Button(btn_frame, text="Move Up", width=18, bg="#e0e0e0", command=self.move_up).pack(pady=5)
        tk.Button(btn_frame, text="Move Down", width=18, bg="#e0e0e0", command=self.move_down).pack(pady=5)
        tk.Button(btn_frame, text="Remove Selected", width=18, bg="#e0e0e0", command=self.remove_file).pack(pady=5)
        
        # Project Save/Load Buttons
        tk.Frame(btn_frame, height=20, bg="#f0f0f0").pack()
        tk.Button(btn_frame, text="Save Project", width=18, bg="#d0d0d0", command=self.save_project).pack(pady=2)
        tk.Button(btn_frame, text="Load Project", width=18, bg="#d0d0d0", command=self.load_project).pack(pady=2)
        
        tk.Frame(btn_frame, height=40, bg="#f0f0f0").pack()
        
        # Build Button
        tk.Button(btn_frame, text="BUILD MASTER", width=18, height=2, bg="#8b0000", fg="white", font=("Arial", 10, "bold"), command=self.build_manuscript).pack(pady=10)

    def add_files(self):
        files = filedialog.askopenfilenames(title="Select Markdown Files", filetypes=(("Markdown Files", "*.md"), ("All Files", "*.*")))
        for f in files:
            if f not in self.file_paths:
                self.file_paths.append(f)
                self.listbox.insert(tk.END, os.path.basename(f))

    def move_up(self):
        try:
            idx = self.listbox.curselection()[0]
            if idx > 0:
                text = self.listbox.get(idx)
                self.listbox.delete(idx)
                self.listbox.insert(idx - 1, text)
                self.file_paths[idx], self.file_paths[idx - 1] = self.file_paths[idx - 1], self.file_paths[idx]
                self.listbox.select_set(idx - 1)
        except IndexError: pass

    def move_down(self):
        try:
            idx = self.listbox.curselection()[0]
            if idx < self.listbox.size() - 1:
                text = self.listbox.get(idx)
                self.listbox.delete(idx)
                self.listbox.insert(idx + 1, text)
                self.file_paths[idx], self.file_paths[idx + 1] = self.file_paths[idx + 1], self.file_paths[idx]
                self.listbox.select_set(idx + 1)
        except IndexError: pass

    def remove_file(self):
        try:
            idx = self.listbox.curselection()[0]
            self.listbox.delete(idx)
            self.file_paths.pop(idx)
        except IndexError: pass

    def save_project(self):
        filename = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json")])
        if filename:
            with open(filename, 'w') as f:
                json.dump(self.file_paths, f)
            messagebox.showinfo("Saved", "Project configuration saved.")

    def load_project(self):
        filename = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
        if filename:
            with open(filename, 'r') as f:
                self.file_paths = json.load(f)
                self.listbox.delete(0, tk.END)
                for path in self.file_paths:
                    self.listbox.insert(tk.END, os.path.basename(path))

    def build_manuscript(self):
        if not self.file_paths:
            messagebox.showwarning("Empty List", "Please add some files first.")
            return

        master_filename = "Master_BMI_Manuscript.md"
        try:
            with open(master_filename, 'w', encoding='utf-8') as master_file:
                for path in self.file_paths:
                    with open(path, 'r', encoding='utf-8') as f:
                        master_file.write(f.read())
                        master_file.write("\n\n\\newpage\n\n") 
            messagebox.showinfo("Success", f"Compiled into {master_filename}!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to build:\n{str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ManuscriptBuilder(root)
    root.mainloop()
