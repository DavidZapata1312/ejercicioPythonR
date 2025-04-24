# ---------------- Comparación entre dos números ----------------

# Se solicita al usuario que ingrese un primer número entero
num1 = int(input("Ingrese un número: "))

# Se solicita un segundo número para comparar con el primero
num2 = int(input("Ingrese el número para comparar: "))

# Se evalúa si ambos números son iguales
if num1 == num2:    
    print("Son iguales")
# Se evalúa si el primer número es mayor al segundo
elif num1 > num2:
    print(f"{num1} es mayor")
# Si no son iguales y num1 no es mayor, entonces num2 es el mayor
else:
    print(f"{num2} es mayor")

# ---------------- Verificación de mayoría de edad ----------------

# Se pide al usuario que ingrese su edad
edad = int(input("Ingresa tu edad: "))

# Se evalúa si el usuario es mayor de edad (18 o más)
if edad >= 18:
    print("Eres mayor")
# Si no es mayor de edad, se indica que es menor
else:
    print("Eres menor")

# ---------------- Comparación de textos (ignorando mayúsculas/minúsculas y espacios) ----------------

# Se solicita al usuario que ingrese un primer texto
# Se eliminan espacios al inicio/final y se convierte a mayúsculas para normalizar
text1 = input("Ingresa un texto: ").strip().upper()

# Se solicita un segundo texto y se aplica el mismo tratamiento
text2 = input("Ingresa un texto para comparar: ").strip().upper()

# Se comparan los textos normalizados
if text1 == text2:
    print("Escribiste lo mismo")
# Si no son iguales, se indica que son diferentes
else:
    print("Son diferentes")
