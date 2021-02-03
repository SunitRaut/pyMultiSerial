
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
    

    
class MultiSerial():
    
    close = False
    ports = set()
    ser = [] 

    def test(self):
        print ("Module imported!")
        t1 = threading.Timer(1,self.test)
        t1.daemon = True
        if(self.close==False):
            t1.start()
            
    def autopilot(self):
        try: 
            while (1):
                '''Write your code from here'''
        
        
                '''Write your code till here'''
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
            #status.append(0);
            '''
            time.sleep(1.5)
            
            self.ser[temp_index].write(b"Hello\n")
            y = ser[temp_index].readline()
            print(y)
            if y==b"Hello\n":
                '''
                
            print('Found: '+portno)
            self.ports.add(portno)
            #t3=threading.Thread(target=read_sink,args=([ser[temp_index],portno]))
            #t3.daemon=True
            #t3.start()
            #else:
                #self.ser[temp_index].close()
                #self.ser.pop(temp_index)
        except IOError:
            pass
        
        except Exception as e:
            print(e)
            print('Not Found: '+portno)
        
    
'''
Process:
    [done] Define constructor
    Scan through all sinks
    Perform optional authentication
    Start a new thread if sink found / authtentication completed
    Post message as soon as found and report it to main thread or provide a hook to process serial port data
    Write on a serial port


'''   
    
