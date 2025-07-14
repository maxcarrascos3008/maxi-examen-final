productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
    'FS1230HD': ['HP', 15.6, '4GB', 'DD', '500GB', 'Intel Celeron', 'integrada']
}


stock = {
    '8475HD': [387990, 10], '2175HD': [327990, 4], 'JjfFHD': [424990, 1],
    'fgdxFHD': [664990, 21], '123FHD': [290890, 32], '342FHD': [444990, 7],
    'GF75HD': [749990, 2], 'UWU131HD': [349990, 1], 'FS1230HD': [249990, 0]
}

def stock_marca(marca):
    marca = marca.lower()
    encontrado = False
    for modelo, datos in productos.items():
        if datos[0].lower() == marca:
            encontrado = True
            print(f'Modelo: {modelo} - Stock: {stock[modelo][1]}')
    if not encontrado:
        print("No hay notebooks de esa marca.")

def busqueda_precio(p_min, p_max):
    resultados = []
    for modelo, datos_stock in stock.items():
        precio, cantidad = datos_stock
        if p_min <= precio <= p_max and cantidad > 0:
            marca = productos[modelo][0]
            resultados.append(f'{marca}--{modelo}')
    
    if resultados:
        resultados.sort()
        print("Resultados encontrados:")
        for res in resultados:
            print(res)
    else:
        print("No hay notebooks en ese rango de precios.")

def actualizar_precio(modelo, nuevo_precio):
    if modelo in stock:
        stock[modelo][0] = nuevo_precio
        return True
    else:
        return False

def main():
    while True:
        print("\n*** MENU PRINCIPAL ***")
        print("1. Stock marca")
        print("2. Búsqueda por precio")
        print("3. Actualizar precio")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            marca = input("Ingrese la marca: ")
            stock_marca(marca)

        elif opcion == "2":
            while True:
                try:
                    p_min = int(input("Ingrese precio mínimo: "))
                    p_max = int(input("Ingrese precio máximo: "))
                    break
                except ValueError:
                    print("Debe ingresar valores enteros!!")
            busqueda_precio(p_min, p_max)

        elif opcion == "3":
            while True:
                modelo = input("Ingrese el modelo: ")
                try:
                    nuevo_precio = int(input("Ingrese el nuevo precio: "))
                except ValueError:
                    print("Debe ingresar un precio válido (número entero).")
                    continue

                actualizado = actualizar_precio(modelo, nuevo_precio)
                if actualizado:
                    print("Precio actualizado!!")
                else:
                    print("El modelo no existe!!")

                otra = input("¿Desea actualizar otro precio? (si/no): ").strip().lower()
                if otra != "si":
                    break

        elif opcion == "4":
            print("Programa finalizado.")
            break

        else:
            print("Debe seleccionar una opción válida!!")

main()
