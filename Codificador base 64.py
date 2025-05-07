# Nombre del proyecto: Codificador base 64
# Autor: Diego Ortiz Puerto
# Fecha de creación: 2025-07-04
# Objetivo: Codificar una cadena de texto en base 64
# Descripción: Este programa toma una cadena de texto como entrada y la codifica en base 64.


# importamos la librería base64
import base64
import os

# Definimos la función codificar_base64 que toma un texto como argumento y lo codifica en base 64
def codificar_base64(texto):
    texto_bytes = texto.encode('utf-8')
    texto_base64_bytes = base64.b64encode(texto_bytes)
    return texto_base64_bytes.decode('utf-8')

# Función principal
def main():
    try:
        salir = False
        while not salir:
            print("Bienvenido al codificador base64\n")

            carpeta = "Archivos a leer"
            
            if not os.path.exists(carpeta):
                os.makedirs(carpeta)
                ruta_absoluta = os.path.abspath(carpeta)
                print(f"Ruta donde se intentará crear la carpeta: {ruta_absoluta}")
                print(" Se ha creado la carpeta 'Archivos a leer'.\n")
            else:
                # Si la carpeta ya existe, mostramos su ruta
                ruta_absoluta = os.path.abspath(carpeta)
                print(f"Ruta de la carpeta 'Archivos a leer': {ruta_absoluta}\n")

            print("Por favor, recuerde ingresar los archivos .xml y .json en la carpeta 'Archivos a leer'.\n")

            archivos = os.listdir(carpeta)
            if not archivos:
                print("No hay archivos en la carpeta.\n")
                input("Presione Enter para continuar...")
                continue

            # Buscar el primer archivo con extensión .xml
            archivo_xml = next((f for f in archivos if f.lower().endswith(".xml")), None)
            #buscar el primer archivo con extensión .json
            archivo_json = next((f for f in archivos if f.lower().endswith(".json")), None)
            
            if archivo_xml is None:
                print(" No se encontró ningún archivo con extensión .xml.\n")
                input("Presione Enter para continuar...")
                continue
            if archivo_json is None:
                print(" No se encontró ningún archivo con extensión .json.\n")
                input("Presione Enter para continuar...")
                continue
            
            ruta_archivo = os.path.join(carpeta, archivo_xml)
            ruta_archivo_json = os.path.join(carpeta, archivo_json)
            
            
            try:
                with open(ruta_archivo, "r", encoding="utf-8") as archivo:
                    texto_xml = archivo.read()
                    print(f" Se ha leído el archivo XML '{archivo_xml}' correctamente.\n")
                # abrimos el archivo json
                with open(ruta_archivo_json, "r", encoding="utf-8") as archivo_json:
                    texto_json = archivo_json.read()
                    print(f" Se ha leído el archivo JSON '{archivo_json}' correctamente.\n")
            except Exception as e:
                print(f" Ocurrió un error al leer el archivo XML y json: {e}\n")
                input("Presione Enter para continuar...")
                continue

            print(" Contenido del archivo XML:\n")
            print(texto_xml)
            print("\n Contenido del archivo JSON:\n")
            print(texto_json)
            
            
            # Codificamos el contenido en base64
            texto_codificado = codificar_base64(texto_xml)
            print("\n Texto codificado en base64 del XML:\n")
            print(texto_codificado)
            
            # convinamos archivo json y xml en una sola cadena
            print("\n Combinando el contenido del archivo JSON y el XML codificado en base64:\n")
            
            texto_json_inicial= f'{{\n "codigoUnicoValidacion": "0",\n "rips":'
            #texto_combinado = texto_json + f",\n""xmlFevFile"":\n"+ texto_codificado 
            texto_combinado = texto_json_inicial+ texto_json + f',\n  "xmlFevFile": \n"{texto_codificado}"\n}}'
            print("\n Texto combinado:\n")
            print(texto_combinado)
            
            #Guardamos el archivo con el texto combinado en un json
            nombre_archivo = "archivo_combinado.json"
            ruta_guardar = os.path.join(carpeta, nombre_archivo)
            try:
                with open(ruta_guardar, "w", encoding="utf-8") as archivo_guardar:
                    archivo_guardar.write(texto_combinado)
                    print(f"\n Se ha guardado el archivo combinado como '{nombre_archivo}' en la carpeta 'Archivos a leer'.\n")
            except Exception as e:
                print(f" Ocurrió un error al guardar el archivo combinado: {e}\n")
            
            # Pregunta para salir
            respuesta = input("\n¿Desea salir del programa? (s/n): ").strip().lower()
            if respuesta == 's':
                salir = True
            elif respuesta != 'n':
                print("Respuesta no válida. Por favor, introduzca 's' o 'n'.\n")
    except Exception as e:
        print(f" Ocurrió un error inesperado: {e}\n")
        input("Presione Enter para continuar...")
        # Pregunta para salir
        respuesta = input("\n¿Desea salir del programa? (s/n): ").strip().lower()
        if respuesta == 's':
            salir = True
        elif respuesta != 'n':
            print("Respuesta no válida. Por favor, introduzca 's' o 'n'.\n")
        # Si se desea salir, terminamos el programa
        if salir:
            print("Saliendo del programa...")
            exit(0)
        else:
            main()

if __name__ == "__main__":
    main()