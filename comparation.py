# ---------------- Comparación de números ----------------

# Solicita un primer número al usuario
num1 = int(input("Ingrese un número: "))

# Solicita un segundo número para comparar con el primero
num2 = int(input("Ingrese el número para comparar: "))

# Compara los dos números e imprime un mensaje dependiendo del resultado
if num1 == num2:
    print("Son iguales")
elif num1 > num2:
    print(f"{num1} es mayor")
else:
    print(f"{num2} es mayor")

# ---------------- Verificación de mayoría de edad ----------------

# Pide al usuario su edad
edad = int(input("Ingresa tu edad: "))

# Determina si el usuario es mayor de edad (18 o más)
if edad >= 18:
    print("Eres mayor")
else:
    print("Eres menor")

# ---------------- Comparación de textos ----------------

# Solicita el primer texto, eliminando espacios al inicio y fin, y convirtiendo todo a mayúsculas
text1 = input("Ingresa un texto: ").strip().upper()

# Solicita el segundo texto, haciendo lo mismo
text2 = input("Ingresa un texto para comparar: ").strip().upper()

# Compara ambos textos ignorando mayúsculas y espacios innecesarios
if text1 == text2:
    print("Escribiste lo mismo")
else:
    print("Son diferentes")
