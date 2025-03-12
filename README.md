 FUNDAMENTOS DE PROGRAMACION 
 <hr>
<p>Repositorio 
<p>Institución: Universidad Estatal Amazónica</p>
<p>Estudiante: Jefferson Alexis Basurto López.</p>
<p>Carrera: Ingeniería en Tecnologías de la Información y Comunicación</p>
<p>Docente: Ing. Edwin Gustavo Fernández Sánchez, Mgs.
</p>
# Definir dimensiones de la matriz
ciudades = ["Ciudad A", "Ciudad B", "Ciudad C"]
dias = ["lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
        Semanas = 2# Número de semanas 7
# Crear la matriz 3D con temperaturas aleatorias entre 10 y 35 grados
matriz_temperaturas = [[[random.randint(10, 35) for _ in dias] for _ in rang 10
# Calcular y mostrar el promedio de temperaturas por ciudad y semana
for i, ciudad in enumerate(ciudades):
    print(f"\nPromedio de temperaturas para {ciudad}:")
for semana in range(semanas):
    promedio = sum(matriz_temperaturas[i][semana]) / len(dias)
print(f"	Semana {semana + 1}: {promedio:.2f}°C")
