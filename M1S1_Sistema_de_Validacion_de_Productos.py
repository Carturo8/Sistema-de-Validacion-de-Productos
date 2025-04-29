# Importar librería necesaria para la validación de expresiones regulares
import re

def Validar_Nombre_Producto(nombre):
    """
    Función para validar el nombre del producto.
    - Expresión regular para validar caracteres permitidos
    - Se permite letras, espacios y acentos
    - Se limita a 25 caracteres
    """    
    while True:
        producto = input(nombre).strip()
        if len(producto) > 25: # Validar longitud del nombre
            print("El nombre del producto no debe exceder los 25 caracteres.")
        elif not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]+", producto): # Validar caracteres permitidos
            print("Entrada inválida. Ingresa un nombre válido.")
        else:
            producto = producto.title()
            return producto

def Validar_Numero_Positivo(numero):
    """
    Función para validar si un número es positivo.
    """
    while True:
        try:
            valor = float(input(numero))
            if valor > 0: # Validar que el número sea positivo
                return valor
            else:
                print("El número debe ser positivo.")
        except ValueError:
            print("Entrada inválida. Ingresa un número válido.")

def Validar_Descuento(descuento):
    """
    Función para validar el descuento.
    """
    while True:
        try:
            valor = round(float(input(descuento)), 2)
            if valor >= 0 and valor <= 100: # Validar que el descuento esté entre 0 y 100
                return valor
            else:
                print("El descuento debe ser un número entre 0 y 100.")
        except ValueError:
            print("Entrada inválida. Ingresa un número válido.")

nombre = Validar_Nombre_Producto("Ingresa el nombre del producto: ") # Validar nombre
precio = Validar_Numero_Positivo("Ingresa el precio unitario del producto: ") # Validar precio
cantidad = int(Validar_Numero_Positivo("Ingresa la cantidad del producto: ")) # Validar cantidad
descuento = Validar_Descuento("Ingresa el porcentaje de descuento: ") # Validar descuento

total = round(precio * cantidad, 2) # Calcular el total sin descuento
valor_descuento = round(total * descuento/100, 2) # Calcular el valor del descuento
total_dc = round(total - valor_descuento, 2) # Calcular el total con descuento

# Mostrar toda la información de la compra de un producto
print(f"""=====================================)
Información del Producto:)
=====================================
- Nombre del Producto: {nombre}
- Precio Unitario: $ {precio}
- Cantidad: {cantidad}
- Precio Total sin Descuento: $ {total}
- Descuento: {descuento}% ---> Valor: $ {valor_descuento}
- Precio Total con Descuento: $ {total_dc}""")
