import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import re  # Para validar hora


class Evento:
    def __init__(self, fecha, hora, descripcion):
        self.fecha = fecha
        self.hora = hora
        self.descripcion = descripcion


class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📔 Agenda Personal")
        self.root.configure(bg="#f0f4f7")  # Color de fondo

        self.eventos = []

        # 🪟 Fuente
        fuente = ("Helvetica", 12)

        # Frame principal
        self.frame_principal = tk.Frame(root, bg="#f0f4f7", padx=10, pady=10)
        self.frame_principal.pack()

        # TreeView con estilo
        self.tree = ttk.Treeview(self.frame_principal, columns=("Fecha", "Hora", "Descripción"), show="headings", height=6)
        self.tree.heading("Fecha", text="📅 Fecha")
        self.tree.heading("Hora", text="🕒 Hora")
        self.tree.heading("Descripción", text="📝 Descripción")
        self.tree.pack(pady=10)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Helvetica", 11))
        style.configure("Treeview", font=("Helvetica", 11))

        # Frame de entrada
        self.frame_entrada = tk.Frame(self.frame_principal, bg="#f0f4f7")
        self.frame_entrada.pack()

        tk.Label(self.frame_entrada, text="📅 Fecha:", font=fuente, bg="#f0f4f7").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.date_entry = DateEntry(self.frame_entrada, width=12, background='navy', foreground='white',
                                    borderwidth=2, date_pattern='dd/mm/yyyy', font=fuente)
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.frame_entrada, text="🕒 Hora (HH:MM):", font=fuente, bg="#f0f4f7").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.hora_entry = tk.Entry(self.frame_entrada, font=fuente)
        self.hora_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.frame_entrada, text="📝 Descripción:", font=fuente, bg="#f0f4f7").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.descripcion_entry = tk.Entry(self.frame_entrada, font=fuente)
        self.descripcion_entry.grid(row=2, column=1, padx=5, pady=5)

        # Botones
        self.frame_botones = tk.Frame(self.frame_principal, bg="#f0f4f7")
        self.frame_botones.pack(pady=10)

        boton_estilo = {"font": fuente, "bg": "#1f6aa5", "fg": "white", "width": 18}

        tk.Button(self.frame_botones, text="➕ Agregar Evento", command=self.agregar_evento, **boton_estilo).grid(row=0, column=0, padx=10)
        tk.Button(self.frame_botones, text="❌ Eliminar Evento", command=self.eliminar_evento, **boton_estilo).grid(row=0, column=1, padx=10)
        tk.Button(self.frame_botones, text="🚪 Salir", command=self.root.quit, **boton_estilo).grid(row=0, column=2, padx=10)

    def agregar_evento(self):
        fecha = self.date_entry.get()
        hora = self.hora_entry.get()
        descripcion = self.descripcion_entry.get()

        # Validación de hora: HH:MM (formato 24 horas)
        if not re.match(r'^([01]?[0-9]|2[0-3]):[0-5][0-9]$', hora):
            messagebox.showerror("⛔ Hora inválida", "Ingresa una hora válida en formato HH:MM (ej. 08:30 o 14:00)")
            return

        if not descripcion.strip():
            messagebox.showwarning("⚠️ Campo vacío", "Por favor ingresa una descripción.")
            return

        evento = Evento(fecha, hora, descripcion)
        self.eventos.append(evento)
        self.tree.insert("", "end", values=(evento.fecha, evento.hora, evento.descripcion))

        self.hora_entry.delete(0, tk.END)
        self.descripcion_entry.delete(0, tk.END)

    def eliminar_evento(self):
        item = self.tree.selection()
        if not item:
            messagebox.showwarning("⚠️ Ninguna Selección", "Seleccione un evento para eliminar.")
            return

        confirmar = messagebox.askyesno("❓ Confirmar", "¿Deseas eliminar el evento seleccionado?")
        if confirmar:
            self.tree.delete(item)


if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
