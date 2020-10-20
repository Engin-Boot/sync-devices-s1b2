#define CATCH_CONFIG_MAIN
#include "catch.hpp"
//#include "patientInfo.h"
//#include "../MRI/Procedure.cpp"
#include "patientInfo.h"
#include "publisher.h"
#include "subscriber.h"

using namespace std;
extern int patientcount();
extern void mainMenu();
string rec_msg;


TEST_CASE("The published and the data received by subscriber is same") {

	SUBSCRIBEmain();
	PUBLISHmain();
	patientInfo testPatientInfo;
	testPatientInfo.setAge(10);
	testPatientInfo.setGender("M");
	testPatientInfo.setName("Mdi");
	testPatientInfo.setProcedureName("puncture");

	string message = testPatientInfo.toString();
	Sleep(5000);

	struct pubsub_opts opts =
	{
		1, 0, 0, 0, "\n", 100,  	/* debug/app options */
		NULL, NULL, 1, 0, 0, /* message options */
		MQTTVERSION_DEFAULT, "my_topic", "patient-monitors", 0, 0, NULL, NULL, "localhost", "1883", NULL, 10, /* MQTT options */
	};

	publish(message);
	Sleep(5000);

	REQUIRE(message == rec_msg);
}