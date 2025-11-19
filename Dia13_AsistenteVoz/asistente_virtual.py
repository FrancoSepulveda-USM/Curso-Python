import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

# opciones de voz / idioma
id1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'
id2 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
id3 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0'
id4 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'


# Escucha el microfono y lo pasa a texto.
def transformar_audio():

    # Objeto recognizer que procesa el audio y lo pasa a texto.
    r = sr.Recognizer()

    # Configurar el microfono
    with sr.Microphone() as origen: # Abre el micro del PC

        # Tiempo de espera hasta que considere que se dejó de hablar.
        r.pause_threshold = 0.8

        # Informar que comenzo la grabacion
        print("ya puedes hablar")

        # Guarda lo que escuchó, escucha hasta que haya un silencio(threshold)
        audio = r.listen(origen)

        try:
            # Manda el audio a servidores de Google Speech Recognition para pasarlo a texto.
            pedido = r.recognize_google(audio, language="es-419")

            print("Dijiste: " + pedido)

            return pedido

        # No entendio lo que dije
        except sr.UnknownValueError:

            print("No entendi")

            return "sigo esperando"

        # Caso de no resolver el pedido (Problema servicio Google)
        except sr.RequestError:
            
            print("No hay servicio")

            return "sigo esperando"

        # Cualquier otro error
        except:

            print("Algo ha salido mal")

            return "sigo esperando"


# Asistente dice lo que aparece en mensaje.
def hablar(mensaje):

    engine = pyttsx3.init() # Enciende el motor de voz
    engine.setProperty('voice', id2)

    engine.say(mensaje) # Pasa al motor lo que debe decir
    engine.runAndWait() #Empieza a hablar, termine cuando diga todo el mensaje


def pedir_dia():

    dia = datetime.date.today()
    dia_semana = dia.weekday()
    print(dia_semana)

    calendario = {0: 'Lunes',
                    1: 'Martes',
                    2: 'Miércoles',
                    3: 'Jueves',
                    4: 'Viernes',
                    5: 'Sábado',
                    6: 'Domingo'}

    hablar(f'Hoy es {calendario[dia_semana]}')


def pedir_hora():

    hora = datetime.datetime.now()
    hora = f'En este momento son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos'
    print(hora)
    
    hablar(hora)


def saludo_inicial():

    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas noches'
    elif 6 <= hora.hour < 13:
        momento = 'Buen día'
    else:
        momento = 'Buenas tardes'

    hablar(f'{momento}, soy Helena, tu asistente personal. Por favor, dime en qué te puedo ayudar')


# Funcion central
def pedir_cosas():

    saludo_inicial()

    while True:

        # activar el micro y guardar el pedido en un string
        pedido = transformar_audio().lower()

        if 'abrir youtube' in pedido:
            hablar('Abriré youTube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir navegador' in pedido:
            hablar('Habriendo navegador Google')
            webbrowser.open('https://www.google.com')
            continue
        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'busca en wikipedia' in pedido:
            hablar('Buscando en wikipedia')
            pedido = pedido.replace('busca en wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar('Wikipedia dice lo siguiente:')
            hablar(resultado)
            continue
        elif 'busca en internet' in pedido:
            hablar('Buscando en internet')
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            hablar('Esto es lo que he encontrado')
            continue
        elif 'reproducir' in pedido:
            hablar('Buena idea, ya comienzo a reproducirlo')
            pywhatkit.playonyt(pedido)
            continue
        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {'apple':'APPL',
                    'amazon':'AMZN',
                    'google':'GOOGL'}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'La encontré, el precio de {accion} es {precio_actual}')
                continue
            except:
                hablar("Perdón pero no la he encontrado")
                continue
        elif 'adiós' in pedido:
            hablar("Hasta pronto")
            break


pedir_cosas()