#include "pch.h"
#include"..\x-ray\patientInfo.h"
#include"..\x-ray\publisher.h"
#include"..\x-ray\pubsub_opts.h"
#include"..\x-ray\subscriber.h"
#include"..\x-ray\publisher.cpp"
#include"..\x-ray\subscriber.cpp"
#include"..\x-ray\mainMenu.cpp"
#include"..\x-ray\saveDataToCSV.cpp"

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