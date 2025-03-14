import tkinter as tk
from tkinter import ttk, messagebox

# Crear ventana principal
app = tk.Tk()
app.title("📋 Tu Lista de Tareas 📋")
app.geometry("450x400")
app.configure(bg="#598392")  # Color de fondo principal

# **Título con nueva fuente y color**
titulo = tk.Label(app, text="📌 ¡Organiza tus Tareas! 📌",
                  font=("Comic Sans MS", 14, "bold"), bg="#598392", fg="white")
titulo.pack(pady=5)

# **Campo de entrada**
tk.Label(app, text="Nueva Tarea:", font=("Comic Sans MS", 10), bg="#598392", fg="white").pack()
entrada_tarea = tk.Entry(app, width=40, font=("Comic Sans MS", 10))
entrada_tarea.pack(pady=5)

# **Función para agregar tarea**
def agregar_tarea():
    tarea = entrada_tarea.get()
    if tarea.strip() == "":
        messagebox.showwarning("⚠️ Atención", "Por favor, ingresa una tarea.")
        return
    tabla.insert("", "end", values=(tarea,))
    entrada_tarea.delete(0, tk.END)

# **Función para eliminar tarea seleccionada**
def eliminar_tarea():
    seleccionado = tabla.selection()
    if not seleccionado:
        messagebox.showwarning("⚠️ Atención", "Selecciona una tarea para eliminar.")
        return
    tabla.delete(seleccionado)

# **Función para limpiar todas las tareas**
def limpiar_todo():
    confirmacion = messagebox.askyesno("⚠️ Confirmar", "¿Deseas eliminar TODAS las tareas?")
    if confirmacion:
        for item in tabla.get_children():
            tabla.delete(item)

# **Marco para los botones con nuevo color**
frame_botones = tk.Frame(app, bg="#aec3b0")
frame_botones.pack(pady=5, fill=tk.X)

# **Botones con nuevos colores y fuente Comic Sans**
btn_agregar = tk.Button(frame_botones, text="✅ Agregar", command=agregar_tarea, bg="#2E8B57", fg="white",
                        font=("Comic Sans MS", 10, "bold"))
btn_agregar.grid(row=0, column=0, padx=5, pady=5)

btn_eliminar = tk.Button(frame_botones, text="❌ Eliminar", command=eliminar_tarea, bg="#B22222", fg="white",
                         font=("Comic Sans MS", 10, "bold"))
btn_eliminar.grid(row=0, column=1, padx=5, pady=5)

btn_limpiar = tk.Button(frame_botones, text="🗑️ Limpiar Todo", command=limpiar_todo, bg="#8B0000", fg="white",
                        font=("Comic Sans MS", 10, "bold"))
btn_limpiar.grid(row=0, column=2, padx=5, pady=5)

btn_salir = tk.Button(frame_botones, text="🚪 Salir", command=app.quit, bg="black", fg="white",
                      font=("Comic Sans MS", 10, "bold"))
btn_salir.grid(row=0, column=3, padx=5, pady=5)

# **Tabla para mostrar las tareas con color personalizado**
style = ttk.Style()
style.configure("Treeview", background="#aec3b0", font=("Comic Sans MS", 10))
style.configure("Treeview.Heading", font=("Comic Sans MS", 10, "bold"))

tabla = ttk.Treeview(app, columns=("Tarea"), show="headings")
tabla.heading("Tarea", text="📌 Tareas Pendientes")
tabla.column("Tarea", width=350, anchor="center")
tabla.pack(pady=10, fill=tk.BOTH, expand=True)

# **Ejecutar la aplicación**
app.mainloop()
