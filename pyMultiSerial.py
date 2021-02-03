
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

    def test(self):
        print ("Module imported!")
        t1 = threading.Timer(1,self.test)
        t1.daemon = True
        if(self.close==False):
            t1.start()
            
    def start(self):
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
        t1 = threading.Timer(1,self.test)
        t1.daemon = True
        t1.start()    
        pass
    
    
    
'''
Process:
    Define constructor
    Scan through all sinks
    Perform optional authentication
    Start a new thread if sink found / authtentication completed
    Post message as soon as found and report it to main thread or provide a hook to process serial port data
    Write on a serial port


'''   
    
