'''
**********************************************************************************
 Author: Sunit Raut   github.com/SunitRaut
**********************************************************************************
 License
**********************************************************************************
 This program is free software; you can redistribute it 
 and/or modify it under the terms of the GNU General    
 Public License as published by the Free Software       
 Foundation; either version 3 of the License, or        
 (at your option) any later version.                    
                                                        
 This program is distributed in the hope that it will   
 be useful, but WITHOUT ANY WARRANTY; without even the  
 implied warranty of MERCHANTABILITY or FITNESS FOR A   
 PARTICULAR PURPOSE. See the GNU General Public        
 License for more details.                              
                                                        
 Licence can be viewed at                               
 http://www.gnu.org/licenses/gpl-3.0.txt
 Please maintain this license information along with authorship
 and copyright notices in any redistribution of this code
**********************************************************************************
'''

import serial
import threading



# Dummy functions for callbacks
def dummy_func():
    
    return True
    pass    

def dummy_func1(p1):
    
    return True
    pass    

def dummy_func2(p1,p2):
    
    return True
    pass    

def dummy_func3(p1,p2,p3):
    
    return True
    pass    

def dummy_func4(p1,p2,p3,p4):
    
    return True
    pass    

    
#MultiSerial Class
class MultiSerial():
    
    close = False
    ports = set()
    ser = [] 
    pause_ser = []
    baudrate = 9600
    timeout = 2
    portno_range = 29
    monitoring_freq = 0
    port_connection_found_callback = dummy_func3
    port_read_callback = dummy_func4
    port_disconnection_callback = dummy_func2
    interrupt_callback = dummy_func1
    loop_callback = dummy_func1

    def test(self):
        print ("Module imported!")
        t1 = threading.Timer(1,self.test)
        t1.daemon = True
        if(self.close==False):
            t1.start()
            
    def Start(self):
        try: 
            while (1):

                '''Schedule periodic tasks in loop_callback'''
                self.loop_callback()
                if self.close == True:
                    self.Stop()
                    exit
                pass                
    
        except:
            self.interrupt_callback()
            pass

        finally:
            self.Stop()
            pass

    def Stop(self):
        self.close = True
        self.ports.clear()
        for i_serial in self.ser:
            i_serial.close()
        for i_serial in self.pause_ser:
            i_serial.close()      
        
        
      
# Function to ignore future communication with port until the port is disconnected
    def ignore_port(self,i_serial):
        #i_serial.close()
        if i_serial in self.ser:
            self.ser.remove(i_serial)
        pass
    
# Function to pause the reading of a serial port 
    def pause_port(self,i_serial):
        if i_serial not in self.pause_ser:
            self.pause_ser.append(i_serial)
        pass

# Function to resume the reading of a serial port
    def resume_port(self,i_serial):
        if i_serial in self.pause_ser:
            self.pause_ser.remove(i_serial)
        pass

    
# Constructor        
    def __init__(self):
        self.scan_ports()
        pass

    
# Monitor port for incoming data
    def read_sink(self,i_serial,i_port):
        self.scan_ports()
        if self.close:
            return
        
        
        try: 
            if (i_serial.inWaiting()>0) and (i_serial in self.ser):
                if i_serial not in self.pause_ser:
                    text = i_serial.readline().decode("utf=8")
                    #Callback
                    self.pause_port(i_serial)
                    self.port_read_callback(i_port,i_serial,text)
                    self.resume_port(i_serial)
                    #Callback
            elif (i_serial not in self.ser):
                text = i_serial.inWaiting()
            if self.close==False:
                if i_serial in self.ser:
                    t = threading.Timer(self.monitoring_freq,self.read_sink,args=([i_serial,i_port]))
                    t.daemon = True
                    t.start()
                else:
                    t1 = threading.Timer(self.monitoring_freq,self.read_sink,args=([i_serial,i_port]))
                    t1.daemon = True
                    t1.start()    
        
        except serial.SerialException:
            #Callback
            self.port_disconnection_callback(i_port)
            #Callback
            i_serial.close()
            if i_serial in self.ser:
                self.ser.remove(i_serial)
            self.ports.discard(i_port)
                

	
# Scan for new connections        
    def scan_ports(self):
        if self.close:
            return
        #print("scan_ports")
        for i in range(self.portno_range+1):
	# Windows Ports
            t2 = threading.Thread(target=self.port_connect,args=([i,"COM"]))
            t2.daemon = True
            t2.start()
	# Linux/MAC USB ports
            t2 = threading.Thread(target=self.port_connect,args=([i,"/dev/ttyUSB"]))
            t2.daemon = True
            t2.start()
	# Linux/MAC ACM ports
            t2 = threading.Thread(target=self.port_connect,args=([i,"/dev/ttyACM"]))
            t2.daemon = True
            t2.start()
            pass    
        t1=threading.Timer(0.5,self.scan_ports)
        t1.daemon=True
        t1.start()
        
        
# Try connecting to a port        
    def port_connect(self,i,prefix):
        if self.close:
            return
        try:
            portno=prefix+str(i)
            if portno in self.ports:
                return
            self.ser.append(serial.Serial(port=portno,baudrate = self.baudrate, timeout=self.timeout))
            temp_index=len(self.ser)-1
            
            self.ports.add(portno)
            
            t3=threading.Thread(target=self.read_sink,args=([self.ser[temp_index],portno]))
            t3.daemon=True
            t3.start()
        
            #Callback
            self.pause_port(self.ser[temp_index])
            self.port_connection_found_callback(portno, self.ser[temp_index])
            if temp_index == len(self.ser)-1:
                self.resume_port(self.ser[temp_index])
            #Callback
                                    
        except IOError:
            pass
        
        except Exception as e:
            print(e)

 
