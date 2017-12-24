import datetime
import platform
import struct
import numpy as np
import serial as sr
import serial.tools.list_ports
import sys

class Live():
    def __init__(self,save_data=False):
        # object initialization of serial
        self.a=""
        self.ser = sr.Serial(port=self.arduino_port(), baudrate=115200)
        #atexit.register(self.close_serial)
        ## Write to file.txt
        # toggle, saving to file, on or off
        self.fenable = save_data

        # initialize file I/O object
        if self.fenable:
            self.filename = "_".join(["data", datetime.datetime.now().strftime("%y%m%d_%H%M%S")])
            self.f = open(self.filename + ".txt", "a")
            # First line in file
            self.f.writelines("OpenBci data, columns: | Index # , 8 Channels |")


    #returns available serial port
    def arduino_port(self):
            if platform.system() == "Linux":
                port_identify = '/dev/ttyACM'
            else:
                if platform.system() == "Windows":
                    port_identify = 'COM'
                else:
                    port_identify = 'No device connected'

            ports = serial.tools.list_ports.comports()
            commPort = 'No device connected'
            numConnection = len(ports)

            for i in range(0, numConnection):
                port = ports[i]
                strPort = str(port)
                if port_identify in strPort:
                    splitPort = strPort.split("'")
                    commPort = (splitPort[1])

            return commPort

    '''
    # object initialization of serial
    ser = sr.Serial(port=arduino_port(), baudrate=115200)
    
    ## Write to file.txt
    # toggle, saving to file, on or off
    fenable = True
    
    # initialize file I/O object
    if fenable:
        filename = "_".join(["data", datetime.datetime.now().strftime("%y%m%d_%H%M%S")])
        f = open(filename + ".txt", "a")
        # First line in file
        f.writelines("OpenBci data, columns: | Index # , 8 Channels |")
    
    '''
    # iterable function to write row
    def save_to_file(self,line):
        if self.fenable:
            self.f.writelines("\n" + line)

    def decode_frame_analog(self):
        try:
            self.command(b'b')
            #data_f = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
            data_b = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
            head = self.ser.read()
            index_n = self.ser.read()
            for x in range(8):
                data_b[x] = int(self.ser.readline())
            tail = self.ser.read()
            # print(head, data_b, tail)
            if head == b'A' and tail == b'\xc0':
                indx = ord(index_n)
                channels = data_b[:] or [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
                # tailor = hex(ord(tail)) or 0

                # return header, indx, channels, tailor
                frame = str(indx) + ", " + str(channels[:])[1:len(str(channels)) - 1]
                self.save_to_file(frame)
                return channels[:]
            else:
                return [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        except TypeError or serial.serialutil.SerialException :
            print("Serial Error")
            self.a("Serial Error","Disconnected")
            exit(0)
    # return separate different parts of frame
    def decode_frame(self):
        self.command(b'b')
        data_f = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        head = self.ser.read()
        index_n = self.ser.read()
        data_b = self.ser.read(32)
        tail = self.ser.read()
        # print(head, data_b, tail)
        if head == b'A' and tail == b'\xc0':
            temp = 0

            for x in range(0, 32, 4):
                data_f[temp] = struct.unpack('f', data_b[x:(x + 4)])[0]
                temp += 1

            indx = ord(index_n)
            channels = data_f[:] or [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
            # tailor = hex(ord(tail)) or 0

            # return header, indx, channels, tailor
            frame = str(indx) + ", " + str(channels[:])[1:len(str(channels)) - 1]
            self.save_to_file(frame)
            return channels[:]


    # w8 for board to be ready to input commands and print whatever is coming
    def initialize(self):
        print("Connection established")
        s = ''
        while '$$$' not in s:
            s = s + self.ser.read().decode('utf-8', errors='replace')
        print(s)


    # send command stream command
    def command(self,c):
        #print(c)
        try:
            self.ser.write(c)
        except serial.serialutil.SerialException:
            #self.reconnect()
            pass
    def run(self,f):
        self.a=f
    def reconnect(self):
        try:
            self.ser = sr.Serial(port=self.arduino_port(), baudrate=115200)
            self.initialize()
        except serial.serialutil.SerialException:
            #self.a()
            pass
    # close connection
    def close_serial(self):
        self.command(b's')
        if self.fenable: self.f.close()
        self.ser.close()
        print("Ending connection")


'''
liv = Live(False)
liv.initialize()
for x in range(10):
    c = liv.decode_frame_analog()
    print(x, c)
liv.close_serial()'''

