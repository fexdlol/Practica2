import os
import random
os.system("cls")

tamaño = int(input("Ingrese el tamaño:"))
while True:
    if(tamaño>=2 and tamaño<=5):
        break
    else:
        tamaño = int(input("Ingrese el tamaño:"))
matriz = []
for i in range(0, tamaño):
    matriz.append([])
for i in range(0, tamaño):
    matriz[0].append(random.randint(1,100))
for i in range(0, tamaño):
    matriz[1].append(random.randint(1,100))
for i in range(0, tamaño):
    matriz[2].append(random.randint(1,100))
for i in range(0, tamaño):
    matriz[3].append(random.randint(1,100))
for i in range(0, tamaño):
    matriz[4].append(random.randint(1,100))

print(f"matriz{matriz[0]}\n{matriz[1]}")