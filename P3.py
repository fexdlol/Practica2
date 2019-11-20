import os
os.system("cls")

n = []
s = []
e = []
a = 0
b = 0

while len(n) < 5:
    Nombre = input("Ingrese su nombre:")
    n.append(Nombre)
while len(s) < 5:
    Sexo = input("Ingrese su sexo:")
    s.append(Sexo)
    if Sexo == "Masculino":
        a += 1
    if Sexo == "Femenino":
        b += 1
while len(e) < 5:
    Edad = int(input("Ingrese su edad:"))
    if Edad>=5 and Edad<=17:
        e.append(Edad)
    else:
        print("Persona no apta")
promedio = (e[0]+e[1]+e[2]+e[3]+e[4])/5      

print("Lista de registro")
print(n)
print(s)
print(e)
print("*************************")
print("Hay", a, "hombres")
print("Hay", b, "mujeres")
print("El promdeio es", promedio)