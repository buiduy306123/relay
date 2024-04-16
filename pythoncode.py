import serial
import time

# Tạo đối tượng Serial port với Arduino
arduino = serial.Serial('COM5', 9600) 
time.sleep(2) 

# Bật chân D2
arduino.write(b'e')
time.sleep(1) 

# Tắt chân D2
arduino.write(b'f')
time.sleep(1) 

# Bật chân D3
arduino.write(b'g')
time.sleep(1) 

# Tắt chân D3
arduino.write(b'h')
time.sleep(1) 

# Đóng kết nối
arduino.close()
