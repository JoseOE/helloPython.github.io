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


if operacion == "+":
  print("El resultado de ", num1, "+", num2, " es: ", num1 + num2)
elif operacion == "-":
    print("El resultado de ", num1, "-", num2, " es: ", num1 - num2)
elif operacion == "*":
    print("El resultado de ", num1, "*", num2, " es: ", num1 * num2)
elif operacion == "/":
    print("El resultado de ", num1, "/", num2, " es: ", num1 / num2)
else:
    print("La operacion es invalida")