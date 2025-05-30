definir sumar(a, b):
    devolver a + b

definir restar(a, b):
    devolver a - b

definir multiplicar(a, b):
    devolver a * b

definir dividir(a, b):
    si b != 0:
        devolver a / b
    sino:
        imprimir("No se puede dividir por cero.")
        devolver Ninguno

imprimir("Calculadora simple")
num1 = int(entrada("Ingrese el primer número: "))
num2 = int(entrada("Ingrese el segundo número: "))

imprimir("Suma:", sumar(num1, num2))
imprimir("Resta:", restar(num1, num2))
imprimir("Multiplicación:", multiplicar(num1, num2))
imprimir("División:", dividir(num1, num2))
