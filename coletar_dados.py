import serial
import time



ser = serial.Serial('COM8', 9600)

# Espera que a porta esteja aberta
time.sleep(2)

# Solicita dados do Arduino
ser.write(b'S')

# Passa os dados para um fichiero de texto
with open('dados_1.txt', 'w') as file:
    start_time = time.time()
    while time.time() - start_time < 3.3*60:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            file.write(line + '\n')
            print(line)  

ser.close()



