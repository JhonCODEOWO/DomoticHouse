# Instalar pip install adafruit-circuitpython-pca9685
import time
import board
import busio
from adafruit_pca9685 import PCA9685

# Configurar el bus I2C
i2c = busio.I2C(board.SCL, board.SDA)

# Inicializar el módulo  PCA9685
pca = PCA9685(i2c)
pca.frequency = 50 # Frecuencia del PWM en HZ

# Definir límites del movimiento del servo
SERVO_MIN_PULSE_WIDTH  =
SERVO_MIN_PULSE_WIDTH  =
SERVO_MIN_PULSE_WIDTH  =
SERVO_MIN_PULSE_WIDTH  =