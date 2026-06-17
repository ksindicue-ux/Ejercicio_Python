cantidad = int(input("ingrese el numero de productos a registrar: "))
Nombres = []
Precios = []
for i in range(cantidad):
    a=input("Nombre del producto: ")
    b=int(input("Precio del producto: "))
    if b>0:
        Nombres.append(a)
        Precios.append(b)
for i in range(len(Nombres)):
    print(Nombres[i],Precios[i])
total = 0
for i in range(len(Precios)):
    total += Precios[i]
Promedio = total/len(Precios)
print(f"El total es ",total)
print(f"El promedio es ",Promedio)