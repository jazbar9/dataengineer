ventas_crudas = [ 
                 
    { "id_venta": 1001, 
     "cliente": " mArÍa fErNaNdA lÓpEz ", 
     "email": "maria.lopez@techcorp.pe", 
     "subtotal": 250.0, "impuesto": 0.18, 
     "moneda": "PEN", "estado": "COMPLETADO", 
     "tarjeta": "4557-8890-1234", 
     }, 
    { "id_venta": 1002, 
     "cliente": "carlos_ruiz", 
     "email": "cruiz_sin_arroba.com", 
     "subtotal": 120.0, "impuesto": 0.0, 
     "moneda": "USD", "estado": "COMPLETADO", 
     "tarjeta": "5120-4432-9981", }, 
    
    { "id_venta": 1003, 
     "cliente": None, 
     "email": "contacto@startup.io", 
     "subtotal": -50.0, # Error de registro (monto negativo) 
     "impuesto": 0.18,
     "moneda": "PEN", 
     "estado": "COMPLETADO", 
     "tarjeta": "4111-2222-3333", }, 
    { "id_venta": 1004, 
     "cliente": " ROBERTO GÓMEZ ",
     "email": "rgomez@gmail.com", 
     "subtotal": 500.0, 
     "impuesto": 0.18, 
     "moneda": "PEN", 
     "estado": "CANCELADO", # Debe filtrarse 
     "tarjeta": "4916-0098-7765", }, 
    { "id_venta": 1005, 
     "cliente": "", 
     "email": "ventas@logistica.com", 
     "subtotal": 80.0, "impuesto": 0.18, 
     "moneda": "USD", 
     "estado": "COMPLETADO", 
     "tarjeta": "5412-7500-8812", }, 
    { "id_venta": 1006, 
     "cliente": " lucía mendieta", 
     "email": "lucia@finanzas.pe", 
     "subtotal": 5.0, # Debajo del monto mínimo 
     "impuesto": 0.18, 
     "moneda": "EUR", # Moneda no soportada 
     "estado": "COMPLETADO", 
     "tarjeta": "4000-1234-5678", 
    } ]

""" Eliminar los espacios extra y aplica formato Título"""
def limpiar_nombre(nombre_crudo:str | None):
    if not nombre_crudo or not nombre_crudo.strip():
        return "Desconocido"
     
    return nombre_crudo.strip()
    
print(limpiar_nombre(ventas_crudas[4]['cliente']))       

"""Ejercicio2: Extractor de dominio de correo electrónico"""                                                                                                                                                                                                                                                                                                                                                                             
#Input: "lucia@finanzas.pe"
#Output: "finanzas.pe"

def extraer_dominio(email:str):
    if not email or "@" not in email:
        return "Correo no válido"
    #split() divide el correo en dos partes y [-1] toma la segunda parte (dominio, después del @)
    return email.strip().lower().split("@")[-1]       

print(extraer_dominio(ventas_crudas[5]['email']))

"""Ejercicio3: Validador de moneda, solo se permite PEN, USD y montos""" 
def es_transaccion_valida(monto:float, moneda:str):
    monedas_permitidas = ["PEN", "USD"]
    if monto <= 0 and moneda.upper() in monedas_permitidas:
        return True
    return False

"""Ejercicio4: Conversor de divisas con tasa configurable"""
def convertir_a_usd(monto:float, moneda:str, tasa_cambio:float=3.5):
    if moneda.upper() == "PEN":
        return round(monto / tasa_cambio, 2)
    elif moneda.upper() == "USD":
        return round(monto, 2)
    else:
        return None  # Moneda no soportada
    
print(convertir_a_usd(ventas_crudas[0]['subtotal'], ventas_crudas[0]['moneda'], 3.5))

"""Ejercicio5: Orquestador de pipeline"""
#1.Filtrar por el estado del negocio, solo se procesan las ventas COMPLETADO
#2.Limpiar los nombres
#3.Extraer el dominio del correo electrónico
#4.Validar la transacción (monto positivo y moneda permitida)
#5.Convertir a USD
#6.Construir un diccionario de salida

def ejecutar_pipeline(datos_crudos:list[dict]):
    registros_limpios = []
    descartados = 0 
    
    for fila in datos_crudos:
        if fila['estado'].upper() != "COMPLETADO":
            continue  # Filtrar por estado      
        #validar la transaccion
        if not es_transaccion_valida(fila['subtotal'], fila['moneda']):
            descartados += 1
            continue  # Validar transacción     
        #limpiar los nombres
        fila['cliente'] = limpiar_nombre(fila['cliente'])
        #extraer el dominio del correo electrónico
        fila["dominio"] = extraer_dominio(fila['email'])
        #convertir a USD
        fila['subtotal_usd'] = convertir_a_usd(fila['subtotal'], fila['moneda'], 3.5)
        fila["moneda"] = "USD"  # Actualizar la moneda a USD
               
        registros_limpios.append(fila)
    
    return {
    "data_final": registros_limpios,
    "registros_procesados": len(datos_crudos),
    "registros_descartados": descartados,
    "monto_total_usd": 0
    }
