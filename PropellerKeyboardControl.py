import keyboard
import serial
import sys
from time import sleep
import serial.tools.list_ports

baud = 115200 #Serial baudrate for the board
timeout = 0.1 #Serial timeout for the board

#Finds existing serial connections and displays information about them
comlist = serial.tools.list_ports.comports()
portList = []
portDescs = []
portHWIDs = []

for element in comlist:
    portList.append(element.name)
    portDescs.append(element.description)
    portHWIDs.append(element.hwid)

#Checks if there are no serial conenctions and exits if there aren't any
if (len(portList) == 0):
    print("No existing serial connections")
    sys.exit()

#Neatly prints out list of serial ports
print("\n\n--------------------CONNECTIONS--------------------")
i = 1
for port in portList:
    print("({}) {}: {} [{}]".format(str(i),portList[i-1], portDescs[i-1], portHWIDs[i-1]))
    i += 1

#Manages selecting a serial connection
def chooseConnection():
    global p
    p = input("\nSelect a serial connection: ")
    try:
        global comport
        if (int(p) == 0):
            p = "1"
        comport = portList[abs(int(p))-1]
    except:
        print("Must be a whole number and correspond to a listed serial connection")
        sleep(0.5)
        chooseConnection()

chooseConnection()

print("Selected port: {}: {}\n".format(comport, portDescs[int(p)-1]))

sleep(0.5);

#Establishes a connection to the board
print("Establishing connection to {}...".format(comport))
sleep(1);
try:
    connection = serial.Serial(port=comport, baudrate=baud, timeout=timeout)
except:
    print("Could not connect to {}".format(comport))
    sleep(0.5)
    sys.exit()
print("Connection established")

print("\nUse the arrow keys or W,A,S,D")
print("Press \'q\' to quit and press \'p\' to ping board")
sleep(0.5)

#Sends keyboard data to the board
while True:
    incoming = connection.read_until()
    if (incoming):
        print(incoming.decode('utf-8'))

    if (keyboard.is_pressed('q')):
        print("Exiting...")
        try:
            connection.close()
        except:
            continue
        sleep(0.5)
        sys.exit()
    elif ((keyboard.is_pressed('w') and keyboard.is_pressed('a')) or (keyboard.is_pressed('up') and keyboard.is_pressed('left'))):
        connection.write(bytes('d', 'utf-8'))
    elif ((keyboard.is_pressed('w') and keyboard.is_pressed('d')) or (keyboard.is_pressed('up') and keyboard.is_pressed('right'))):
        connection.write(bytes('a', 'utf-8'))
    elif ((keyboard.is_pressed('s') and keyboard.is_pressed('a')) or (keyboard.is_pressed('down') and keyboard.is_pressed('left'))):
        connection.write(bytes('c', 'utf-8'))
    elif ((keyboard.is_pressed('s') and keyboard.is_pressed('d')) or (keyboard.is_pressed('down') and keyboard.is_pressed('right'))):
        connection.write(bytes('b', 'utf-8'))
    elif (keyboard.is_pressed('w') or keyboard.is_pressed('up')):
        connection.write(bytes('n', 'utf-8'))
    elif (keyboard.is_pressed('a') or keyboard.is_pressed('left')):
        connection.write(bytes('w', 'utf-8'))
    elif (keyboard.is_pressed('s') or keyboard.is_pressed('down')):
        connection.write(bytes('s', 'utf-8'))
    elif (keyboard.is_pressed('d') or keyboard.is_pressed('right')):
        connection.write(bytes('e', 'utf-8'))
    elif (keyboard.is_pressed('p')):
        connection.write(bytes('p', 'utf-8'))

    sleep(0.02)
