import paho.mqtt.client as mqtt #import the client1
import time
import sys
import threading

def takePatientInput():
    patientName=input("Enter Patient Name")
    patientAge=input("Enter Patient Age")
    patientGender=input("Enter Patient Gender M/F")
    patientProcedure=input("Enter name of Procedure")
    patientData=str(patientName)+";"+str(patientAge)+";"+str(patientGender)+";"+str(patientProcedure)
    print(patientData.replace(";"," "))
    if(input("Check if details entered are correct yes/no")=="yes"):
        return patientData


############
def on_message(client, userdata, message):
    print(str(message.payload.decode("utf-8")))
########################################
def subscriber():
    broker_address="127.0.0.1"
    #broker_address="mqtt.eclipse.org"
    #print("creating new instance")
    client = mqtt.Client("P1") #create new instance
    #client = mqtt.Client()  # create new instance
    client.on_message=on_message #attach function to callback
    #print("connecting to broker")
    client.connect(broker_address) #connect to broker
    #print("Subscribing to topic","my_topic")
    client.subscribe("my_topic")
    client.loop_forever()
    
###########################################
def publisher():
    broker_address="127.0.0.1"
    #broker_address="mqtt.eclipse.org"
    #print("creating new instance")
    client = mqtt.Client("P2") #create new instance
    client.on_message=on_message #attach function to callback
    #print("connecting to broker")
    client.connect(broker_address) #connect to broker
    message=takePatientInput()
    print("Publishing message to topic","my_topic")
    client.publish("my_topic",message)
    client.loop_forever()

###########################################    
if __name__=="__main__":
    # creating thread
    t1 = threading.Thread(target=subscriber)
    t2 = threading.Thread(target=publisher)
    # starting thread 1
    t1.start()
    # starting thread 2

    # wait until thread 1 is completely executed
    #t1.join()
    # wait until thread 2 is completely executed
    #t2.join()
    try:
        num=input("welcome!!! enter 1 if you want to enter your details else do nothing\n")
        if(int(num)==1):
            print("NOW publish")
            t2.start()

    except KeyboardInterrupt:
        sys.exit()
