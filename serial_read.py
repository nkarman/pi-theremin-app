import serial
import struct
from pythonosc import udp_client

ser = serial.Serial('/dev/cu.usbserial')

client = udp_client.SimpleUDPClient('127.0.0.1', 6969)

while True:
    data = struct.unpack('f', ser.read(4))
    print(data[0])
    client.send_message('/theremin/midi', data[0])
