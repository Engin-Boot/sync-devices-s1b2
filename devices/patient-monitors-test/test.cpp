#include "pch.h"
#include"..\patient-monitors\patientInfo.h"
#include"..\patient-monitors\publisher.h"
#include"..\patient-monitors\pubsub_opts.h"
#include"..\patient-monitors\subscriber.h"
#include"..\patient-monitors\publisher.cpp"
#include"..\patient-monitors\subscriber.cpp"
#include"..\patient-monitors\mainMenu.cpp"
#include"..\patient-monitors\saveDataToCSV.cpp"

TEST(MRITESTING ,PatientDetails) {
    SUBSCRIBEmain();
    PUBLISHmain();
    sleep(3000);
    patientInfo publisherpatientInfo;
    publisherpatientInfo.setName("shivani");
    publisherpatientInfo.setAge(22);
    publisherpatientInfo.setGender("M");
    publisherpatientInfo.setProcedureName("cardio");
    string finalDetails = publisherpatientInfo.toString();
    publisherpatientInfo.setReceivedString(finalDetails);
    publish(finalDetails);
    sleep(3000);
  EXPECT_EQ(publisherpatientInfo.getReceivedString(), subscriberPatientInfo.getReceivedString());
  EXPECT_TRUE(true);
}