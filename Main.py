import OperArchivos
import ConsultaWFC
from bs4 import BeautifulSoup
import requests

class API:
    #Clase 
    location = ""
    time = ""
    info = ""
    weather = ""
    def __init__(self, city):
        #Entrada city: string
        #Output (no variable): just printing output
        try:
            city = city.replace(" ", "+")
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
            res = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
            print("Searching...\n")
            soup = BeautifulSoup(res.text, 'html.parser')
            self.location = soup.select('#wob_loc')[0].getText().strip()
            self.time = soup.select('#wob_dts')[0].getText().strip()
            self.info = soup.select('#wob_dc')[0].getText().strip()
            self.weather = soup.select('#wob_tm')[0].getText().strip()
            print("Ubicación: ", self.location)
            print("Tiempo: ", self.time)
            print("Descripción: ", self.info)
            print("Temperatura: ", self.weather+"°C", "\n")
            location = self.location
            time = self.time
            info = self.info
            weather = self.info
            
        except:
            print("\nERROR\nHa ocurrido un error en la petición de datos sobre su ciudad...\nVuelva pronto!\n")

class Archivo:
    def __init__(self, city):
        nombre_archivo = city + ".txt"
        self.archivo = open(nombre_archivo, "w+")
    def escribir(self, location, time, info, weather):
        valores = [location, time, info, weather]
        for x in valores:
            self.archivo.write(x)
            self.archivo.write("\n")
        self.archivo.close()

#Programa principal
Corriendo = True
while (Corriendo):
    try:
        print("\n\nBienvenido a mi proyecto!")
        print("MENU PRINCIPAL----\n")
        print("Opción (1): Consulta de tiempo en una ciudad del mundo")
        print("Opción (2): Demostración del programa")
        print("Opción (3): Salir del programa\n")
        opcion = input("Introduzca su opción (1) o (2), escriba solo el numero: ")
        opcion = int(opcion)
        
        if (opcion == 1):
            valor = input("Introduzca el nombre de una ciudad: ")
            city = valor + " weather"
            resultados = API(city)
            File = Archivo(valor)
            File.escribir(resultados.location, resultados.time, resultados.info, resultados.weather)

        elif (opcion == 2):
            Diccionario = {"India":"Mumbai","Estados Unidos":"Miami","Ecuador":"Guayaquil","Estados Unidos":"New York","Costa Rica":"San Jose"}
            for key, value in Diccionario.items():
                values = value + " weather"
                resultados = API(values)
                File = Archivo(value)
                File.escribir(resultados.location, resultados.time, resultados.info, resultados.weather)
            print("Demostración finalizada!\n...\n...\n")

        elif (opcion == 3):
            Corriendo = False
            print("\nSaliendo del programa :(\n")

        else:
            print("Ha introducido una opción incorrecta!!\nIntroduzca una de las opciones '1' o '2'\n")
            
    except:
        print("Ha ocurrido un error procesando su petición.")
