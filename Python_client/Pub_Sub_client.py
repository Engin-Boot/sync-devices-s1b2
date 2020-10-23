import paho.mqtt.client as mqtt #import the client1
import time
import sys
import threading

def takePatientInput():
    patientName=input("Enter Patient Name: ")
    patientAge=input("Enter Patient Age: ")
    patientGender=input("Enter Patient Gender, M for Male, F for Female: ")
    patientProcedure=input("Enter name of Procedure: ")
    patientData=str(patientName)+";"+str(patientAge)+";"+str(patientGender)+";"+str(patientProcedure)
    print(patientData.replace(";"," "))
    if(input("Check if details entered are correct yes/no\n")=="yes"):
        return patientData
    else:
        takePatientInput()


########################################
    
def on_message(client, userdata, message):
    print(str(message.payload.decode("utf-8")))
    
########################################
    
def on_disconnect(client, userdata,rc=0):
    logging.debug("DisConnected result code "+str(rc))
    client.loop_stop()
    
########################################
    
def subscriber():
    broker_address="127.0.0.1"
    #broker_address="mqtt.eclipse.org"
    client = mqtt.Client("P1") #create new instance
    client.on_message=on_message #attach function to callback
    client.connect(broker_address) #connect to broker
    client.loop_start()
    client.on_disconnect=on_disconnect
    client.subscribe("my_topic")
    
###########################################
def publisher():
    broker_address="127.0.0.1"
    #broker_address="mqtt.eclipse.org"
    client = mqtt.Client("P2") #create new instance
    client.on_message=on_message #attach function to callback
    client.connect(broker_address) #connect to broker
    message=takePatientInput()
    print("Publishing message to topic","my_topic")
    client.publish("my_topic",message)
    sys.exit()

###########################################    
if __name__=="__main__":
    try:
        # creating thread
        t1 = threading.Thread(target=subscriber)
        t2 = threading.Thread(target=publisher)
        # starting thread 1
        t1.start()
        num=input("welcome!!! enter 1 if you want to enter your details else do nothing\n")
        if(int(num)==1):
            t2.start()
            t2.join()
    except KeyboardInterrupt:
        t1.join()
        sys.exit()
