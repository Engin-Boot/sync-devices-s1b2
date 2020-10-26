import watchdog.events
import watchdog.observers
import time
import pathlib
import smtplib
import csv

# To run on local host port is set to 1025 and smtp_server to "localhost". To run local SMTP server use "python -m smtpd -c DebuggingServer -n localhost:1025" in command prompt
# login is not required while running with local SMTP server

#################################################################################
#Global Variables which are fixed

procedureDict={"cardiac": "Cardiac Cathether"}
InventoryPath="D:\a\sync-devices-s1b2\sync-devices-s1b2\InventoryManager\Inventory.csv"

#################################################################################
#SMTP details, using localhost here so login and email not required

port = 1025  # For SSL
smtp_server = "localhost"
sender_email = "my@gmail.com"  # Enter your address
receiver_email = "receiver@gmail.com"  # Enter receiver address
# password = input("Type your password and press enter: ")


#################################################################################

def sendmail(msg):
    with smtplib.SMTP(smtp_server, port) as server:
        server.sendmail(sender_email, receiver_email, msg)

def checkItemCountAndSendMail(count,procedure):
    if (count < 3):
        message = (str(procedure) + " supply is low, the present count is = " + str(count))
        print("mail message is", message)
        sendmail(message)
        print("mail sent")
        return 1
    return 0

#################################################################################

def import_csv(csvfilename):
    data = []
    with open(csvfilename, "r", encoding="utf-8", errors="ignore") as scraped:
        reader = csv.reader(scraped, delimiter=',')
        row_index = 0
        for row in reader:
            if row:  # avoid blank lines
                row_index += 1
                columns = row[3]
                print(columns)
                data.append(columns)
    print("last updated patient procedure",data[-1])
    return data[-1]
    
#################################################################################

def reduceCount(item):
    row_count = 0
    lines=[]
    with open(InventoryPath,"r") as scraped:
        reader=csv.reader(scraped, delimiter=',')
        lines=list(reader)
        for row in lines:
            if row[0] == item:
                print(row[0])
                break
            row_count =row_count+1

    count_value=int(lines[row_count][1])
    count_value=count_value-1
    lines[row_count][1]=str(count_value)
    writer = csv.writer(open(InventoryPath, "w",newline =''))
    writer.writerows(lines)
    checkItemCountAndSendMail(count_value,lines[row_count][0])

def checkInventoryFile(inventoryFilePath):
    inventoryFileCorrectFormat=['Item','Qty']
    if pathlib.Path(inventoryFilePath).is_file():
        with open(inventoryFilePath, "r", encoding="utf-8", errors="ignore") as scraped:
            reader = csv.reader(scraped, delimiter=',')
            first_row = next(reader)
            if (inventoryFileCorrectFormat==first_row):
                print("correct format for inventory file")
                return True
            else:
                print("Inventory file format incorrect, path is: ", inventoryFilePath)
                return False

    print("Inventory File Missing")
    return False

def checkProcedureAndOperate(procedure):
    if procedure in procedureDict:
        if checkInventoryFile(InventoryPath)==True:
            reduceCount(procedureDict[procedure])
            return 1
        else:
            return 0
    else:
        print("No such procedure in inventory record")
        return 0

#################################################################################

def checkPatientFileFormat(patientCSVpath):
    with open(patientCSVpath, "r", encoding="utf-8", errors="ignore") as scraped:
        reader = csv.reader(scraped, delimiter=',')
        first_row=next(reader)
        if(len(first_row)==5):
            print("correct patient file format")
            return True
        else:
            print("Patient file format incorrect, path is: ", patientCSVpath)
            return False

#################################################################################

class Handler(watchdog.events.PatternMatchingEventHandler):
    def __init__(self):
        watchdog.events.PatternMatchingEventHandler.__init__(self, patterns=['*.csv'],
                                                             ignore_directories=True, case_sensitive=False)

    def on_modified(self, event):
        patientCSVpath="D:\a\sync-devices-s1b2\sync-devices-s1b2\devices\patient-monitors\x64\debug\patientdetailsReport.csv"
        print("Watchdog received modified event - % s." % event.src_path)
        if(str(event.src_path)==patientCSVpath):
            print("right file modified")
            if(checkPatientFileFormat(patientCSVpath)==True):
                data = import_csv(patientCSVpath)
                checkProcedureAndOperate(data)
        else:
            print("some other file modified, waiting for patientfile to be modified")

#################################################################################

if __name__ == "__main__":
    #path to be observed
    src_path = "D:\a\sync-devices-s1b2\sync-devices-s1b2\devices\patient-monitors\x64\debug\"

    event_handler = Handler()
    observer = watchdog.observers.Observer()
    observer.schedule(event_handler, path=src_path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
