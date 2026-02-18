#MINI IA EN PYTHON QUE APRENDE A PREDECIR EL PRECIO DE UNA CASA

#DATOS DE ENTRENAMIENTO {TAMAÑO DE CASA VS PROYECTO}

tamanos = [50, 60, 80, 100, 120]
precios = [100000, 120000, 160000, 200000, 240000]

#Paso 1: CALCULAR PROMEDIOS 

prom_tamanos = sum(tamanos) / len(tamanos)
prom_precios = sum(precios) / len(precios)

#Paso 2: CALCULAR LA PENDIENTE (m)
numerador = sum((t - prom_tamanos) * (p - prom_precios) for t, p in zip(tamanos, precios))
denominador = sum((t - prom_tamanos) ** 2 for t in tamanos)

m = numerador / denominador

#Paso 3: CALCULAR LA INTERSECCIÓN (b)
b = prom_precios - m * prom_tamanos

#Paso 4: PREDECIR EL PRECIO DE UNA CASA NUEVA
while True:
    entrada = input("\nIngresa el tamaño de la casa (o escribe salir): ")

    if entrada.lower() == "salir":
        print("Programa terminado.")
        break

    tamano_usuario = float(entrada)
    prediccion = m * tamano_usuario + b

    print(f"Precio estimado por la IA: ${prediccion:,.2f}")
