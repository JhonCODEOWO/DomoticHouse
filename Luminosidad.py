# Instalar pip instal RPi.GPIO
import RPi.GPIO as GPIO
import time

# Definimos el pin para recibir los datos
SENSOR_PIN = 18

# Método para leer la luminosidad
def read_luminusity():
    # Definimos el pin de información y si será de entrada o de salida
    GPIO.setup(SENSOR_PIN, GPIO.IN)

    # Leer el valor recibido por el pin
    luminosidad = GPIO.input(SENSOR_PIN)

    return luminosidad

try:
    #Almacenamos el dato recibido por la función
    luminosity = read_luminusity()
    
    # Imprimir la luminosidad
    print('Luminosidad actual: ' + luminosity)

    # Suspendemos el proceso un segundo hasta la siguiente lectura
    time.sleep(1)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
