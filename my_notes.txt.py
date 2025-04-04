# Crea un nuevo archivo llamado my_notes.txt
try:
    archivo = open("my_notes.txt", "w")  # Abre el archivo en modo escritura ('w')
    # Escribe al menos tres líneas de notas personales en el archivo
    archivo.write("Trabajar en el día.\n")
    archivo.write("Hacer tareas.\n")
    archivo.write("Terminar el proyecto de física.\n")
    print("Notas escritas en el archivo my_notes.txt")
except Exception as e:
    print(f"Error al crear o escribir en el archivo: {e}")
finally:
    if 'archivo' in locals() and 'archivo': # Verifica si el archivo fue abierto correctamente
        archivo.close() # Cierra el archivo


# Parte 2: Lectura de Archivo de Texto

# Abre el archivo my_notes.txt en modo lectura ('r')
try:
    archivo = open("my_notes.txt", "r")
    # Lee el contenido del archivo línea por línea
    linea = archivo.readline()
    while linea:
        # Muestra en la consola cada línea leída
        print(linea, end="")  # end="" evita un salto de línea extra
        linea = archivo.readline()
except FileNotFoundError:
    print("El archivo my_notes.txt no se encuentra.")
except Exception as e:
    print(f"Error al leer el archivo: {e}")
finally:
    if 'archivo' in locals() and archivo: # Verifica si el archivo fue abierto correctamente
        archivo.close() # Cierra el archivo


# Parte 3: Cierre de Archivos (Ya se realiza en las partes 1 y 2 con finally)