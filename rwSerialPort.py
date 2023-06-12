import serial
import struct 


port = '/dev/ttyUSB0'                                   # Porta serial utilizada
baud_rate = 9600                                        # Taxa de baudrate
ser = serial.Serial(port, baud_rate)                    # Conexão serial  


while True:
    # Ler o valor hexa da porta serial:
    ser.reset_input_buffer()
    hex_value = ser.readline()
    #print(hex_value)

    
    # Converter para decimal:
    decimal_value = int.from_bytes(hex_value[0:-1],"big")
    temp = (decimal_value & 0xFFFF0000) >> 16
    hum = decimal_value & 0x0FFFF
    #print("hex_value: ", hex(temp))
    #print("decimal value: ",temp)

    # Calcular o valor em graus celsius: 
    temp = -45 + (175*(temp/65535))
    hum = -6 + (125*(hum/65535))
    temp = round(temp,2)
    hum = round(hum,2)
    
    # Imprimir o valor da temperatura:
    print("Temperatura:",temp,"ºC")
    print("Humidade:",hum,"%")
    print("\n")
