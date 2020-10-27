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
