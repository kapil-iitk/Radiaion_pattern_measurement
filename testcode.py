import serial
import time

def read_inst():
    time.sleep(2)
    line = My_ant_controller.readline()
    return line
    
def write_inst(Inst_Command,Response_Time):
    #time.sleep(2)
    My_ant_controller.write(Inst_Command)
    time.sleep(4.0*Response_Time/5)
    return_command2=read_inst()
    print return_command2
    
try:
    #try to open instrument, if failed, display the msg and exit
    My_ant_controller = serial.Serial('COM3', 19200, timeout=0)
except:
    print "___________________________________________"
    print ""
    print("Failed to open antenna positioner")
    print "Please connect the positiner to serial port"
    print "___________________________________________"
    My_ant_controller.close()
    exit()


return_command1=read_inst()
print return_command1

if return_command1=="Yes":
    print "Yessss"

#write_inst("Start",0)
#angle=5
#write_inst("Anticlockwise#"+str(angle)+"000.00$800",angle)
#angle=360
#write_inst("Anticlockwise#"+str(angle)+"000.00$800",angle)
My_ant_controller.close()
print "instrument Closed"