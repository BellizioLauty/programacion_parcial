def calcular_totales(existencias):
    totales = [0] * 5  # Inicializar la lista de totales para 5 depósitos
    provincias = ["PBA", "CABA", "Chubut", "Tucumán", "Mendoza"]
    
    for juguete in existencias:
        for i in range(5):
            if juguete[0] == provincias[i]:
                totales[i] += juguete[2]  # Sumar la cantidad al total correspondiente

    return totales

def obtener_juguetes_a_reponer(existencias):
    juguetes_a_reponer = []  # Lista para almacenar juguetes a reponer
    provincias = ["PBA", "CABA", "Chubut", "Tucumán", "Mendoza"]
    
    for provincia in provincias:
        juguetes = []
        for juguete in existencias:
            if juguete[0] == provincia and juguete[2] < 500:
                juguetes.append(juguete[1])  # Agregar el tipo de juguete a reponer
        if juguetes:  # Solo agregar si hay juguetes a reponer
            juguetes_a_reponer.append((provincia, juguetes))
    
    return juguetes_a_reponer

def deposito_mayor_recaudacion(existencias, precios):
    recaudacion = [0] * 5  # Inicializar la lista de recaudación para 5 depósitos
    provincias = ["PBA", "CABA", "Chubut", "Tucumán", "Mendoza"]
    
    for juguete in existencias:
        for i in range(5):
            if juguete[0] == provincias[i]:
                tipo_index = ["autos", "muñecas", "trenes", "peluches", "spinners", "cartas"].index(juguete[1])
                recaudacion[i] += juguete[2] * precios[tipo_index]  # Calcular la recaudación

    max_recaudacion = max(recaudacion)
    indice_max = recaudacion.index(max_recaudacion)
    
    return provincias[indice_max], max_recaudacion

def cantidad_depositos_mayores(existencias):
    provincias = []
    totales = calcular_totales(existencias)

    for i in range(len(totales)):
        if totales[i] > 50000:
            provincias.append(f"Depósito {existencias[i * 6][0]}")  # Nombre de la provincia
    return provincias