import serial
import json
import subprocess
ser = serial.Serial('/dev/ttyUSB0')  # open serial port
ser.baudrate = 9600

while(1):

    data = ser.read_until(b'}')     # reading
    
    data = data.decode("utf-8")
    print (data)

    array = json.loads(data)

    subprocess.run(["python3", "send_data.py",str(array['temperature']),str(array['pression']),str(array['humidite']),str(array['altitude']),str(array['feu'])]) 

ser.close()             # close port


