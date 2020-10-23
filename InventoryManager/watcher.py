import watchdog.events
import watchdog.observers
import time
import pathlib
import smtplib
import csv

# To run on local host port is set to 1025 and smtp_server to "localhost". To run local SMTP server use "python -m smtpd -c DebuggingServer -n localhost:1025" in command prompt
# login is not required while running with local SMTP server
procedureDict={"cardiac": "Cardiac Cathether"}

port = 1025  # For SSL
smtp_server = "localhost"
sender_email = "my@gmail.com"  # Enter your address
receiver_email = "receiver@gmail.com"  # Enter receiver address
# password = input("Type your password and press enter: ")

def sendmail(msg):
    with smtplib.SMTP(smtp_server, port) as server:
        server.sendmail(sender_email, receiver_email, msg)

def checkItemCountAndSendMail(count,procedure):
    if (count < 3):
        message = (str(procedure) + " supply is low, the present count is = " + str(count))
        print(message)
        sendmail(message)
        print("mail sent")

def import_csv(csvfilename):
    data = []
    with open(csvfilename, "r", encoding="utf-8", errors="ignore") as scraped:
        reader = csv.reader(scraped, delimiter=',')
        row_index = 0
        for row in reader:
            if row:  # avoid blank lines
                row_index += 1
                columns = row[3]
                data.append(columns)
    print(data)
    print(data[-1])
    return data

def reduceCount(item):
    row_count = 0
    lines=[]
    with open("D:\a\sync-devices-s1b2\sync-devices-s1b2\InventoryManager\Inventory.csv","r") as scraped:
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
    writer = csv.writer(open("D:\a\sync-devices-s1b2\sync-devices-s1b2\InventoryManager\Inventory.csv", "w",newline =''))
    writer.writerows(lines)
    checkItemCountAndSendMail(count_value,lines[row_count][0])

def checkProcedureAndOperate(procedure):
    if procedure in procedureDict:
        reduceCount(procedureDict[procedure])
    else:
        print("No such procedure in inventory record")


class Handler(watchdog.events.PatternMatchingEventHandler):
    def __init__(self):
        watchdog.events.PatternMatchingEventHandler.__init__(self, patterns=['*.csv'],
                                                             ignore_directories=True, case_sensitive=False)

    def on_modified(self, event):
        print("Watchdog received m/odified event - % s." % event.src_path)
        data = import_csv("D:\a\sync-devices-s1b2\sync-devices-s1b2\devices\patient-monitors\x64\debug\patientdetailsReport.csv")
        procedure = data[-1]
        checkProcedureAndOperate(procedure)

if __name__ == "__main__":
    src_path = "D:\a\sync-devices-s1b2\sync-devices-s1b2\devices\patient-monitors\x64\debug"
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