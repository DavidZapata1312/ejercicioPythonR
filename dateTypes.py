# Solicita al usuario que ingrese un número entero
ent = int(input("ingresa un numero: "))

# Solicita un número decimal (float)
flota = float(input("ingresa un numero: "))

# Pide un texto que luego intentará convertir a número para una suma
text_sum = input("ingrese un texto para intentar sumar: ")

# Solicita un número entero que se usará para sumar al texto convertido
sumar = int(input("¿Por que numero te gustaria sumar?: "))

# Convierte el texto ingresado previamente en número entero
# (si el texto no es un número, esto lanzará un ValueError)
numASumar = int(text_sum)

# Realiza la suma entre el número convertido y el número proporcionado
resSum = numASumar + sumar

# Muestra el resultado de la suma
print(f"el resultado de la suma es: {resSum}")

# Pide otro texto, esta vez para convertirlo a número decimal para multiplicar
text_mult = input("Ingrese un texto para intentar multiplicar: ")

# Solicita el número por el que se quiere multiplicar
multiplicador = float(input("¿Por que numero te gustaria multplicar?: "))

# Convierte el texto ingresado a número decimal
multiplo = float(text_mult)

# Realiza la multiplicación
multiplicacion = multiplo * multiplicador

# Muestra el resultado de la multiplicación
print(f"El resultado de tu multiplicacion es: {multiplicacion}")

# Pide un texto cualquiera que se va a evaluar para ver si puede ser un número
texto = input("ingresa un texto: ")

# Función para verificar si un texto se puede convertir a número
def es_convertible_a_numero(texto):
    try:
        float(texto)  # Si se puede convertir a float, es un número
        return True
    except ValueError:
        # Si da error, entonces no es convertible
        return False

# Se llama a la función para evaluar si el texto ingresado es numérico o no
if es_convertible_a_numero(texto) == False:
    print("Al parecer no es numero")
else:
    print("Eso si es un numero")
