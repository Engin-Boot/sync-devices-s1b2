#define CATCH_CONFIG_MAIN
#include "catch.hpp"
#include "../patient-monitors/patientInfo.h"
#include "../patient-monitors/publisher.h"
#include "../patient-monitors/subscriber.h"

using namespace std;
extern int patientcount();
extern void mainMenu();

TEST_CASE("When user enters 1 and enters data to publish then the data to be published is processed as a correct string")
{
	patientInfo testPatientInfo;
	testPatientInfo.setAge(10);
	testPatientInfo.setGender("M");
	testPatientInfo.setName("Mdi");
	testPatientInfo.setProcedureName("puncture");

	string message = testPatientInfo.toString();

	REQUIRE(message == "Mdi;10;M;puncture");
}

TEST_CASE("The published and the data received by subscriber is same for patient-monitors") {

	SUBSCRIBEmain();
	PUBLISHmain();
	patientInfo testPatientInfo;
	testPatientInfo.setAge(10);
	testPatientInfo.setGender("M");
	testPatientInfo.setName("Mdi");
	testPatientInfo.setProcedureName("puncture");

	string message = testPatientInfo.toString();

	publish(message);
	Sleep(5000);

	REQUIRE(message == rec_msg);
}
