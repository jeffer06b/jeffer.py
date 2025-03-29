informacion_persona1 = {
    "nombre": "Alexis",
    "edad": 30,
    "ciudad": "Guayaquil",
    "profesion": "Ingeniera"
}
if "telefono" not in informacion_persona1:
    informacion_persona1["telefono"] = "0993742130"
    del informacion_persona1["edad"]
    print(informacion_persona1)