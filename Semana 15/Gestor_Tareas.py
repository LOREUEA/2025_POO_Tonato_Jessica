import tkinter as tk
from tkinter import ttk, messagebox

class GestorTareas:
    def _init(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.configure(bg="#f4f4f4")
        self.root.geometry("600x500")
        self.fuente = ("Segoe UI", 10)

        # Estilos
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Azul.TButton", font=self.fuente, background="#2F4F6F", foreground="white", padding=8)
        style.map("Azul.TButton", background=[("active", "#223E5C")])
        style.configure("Gris.TButton", font=self.fuente, background="#888888", foreground="white", padding=8)
        style.map("Gris.TButton", background=[("active", "#6e6e6e")])
        style.configure("Dorado.TButton", font=self.fuente, background="#D4AF37", foreground="white", padding=8)
        style.map("Dorado.TButton", background=[("active", "#B89C3A")])

        # Frame superior
        frame_superior = tk.Frame(root, bg="#f4f4f4")
        frame_superior.pack(fill="x", padx=20, pady=(20, 10))

        self.entrada = ttk.Entry(frame_superior, font=self.fuente)
        self.entrada.pack(side="left", expand=True, fill="x", padx=(0, 10))
        self.entrada.bind("<Return>", self.agregar_tarea_evento)

        self.btn_añadir = ttk.Button(frame_superior, text="➕ Añadir", style="Azul.TButton", command=self.agregar_tarea)
        self.btn_añadir.pack(side="right")

        # Treeview
        self.tree = ttk.Treeview(root, columns=("Tarea", "Estado"), show="headings", height=12)
        self.tree.pack(padx=20, pady=10, fill="both", expand=True)

        self.tree.heading("Tarea", text="📝 Tarea")
        self.tree.heading("Estado", text="✅ Estado")
        self.tree.column("Tarea", width=350, anchor="w")
        self.tree.column("Estado", width=120, anchor="center")

        scrollbar = ttk.Scrollbar(root, orient="vertical", command=self.tree.yview)
        scrollbar.place(x=580, y=90, height=300)
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Botones inferiores
        frame_botones = tk.Frame(root, bg="#f4f4f4")
        frame_botones.pack(pady=10)

        self.btn_completar = ttk.Button(frame_botones, text="✅ Marcar como Hecha", style="Gris.TButton", command=self.marcar_completada)
        self.btn_completar.grid(row=0, column=0, padx=5)

        self.btn_eliminar = ttk.Button(frame_botones, text="🗑 Eliminar Actividad", style="Dorado.TButton", command=self.eliminar_tarea)
        self.btn_eliminar.grid(row=0, column=1, padx=5)

        self.btn_limpiar = ttk.Button(frame_botones, text="🧹 Limpiar Todo", style="Gris.TButton", command=self.limpiar_todo)
        self.btn_limpiar.grid(row=0, column=2, padx=5)

        # Etiqueta de ayuda
        ayuda = tk.Label(root, text="📌 Escribe una tarea → presiona Enter → se añade ✔\n"
                                    "Selecciona una tarea y presiona C → se marca como completada\n"
                                    "Selecciona una tarea y presiona D o Delete → se elimina 🗑\n"
                                    "Presiona Escape → se cierra la app",
                         bg="#f4f4f4", font=("Segoe UI", 9), justify="left", anchor="w")
        ayuda.pack(pady=(0, 10), padx=20, anchor="w")

        # Atajos de teclado
        self.root.bind("<c>", lambda e: self.marcar_completada())
        self.root.bind("<C>", lambda e: self.marcar_completada())
        self.root.bind("<d>", lambda e: self.eliminar_tarea())
        self.root.bind("<D>", lambda e: self.eliminar_tarea())
        self.root.bind("<Delete>", lambda e: self.eliminar_tarea())
        self.root.bind("<Escape>", lambda e: self.root.destroy())

    def agregar_tarea(self):
        texto = self.entrada.get().strip()
        if texto:
            self.tree.insert("", "end", values=(texto, "Pendiente"))
            self.entrada.delete(0, tk.END)
        else:
            messagebox.showwarning("⚠ Campo vacío", "Por favor escribe una tarea.")

    def agregar_tarea_evento(self, event):
        self.agregar_tarea()

    def marcar_completada(self):
        seleccion = self.tree.selection()
        if seleccion:
            for item in seleccion:
                self.tree.item(item, values=(self.tree.item(item, "values")[0], "✔ Hecha"))
                self.tree.tag_configure("hecho", background="#d0f0c0")
                self.tree.item(item, tags=("hecho",))
        else:
            messagebox.showinfo("ℹ", "Selecciona al menos una tarea para marcar como hecha.")

    def eliminar_tarea(self):
        seleccion = self.tree.selection()
        if seleccion:
            for item in seleccion:
                self.tree.delete(item)
        else:
            messagebox.showinfo("ℹ", "Selecciona una tarea para eliminar.")

    def limpiar_todo(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

# Ejecutar la app
if _name_ == "_main":
    root = tk.Tk()
    app = GestorTareas(root)
    root.mainloop()