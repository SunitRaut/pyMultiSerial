
import pyMultiSerial as p

# Create object of class pyMultiSerial
gateway = p.MultiSerial()  
#Set gateway on autopilot mode (Optional). 
#In this mode, the gateway runs on its own and handles the complete execution flow of program. 
#In this mode, you can't add your own code. You can register callbacks.
gateway.autopilot()


