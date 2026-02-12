def division_segura(a, b):
    try:
        resultado = a / b
        return f"Resultado: {resultado}"
    except ZeroDivisionError:
        return "Error: No puedes dividir por cero, ¡matemáticas básicas!"


print("--- Mi aprendizaje en Zed ---")
num = 10
den = 0


print(division_segura(num, den))


# Es una prueba de zed simple + git nada importante la verdad xd


# segunda prueba en zed
