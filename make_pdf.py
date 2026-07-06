import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os
import json

CONFIG_FILE = "pdf_builder_config.json"

def load_config():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as f:
                return json.load(f)
        except:
            return {"output_dir": ""}
    return {"output_dir": ""}

def save_config(output_dir):
    with open(CONFIG_FILE, "w") as f:
        json.dump({"output_dir": output_dir}, f)

class PDFBuilderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Manuscript Builder")
        self.root.geometry("450x350")
        
        self.config = load_config()
        self.selected_md = None
        self.output_dir = self.config.get("output_dir", "")

        # --- MD Selection ---
        tk.Button(root, text="Select Markdown Manuscript", command=self.on_select_md).pack(pady=10)
        self.lbl_md = tk.Label(root, text="No file selected", fg="gray")
        self.lbl_md.pack()

        # --- Output Selection ---
        tk.Button(root, text="Select PDF Output Directory", command=self.on_select_output).pack(pady=10)
        self.lbl_output = tk.Label(root, text=self.output_dir if self.output_dir else "Default: Source Directory", fg="blue", wraplength=400)
        self.lbl_output.pack()

        # --- Control Frame (To hold the buttons side-by-side) ---
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=30)

        # --- View in Micro Button ---
        tk.Button(btn_frame, text="View in Micro", command=self.on_view_md, height=2, width=15).pack(side=tk.LEFT, padx=5)

        # --- Export Button ---
        self.btn_export = tk.Button(btn_frame, text="EXPORT PDF", command=self.on_export, bg="green", fg="white", height=2, width=15)
        self.btn_export.pack(side=tk.LEFT, padx=5)

    def on_select_md(self):
        file_path = filedialog.askopenfilename(filetypes=[("Markdown files", "*.md")])
        if file_path:
            self.selected_md = file_path
            self.lbl_md.config(text=os.path.basename(file_path), fg="black")

    def on_select_output(self):
        dir_path = filedialog.askdirectory()
        if dir_path:
            self.output_dir = dir_path
            self.lbl_output.config(text=dir_path, fg="black")
            save_config(dir_path)

    def on_view_md(self):
        if not self.selected_md:
            messagebox.showwarning("Warning", "Please select a Markdown file first.")
            return
        
        # Opens micro in a new terminal window
        # Note: 'gnome-terminal' is the standard for most Linux distros. 
        # If it doesn't open, change 'gnome-terminal' to 'xterm' or 'konsole'.
        try:
            subprocess.Popen(["gnome-terminal", "--", "micro", self.selected_md])
        except FileNotFoundError:
            messagebox.showerror("Error", "Could not find terminal emulator (gnome-terminal). Check your PATH.")

    def on_export(self):
        if not self.selected_md:
            messagebox.showwarning("Error", "Please select a Markdown file first.")
            return

        self.btn_export.config(text="Exporting...", state="disabled")
        self.root.update()

        base_name = os.path.splitext(os.path.basename(self.selected_md))[0]
        target_dir = self.output_dir if self.output_dir else os.path.dirname(self.selected_md)
        output_path = os.path.join(target_dir, base_name + ".pdf")

        cmd = [
            "pandoc", 
            self.selected_md, 
            "-o", output_path, 
            "--pdf-engine=xelatex",
            "--resource-path=.:assets/images"
        ]
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=False)
            self.btn_export.config(text="EXPORT PDF", state="normal")
            
            if result.returncode == 0:
                messagebox.showinfo("Success", f"PDF saved to:\n{output_path}")
            else:
                messagebox.showerror("Pandoc Error", f"Pandoc failed:\n{result.stderr}")
        except Exception as e:
            self.btn_export.config(text="EXPORT PDF", state="normal")
            messagebox.showerror("Error", f"Could not run Pandoc: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFBuilderApp(root)
    root.mainloop()
