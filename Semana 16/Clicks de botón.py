import tkinter as tk
from tkinter import messagebox

class TaskApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("400x400")
        self.root.bind("<Return>", self.add_task_event)
        self.root.bind("<Escape>", lambda e: root.quit())
        self.root.bind("<c>", self.complete_task_event)
        self.root.bind("<d>", self.delete_task_event)
        self.root.bind("<Delete>", self.delete_task_event)

        self.tasks = []

        # Campo de entrada
        self.entry = tk.Entry(root, font=("Arial", 12))
        self.entry.pack(pady=10)
        self.entry.focus()

        # Botones
        self.button_frame = tk.Frame(root)
        self.button_frame.pack()

        tk.Button(self.button_frame, text="Añadir", command=self.add_task).grid(row=0, column=0, padx=5)
        tk.Button(self.button_frame, text="Completar", command=self.complete_task).grid(row=0, column=1, padx=5)
        tk.Button(self.button_frame, text="Eliminar", command=self.delete_task).grid(row=0, column=2, padx=5)

        # Lista de tareas
        self.listbox = tk.Listbox(root, width=50, font=("Arial", 12))
        self.listbox.pack(pady=10)

    def add_task(self):
        task = self.entry.get().strip()
        if task:
            self.tasks.append({"text": task, "done": False})
            self.entry.delete(0, tk.END)
            self.refresh_list()

    def add_task_event(self, event):
        self.add_task()

    def complete_task(self):
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            self.tasks[index]["done"] = not self.tasks[index]["done"]
            self.refresh_list()

    def complete_task_event(self, event):
        self.complete_task()

    def delete_task(self):
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            del self.tasks[index]
            self.refresh_list()

    def delete_task_event(self, event):
        self.delete_task()

    def refresh_list(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            text = task["text"]
            if task["done"]:
                text += " ✔️"
            self.listbox.insert(tk.END, text)

# Ejecutar aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskApp(root)
    root.mainloop()
