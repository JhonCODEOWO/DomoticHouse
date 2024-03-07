# Instalar pip install Adafruit_DHT
import Adafruit_DHT
import time

PIN_SENSOR = 17
DHT = Adafruit_DHT.DHT11(PIN_SENSOR)

try:
    while True:
        # Leemos el valor de la temperatura
        temperatura = DHT.temperature

        # Verificamos que la temperatura sea menor a cierto valor y realizamos una acción
        if temperatura > 25:
            print('Temperatura elevada')
        else:
            print('Temperatura normal')
        
        time.sleep(1)

except KeyboardInterrupt:
    pass