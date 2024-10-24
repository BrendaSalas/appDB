import tkinter as tk
import requests

# URL de la API para obtener los datos
url = "https://66db3d98f47a05d55be77b70.mockapi.io/api/v1/estudiante"


def obtener_ultimo_registro():
    try:
        # Hacemos una solicitud a la API para obtener todos los registros
        response = requests.get(url)
        response.raise_for_status()  # Verifica si la solicitud fue exitosa
        data = response.json()

        if data:
            # Tomamos el último registro
            ultimo_registro = data[-1]

            # Extraemos los campos del último registro
            id_ = ultimo_registro.get("id", "N/A")
            nombre = ultimo_registro.get("nombre", "N/A")
            apellido = ultimo_registro.get("apellido", "N/A")
            ciudad = ultimo_registro.get("ciudad", "N/A")
            calle = ultimo_registro.get("calle", "N/A")

            # Actualizamos la interfaz gráfica con los datos del último registro
            lbl_resultado.config(text=f"ID: {id_}\n"
                                      f"Nombre: {nombre}\n"
                                      f"Apellido: {apellido}\n"
                                      f"Ciudad: {ciudad}\n"
                                      f"Calle: {calle}")
        else:
            lbl_resultado.config(text="No se encontraron registros.")
    except requests.exceptions.RequestException as e:
        lbl_resultado.config(text=f"Error al obtener datos: {e}")


# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Último Registro del Estudiante")
ventana.geometry("300x200")

# Etiqueta para mostrar los resultados
lbl_resultado = tk.Label(ventana, text="Cargando datos...", justify="left", anchor="w")
lbl_resultado.pack(pady=20, padx=10)

# Botón para actualizar y mostrar el último registro
btn_actualizar = tk.Button(ventana, text="Actualizar Datos", command=obtener_ultimo_registro)
btn_actualizar.pack(pady=10)

# Cargar los datos al iniciar la aplicación
obtener_ultimo_registro()

# Iniciar el bucle de la aplicación
ventana.mainloop()
