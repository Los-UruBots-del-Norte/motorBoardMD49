from time import sleep
from motorBoardMD49 import MotorBoardMD49

PORT = "/dev/ttyUSB0"  # Cambia esto a tu puerto serial, como "COM3" en Windows
motor_board = MotorBoardMD49(port=PORT)

try:
    if motor_board.SetMode(0):
        print("Modo configurado a 0 (unsigned).")

    speed1 = motor_board.GetSpeed1()
    if speed1 is not None:
        print(f"Velocidad del motor 1: {speed1}")
    else:
        print("No se pudo leer la velocidad del motor 1.")

    speed2 = motor_board.GetSpeed2()
    if speed2 is not None:
        print(f"Velocidad del motor 2: {speed2}")
    else:
        print("No se pudo leer la velocidad del motor 2.")

    encoders = motor_board.GetEncoders()
    if encoders is not None:
        print(f"Encoders: Motor 1 = {encoders[0]}, Motor 2 = {encoders[1]}")
    else:
        print("No se pudieron leer los encoders.")

    volts = motor_board.GetVolts()
    if volts is not None:
        print(f"Voltaje de la placa: {volts / 10:.1f} V")
    else:
        print("No se pudo leer el voltaje.")

    # Establecer una velocidad para el motor 1 (por ejemplo, 128 en modo unsigned)
    if motor_board.SetSpeed1(128):
        print("Velocidad del motor 1 establecida a 128.")
    else:
        print("No se pudo establecer la velocidad del motor 1.")
        
    # Establecer una velocidad para el motor 2 llamado a la función set_speed_2_turn
    if motor_board.set_speed_2_turn(128):
        print("Velocidad del motor 2 establecida a 128.")
    else:
        print("No se pudo establecer la velocidad del motor 2.")

    sleep(2)

except Exception as e:
    print(f"Ocurrió un error: {e}")

finally:
    motor_board.Close()
    print("Conexión cerrada.")