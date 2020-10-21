
#define CATCH_CONFIG_MAIN
#include "../patient-monitors-test/catch.hpp"
#include "../x-ray/patientInfo.h"
#include "../x-ray/publisher.h"
#include "../x-ray/subscriber.h"

using namespace std;
extern int patientcount();
extern void mainMenu();


TEST_CASE("The published and the data received by subscriber is same for x-ray") {

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
