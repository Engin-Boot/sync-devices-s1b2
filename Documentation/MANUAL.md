# Application Utility in Real World

The application can be used by a medical team of nurses, attendants and doctors to synchronize patient information among various devices. This would help them as they can enter patient details in one device and all the other devices will get those details synchronized and updated. These devices might even be various 3rd party vendors. The medical team does not need to have any technical knowledge of the operation that is being performed in background. This would help them to maintain synchronized patient records across all their systems.

# Dependencies Requirement

In order to run the Python client device on your local system use the below command on command prompt:

	pip install paho-mqtt

# Steps to check the demo by running few client devices and synchronizing information across them

- Go to devices/'device-name' folder to open the respective C++ device clients. We have implemented 3 C++ clients, namely:

	1. patient-monitor
	2. ultra-sound
	3. x-ray

- Using Visual Studio open the respective device .vcxproj project files and build it using x64 platform.
- Or use the below command to build, after replacing 'path' with the respective path to the project file and 'device-name' with the respective device name: 

		msbuild 'path'/'device-name'.vcxproj /p:configuration=debug /p:platform=x64

- Run the .exe generated after the build and communicate between the clients as required to synchronize patient information.

- Open command prompt and type:
	
		python Python_client/Pub_Sub_client.py

This runs the Python client device. Now you can communicate with the rest of the C++ devices in a similar fashion as previous.

# Working Mechanism

- Each device has 2 client IDs. One for publishing and one for subscribing.
- Each device connects to the online broker [MQTT Eclipse](https://mqtt.eclipse.org).
- Each device subscribes to a specific topic and listens on port 1883 and receives any new message which has been published to that port.
- Every device can also publish their own message to a specific topic.
- The code internally uses separate threads for subscriber and publisher.
- Whenever any new message is published by a device, a CSV file records and maintains the patient details.

# Inventory Manager

## About

This script processes patient information csv file generated by the mqtt devices of this repository and based on the procedure entered in these devices, maintains record of items in inventory required for that procedure and alerts when there is shortage of any item in inventory.

As mentioned in the problem statement when a cardiac procedure is performed, a cardiac catheter is required so whenever cardiac procedure is performed the count of cardiac catheter is reduced and if the count of catheter is less than three the module alerts the concerned person by sending a mail.

## Usage

All paths are set as per this repository,  you can reset these paths as per your requirements: the path of directory to be watched for patient info file, patient file path and inventory file path in global variable section of script.

This script uses local SMTP server to recieve mail which can be changed to run on any other SMTP server, to initiate local SMTP server use command mentioned in the next line in command prompt. Run SMTP server.

```
python -m smtpd -c DebuggingServer -n localhost:1025
```

Now execute Inventory Manager python file as

```
python InventoryManager.py
```

Keep the script running while the devices are being used.

## Description

The module identifies modification whenever the patient file is updated using watchdog, which watches directory for change. Whenever the patient file is modified the event gets detected.

On detection of modification the last patient details are read from the CSV file and the procedure performed is identified.

A procedure dictionary is used which lists out procedures and required item for that procedure. The procedure is mapped to the corresponding item.

Count of the required item is reduced in the inventory CSV.

Whenever count of item is below a given threshold(here 3) a mail is sent using SMTP(here to local SMTP server).

This is simple chart to elaborate all basic components:

![alt text] (https://github.com/Engin-Boot/sync-devices-s1b2/blob/master/Documentation/flow.png)
