nombre = input("Ingresa tu nombre\n")
if nombre=="Valeria Soto Hernandez":
    print("LA GENTE MENTIROSA ESTA RESTRINGIDA DE ESTE CODIGO EPIQUISIMO \nNIMODOTE AMOR")
    exit()

email=input("Ingresa tu correo electronico\n")
# Validar el correo electrónico
if "@" not in email or "." not in email:
  print("El correo electrónico no es válido.")
  exit()

edad = int(input("Ingresa tu edad\n"))
if edad <18:
    print("Tas muy chavo we")
    exit()



print(f"Bienvenido {nombre}, Empieza a calcular")

num1 = int(input("Ingresa el primer numero\n"))
operacion = input("Ingresa la operacion a realizar (+, -, *, /)\n")
num2 = int(input("Ingresa el segundo numero\n"))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
divicion = num1 / num2


if operacion == "+":
  print("El resultado de ", num1, "+", num2, " es: ", suma)
elif operacion == "-":
    print("El resultado de ", num1, "-", num2, " es: ", resta)
elif operacion == "*":
    print("El resultado de ", num1, "*", num2, " es: ", multiplicacion)
elif operacion == "/":
    print("El resultado de ", num1, "/", num2, " es: ", divicion)
else:
    print("La operacion es invalida")

oo = int(input("Deseas realizar otra operacion con ese resultado? y/n"))

if oo == "y":
    operacion2 = input("Ingresa la operacion a realizar (+, -, *, /)\n")
    num3 = int(input("Ingresa el segundo numero\n"))

    if operacion2 == "+":
        print("El resultado de ", suma, "+", num3, " es: ", suma + num3)
    elif operacion2 == "-":
        print("El resultado de ", resta, "-", num3, " es: ", resta - num3)
    elif operacion2 == "*":
        print("El resultado de ", multiplicacion, "*", num3, " es: ", multiplicacion * num3)
    elif operacion2 == "/":
        print("El resultado de ", divicion, "/", num3, " es: ", divicion / num3)
    else:
        print("La operacion es invalida")

elif oo == "n":
    print("Hara luego...")
    exit()    


