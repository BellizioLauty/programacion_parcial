
from calcular import total_juguetes_por_provincia
from deposito_mayor_recaudacion import deposito_mayor_recaudacion
from depositos_mayor_50mil import depositos_mayor_50k
from informe_recaudacion import ordenar_por_insercion
from corregir import corregir_error

def main():

    inventario = [
        ["PBA", "autos", 0],
        ["PBA", "muñecas", 0],
        ["PBA", "trenes", 0],
        ["PBA", "peluches", 0],
        ["PBA", "spinners", 0],
        ["PBA", "cartas", 0],
        ["CABA", "autos", 0],
        ["CABA", "muñecas", 0],
        ["CABA", "trenes", 0],
        ["CABA", "peluches", 0],
        ["CABA", "spinners", 0],
        ["CABA", "cartas", 0],
        ["Chubut", "autos", 0],
        ["Chubut", "muñecas", 0],
        ["Chubut", "trenes", 0],
        ["Chubut", "peluches", 0],
        ["Chubut", "spinners", 0],
        ["Chubut", "cartas", 0],
        ["Tucumán", "autos", 0],
        ["Tucumán", "muñecas", 0],
        ["Tucumán", "trenes", 0],
        ["Tucumán", "peluches", 0],
        ["Tucumán", "spinners", 0],
        ["Tucumán", "cartas", 0],
        ["Mendoza", "autos", 0],
        ["Mendoza", "muñecas", 0],
        ["Mendoza", "trenes", 0],
        ["Mendoza", "peluches", 0],
        ["Mendoza", "spinners", 0],
        ["Mendoza", "cartas", 0]
    ]

    precios = {
        "autos": 10,
        "muñecas": 20,
        "trenes": 30,
        "peluches": 25,
        "spinners": 5,
        "cartas": 2
    }

    while True:
        print("\nMenú de opciones:")
        print("1. Cargar existencias")
        print("2. Calcular total de juguetes por depósito")
        print("3. Obtener juguetes a reponer")
        print("4. Máxima cantidad de juguetes por tipo")
        print("5. Depósito con mayor recaudación")
        print("6. Depósitos con más de 50,000 unidades")
        print("7. Porcentaje de juguetes por tipo")
        print("8. Informe de recaudación ordenada")
        print("9. Corregir errores en el inventario")
        print("0. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':

            for i in range(len(inventario)):
                provincia = inventario[i][0]
                tipo = inventario[i][1]
                cantidad = int(input(f"Ingrese la cantidad de {tipo} en {provincia}: "))
                inventario[i][2] = cantidad

        elif opcion == '2':
            print("Total de juguetes por provincia:", total_juguetes_por_provincia(inventario))

        elif opcion == '3':
            print("Depósito con mayor recaudación:", deposito_mayor_recaudacion(inventario, precios))

        elif opcion == '4':
            print("Provincias con más de 50k juguetes:", depositos_mayor_50k(inventario))

        elif opcion == '5':

            recaudacion = [0] * len(inventario)
            for i in range(len(inventario)):
                provincia = inventario[i][0]
                tipo = inventario[i][1]
                total_juguetes = inventario[i][2]
                recaudacion[i] = total_juguetes * precios[tipo]
            print("Recaudación ordenada:", ordenar_por_insercion(recaudacion))

        elif opcion == '9':
            inventario = corregir_error(inventario)
            print("Inventario corregido:", inventario)

        elif opcion == '0':
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()




