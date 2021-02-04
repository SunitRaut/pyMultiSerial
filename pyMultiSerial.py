
import serial
import threading
import time
'''
def test():
    print ("Module1 imported!")
        
def test2():
    while(1):
        time.sleep(1)
        print ("Module2 imported!")
     

def test1():
    print("Just to see if it works")
'''


    
def test_hook():
    print ("hook")
    pass
    
class MultiSerial():
    
    close = False
    ports = set()
    ser = [] 
    port_connection_found_callback = 0
    port_read_callback = 0
    port_disconnection_callback = 0

    def test(self):
        print ("Module imported!")
        t1 = threading.Timer(1,self.test)
        t1.daemon = True
        if(self.close==False):
            t1.start()
            
    def autopilot(self):
        try: 
            while (1):
                '''Task Schedular goes here'''

                '''   '''
                pass
    
    
        except Exception:
            pass

        finally:
    
            self.close = True
            pass
      
    
        
    def __init__(self):
        #t1 = threading.Timer(1,self.test)
        #t1.daemon = True
        #t1.start()   
        self.scan_ports()
        pass
    
    def scan_ports(self):
        if self.close:
            print("Stop scan_ports")
            return
        print("scan_ports")
        for i in range(15):
            t2 = threading.Thread(target=self.port_connect,args=([i]))
            t2.daemon = True
            t2.start()
            pass    
        t1=threading.Timer(1,self.scan_ports)
        t1.daemon=True
        t1.start()
        
    def port_connect(self,i):
        if self.close:
            return
        try:
            #portno='/dev/ttyACM'+str(i)
            portno='COM'+str(i)
            if portno in self.ports:
                return
            self.ser.append(serial.Serial(port=portno,baudrate = 9600))
            temp_index=len(self.ser)-1
            flag = True
            #Callback
            flag = self.port_found_callback(portno)
            #Callback
            #status.append(0);
            '''
            time.sleep(1.5)
            
            self.ser[temp_index].write(b"Hello\n")
            y = ser[temp_index].readline()
            print(y)
            if y==b"Hello\n":
                '''
            if flag==True:
                self.ports.add(portno)
                t3=threading.Thread(target=self.read_sink,args=([self.ser[temp_index],portno]))
                t3.daemon=True
                t3.start()
            else:
                self.ser[temp_index].close()
                self.ser.pop(temp_index)
        except IOError:
            pass
        
        except Exception as e:
            print(e)
            #print('Not Found: '+portno)
 
            
        
        def read_sink(self,i_serial,i_port):
            
            if self.close:
                return
            
            
            try: 
                if (i_serial.inWaiting()>0):
                    text = i_serial.readline().decode("utf=8")
                    self.port_read_callback(i_port,text)
                pass
            
            except serial.SerialException:
        
                #i_serial.close()
                if i_serial in self.ser:
                    self.port_disconnection_callback(i_port)
                    self.ser.remove(i_serial)
                    #print("Sink disconnected")
                    self.ports.discard(i_port)
            finally: 
                if self.close==False:
                    t = threading.Thread(target=read_sink,args=([i_serial,i_port]))
                    t.daemon = True
                    t.start()
        



    
'''
Process:
    [done] Define constructor
    Scan through all sinks
    Perform optional authentication
    Start a new thread if sink found / authtentication completed
    Post message as soon as found and report it to main thread or provide a hook to process serial port data
    Write on a serial port


'''   
    
