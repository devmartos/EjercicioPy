numero = 5

secreto = int(input("¿Cual es el número secrero? Escoge ente el 1 y el 10  "))

if secreto == numero:
    print("Has acertado! es el número 5!")
else:
    print("Lo siento, ese no es el número, suerte la próxima vez")



x = int(input("Introduce el valor 1: "))

y = int(input("Introduce el valor 2: "))

operacion = input("Que quiere hacer con ellos? (+, -, *, /: ")

if operacion == "+":
    print(x + y)
elif operacion == "-":
    print(x - y)
elif operacion == "*":
    print(x * y)
elif operacion == "/":
    print(x / y)
else:
    print("Ups, debes escoger un simbolo corretamente.")