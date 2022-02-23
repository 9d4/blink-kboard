#!/usr/bin/python3
from pynput import keyboard
import sys
import glob
import serial
import asyncio

RELEASED = "\0"
PRESSED = "\1"

ports = []


def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


async def send_to_serial(bytesin):
    for port in ports:
        try:
            arduino = serial.Serial(port=port, baudrate=115200, timeout=.1)
            arduino.write(bytes(bytesin, "utf-8"))
        except serial.SerialException:
            pass


def on_press(key):
    # send_to_serial(PRESSED)
    asyncio.run(send_to_serial(PRESSED))


def on_release(key):
    # send_to_serial(RELEASED)
    asyncio.run(send_to_serial(RELEASED))


# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    ports = serial_ports()
    print(ports)
    print("Listening...")
    listener.join()
