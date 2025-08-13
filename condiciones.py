# Ejemplo de condiciones en Python

# Variables
nombre = "David"
edad = 32
es_QA = True

# Verificar si la persona es QA
if es_QA:
    print(nombre, "es un QA ✅")
else:
    print(nombre, "no es QA ❌")

# Verificar si la persona es mayor de edad
if edad >= 18:
    print(nombre, "es mayor de edad")
else:
    print(nombre, "es menor de edad")

# Mensaje combinado según edad
if edad < 18:
    print("Todavía estás estudiando")
elif edad < 30:
    print("Estás en los primeros años de tu carrera")
else:
    print("Tienes experiencia acumulada en tu carrera")
