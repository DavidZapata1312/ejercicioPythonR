# Solicita al usuario la base del rectángulo
base = int(input("Ingresa la base de tu rectángulo: "))

# Solicita la altura del rectángulo
alt = int(input("Ingresa la altura de tu rectángulo: "))

# Calcula el área del rectángulo (base * altura)
area = base * alt

# Muestra el resultado del cálculo del área
print(f"El área es {area}")

# ---------------- Cálculo de descuento ----------------

# Pide el precio original de un producto
price = int(input("Ingresa un precio: "))

# Solicita el descuento en porcentaje
discontVal = float(input("Ingresa el descuento (%): "))

# Calcula el valor del descuento aplicando el porcentaje
discont = price * discontVal / 100

# Calcula el precio final restando el descuento al precio original
finalPrice = price - discont

# Muestra el valor final a pagar luego del descuento
print(f"El valor a pagar es: {finalPrice}")

# ---------------- Cálculo de residuo ----------------

# Pide el primer número para dividir
val1 = int(input("Ingrese el primer número a dividir: "))

# Pide el segundo número para dividir
val2 = int(input("Ingrese el segundo número a dividir: "))

# Calcula el residuo (módulo) de la división
residuo = val1 % val2

# Muestra el residuo
print(f"El residuo es {residuo}")

# ---------------- Operación combinada ----------------

# Solicita cuatro valores numéricos al usuario
num1 = int(input("Ingrese un valor: "))
num2 = int(input("Ingrese otro valor: "))
num3 = int(input("Ingrese otro valor más: "))
num4 = int(input("Ingrese un último valor: "))

# Realiza la operación: (num1 + num2) * num3 / num4
restOp = (num1 + num2) * num3 / num4

# Muestra el resultado con un mensaje explicativo
print(f"El resultado de {num1} + {num2} multiplicado por {num3} y dividido {num4} es {restOp}")
