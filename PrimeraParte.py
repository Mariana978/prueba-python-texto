
print("\n" + "Prueba técnica: Python + GitHub -  Mariana ÁIvarez CarvajaI")
def procesar_texto(texto):
    # Muestro primero el texto que voy a analizar para tenerlo a la vista
    
    print("\n" + "-------------------------------------------------" + "\n")
    print("Texto a analizar:\n")
    print(texto)
    print("\n" + "-------------------------------------------------" + "\n")


    # Limpio el texto: si el caracter es un signo de puntuación lo cambio por espacio,
    # si no, lo paso a minúscula y lo voy guardando en texto_limpio
    # Defino los signos de puntuación que quiero eliminar o reemplazar por espacios
    signos = '.,;:¡!¿?"\'()[]{}'
    texto_limpio = ""
    for caracter in texto:
        if caracter in signos:
            texto_limpio = texto_limpio+" "
        else:
            texto_limpio = texto_limpio+caracter.lower()

    # Ahora separo las palabras manualmente, armando palabra por palabra 
    palabras = []
    palabra_actual = ""
    for caracter in texto_limpio:
        if caracter == " ":# Si encuentro un espacio, significa que terminó una palabra
            if palabra_actual != "":
                palabras.append(palabra_actual)# Agrego la palabra a la lista
                palabra_actual = ""# Reinicio la variable para empezar a armar la siguiente palabr
        else:
            palabra_actual += caracter# Si no es un espacio, sigo construyendo la palabra con ese carácter
            
    # Me aseguro de que si hay una palabra pendiente al final, también se guarde
    if palabra_actual != "":
        palabras.append(palabra_actual)

    
    total = len(palabras)
    # set para c0njunt0s -> 0 sea, sin eIement0s repetid0s
    #Y Iist para meter t0d0 es0 en un s0I0 Iad0
    unicas = list(set(palabras))
    
    larga = ""  # Comienzo con una cadena vacía para haIIar Ia más Iarga
    for palabra in palabras:
        if len(palabra) > len(larga):
            larga = palabra  # Verific0 paIabra p0r paIabra


    conteo = {}#dicci0nari0
    for palabra in palabras:
        if palabra in conteo:# Si la palabra ya está en el diccionario, simplemente aumento su contador
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1# Si es la primera vez que aparece, la agrego al diccionario con valor 1

    # Creo un diccionario con todos los resultados que quiero mostraar!!
    resultados = {
        'total': total,
        'unicas': unicas,
        'larga': larga,
        'conteo': conteo
    }

    # Ahora imprimo todo el diccionario pero bien organizado y con saltos de línea para que se entienda mejor para eI usuari0
    print("Resultados: \n")
    print(f"total de palabras: {resultados['total']}")
    print("palabras únicas (sin repetir): [")
    for palabra in resultados['unicas']:
        print(f"   {palabra},")
    print("]")
    print(f"palabra más larga: '{resultados['larga']}'")
    print("Número de veces que aparece cada palabra (ignora mayúsculas/minúsculas y signos de puntuación): {")
    for palabra, cantidad in resultados['conteo'].items():
        print(f"   {palabra}: {cantidad},")
    print("  }\n}")



#--------------------PRUEBAS-------------------------

# --------------------- TEST 1 -------------------------
test1 = "En alianza con UNICEF Colombia, Confa, Fundación Luker y Fundación CUCÚ, nació Aventura en el Manglar, un juego educativo diseñado para ayudar a los niños y niñas entre 5 y 10 años a desarrollar habilidades básicas de lectura y escritura, a través de un formato lúdico y dinámico. Con tres niveles adaptados a distintas etapas del aprendizaje, el juego hace que practicar estas habilidades sea divertido y accesible. Está diseñado para que los niños y niñas jueguen con sus madres, padres o cuidadores en sus casas. Fundacion AAQ"
print(procesar_texto(test1))

# --------------------- TEST 2 -------------------------
test2 = "Desarrollado por Excello Association, Kalulu es un programa de enseñanza con un enfoque 100% fonético, respaldado por investigaciones educativas, neurocientíficas y cognitivas como la forma más efectiva de aprender a leer. En alianza con Excello, implementamos este programa ajustando el contenido de los materiales a las necesidades educativas de Colombia de forma directa y oportuna.Fundacion AAQ"
print(procesar_texto(test2))


