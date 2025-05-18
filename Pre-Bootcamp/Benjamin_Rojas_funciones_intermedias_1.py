# 1. Actualizar valores en diccionarios y listas 

# Cambiar valor en la matriz
matriz = [[10, 15, 20], [3, 7, 14]]
matriz[1][0] = 6

# Cambiar nombre del primer cantante
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]
cantantes[0]["nombre"] = "Enrique Martin Morales"

# Cambiar "Cancun" por "Monterrey"
ciudades = {
    "Mexico": ["Ciudad de Mexico", "Guadalajara", "Cancun"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}
ciudades["Mexico"][2] = "Monterrey"

# Cambiar latitud
coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]
coordenadas[0]["latitud"] = 9.9355431


print("\nValores actualizados: ")
print("Matriz:", matriz)
print("Cantantes:", cantantes)
print("Ciudades:", ciudades)
print("Coordenadas:", coordenadas)


# 2. Iterar a través de una lista de diccionarios
def iterarDiccionario(lista):
    for diccionario in lista:
        linea = []
        for clave, valor in diccionario.items():
            linea.append(f"{clave} - {valor}")
        print(", ".join(linea))


# 3. Obtener valores de una lista de diccionarios 
def iterarDiccionario2(llave, lista):
    for diccionario in lista:
        if llave in diccionario:
            print(diccionario[llave])


# 4. Iterar a través de un diccionario con valores de lista 
def imprimirInformacion(diccionario):
    for clave, lista in diccionario.items():
        print(f"{len(lista)} {clave.upper()}")
        for item in lista:
            print(item)
        print()  


# Lista extendida de cantantes
cantantes = [
    {"nombre": "Enrique Martin Morales", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "Jose Jose", "pais": "Mexico"},
    {"nombre": "Juan Luis Guerra", "pais": "Republica Dominicana"}
]

print("\nIterar Diccionario: ")
iterarDiccionario(cantantes)

print("\nIterar Diccionario 2 (nombre): ")
iterarDiccionario2("nombre", cantantes)

print("\nIterar Diccionario 2 (pais): ")
iterarDiccionario2("pais", cantantes)

print("\nImprimir Información: ")
costa_rica = {
    "ciudades": ["- San Jose", "- Limon", "- Cartago", "- Puntarenas"],
    "comidas": ["- gallo pinto", "- casado", "- tamales", "- chifrijo", "- olla de carne"]
}
imprimirInformacion(costa_rica)