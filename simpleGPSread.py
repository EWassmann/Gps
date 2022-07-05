import serial
gps = serial.Serial(
port = '/dev/ttyACM0', baudrate = 9600)
x = gps.read(1000)
print(x)