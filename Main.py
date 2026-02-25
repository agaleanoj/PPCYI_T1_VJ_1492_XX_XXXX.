import xml.etree.ElementTree as ET


# =========================
# Clase Vuelo
# =========================
class Vuelo:
    def __init__(self, codigo, origen, destino, duracion, aerolinea):
        self.codigo = codigo
        self.origen = origen
        self.destino = destino
        self.duracion = int(duracion)
        self.aerolinea = aerolinea

    def mostrar_detalle(self):
        print("Código:", self.codigo)
        print("Origen:", self.origen)
        print("Destino:", self.destino)
        print("Duración:", self.duracion, "horas")
        print("Aerolínea:", self.aerolinea)


# =========================
# Diccionario global
# =========================
vuelos = {}


# =========================
# 1. Cargar archivo XML
# =========================
def cargar_archivo():
    ruta = input("Ingrese la ruta del archivo XML: ")

    try:
        tree = ET.parse(ruta)
        root = tree.getroot()

        for vuelo_xml in root.findall("vuelo"):

            codigo = vuelo_xml.find("codigo").text
            origen = vuelo_xml.find("origen").text
            destino = vuelo_xml.find("destino").text
            duracion = vuelo_xml.find("duracion").text
            aerolinea = vuelo_xml.find("aerolinea").text

            if codigo in vuelos:
                print("⚠ Código repetido:", codigo)
            else:
                nuevo_vuelo = Vuelo(codigo, origen, destino, duracion, aerolinea)
                vuelos[codigo] = nuevo_vuelo

        print("Archivo cargado correctamente.")

    except Exception as e:
        print("Error al leer el archivo:", e)


# =========================
# 2. Detalle vuelo específico
# =========================
def detalle_vuelo():
    codigo = input("Ingrese el código del vuelo: ")

    if codigo in vuelos:
        vuelos[codigo].mostrar_detalle()
    else:
        print("Vuelo no encontrado.")


# =========================
# 3. Agrupar por aerolínea
# =========================
def agrupar_por_aerolinea():
    agrupados = {}

    for vuelo in vuelos.values():
        if vuelo.aerolinea not in agrupados:
            agrupados[vuelo.aerolinea] = []

        agrupados[vuelo.aerolinea].append(vuelo.codigo)

    for aerolinea, lista_codigos in agrupados.items():
        print("\nAerolínea:", aerolinea)
        for codigo in lista_codigos:
            print("  -", codigo)


# =========================
# 4. Ordenar por duración
# =========================
def ordenar_por_duracion():
    lista_ordenada = sorted(vuelos.values(), key=lambda v: v.duracion, reverse=True)

    print("\nVuelos ordenados de mayor a menor duración:")
    for vuelo in lista_ordenada:
        print(vuelo.codigo, "-", vuelo.duracion, "horas")


# =========================
# Menú principal
# =========================
def menu():
    while True:
        print("\n===== MENÚ =====")
        print("1. Cargar Archivo")
        print("2. Detalle de vuelo específico")
        print("3. Agrupar vuelos por aerolínea")
        print("4. Ordenar por duración")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cargar_archivo()
        elif opcion == "2":
            detalle_vuelo()
        elif opcion == "3":
            agrupar_por_aerolinea()
        elif opcion == "4":
            ordenar_por_duracion()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.")


# Ejecutar programa
menu()