#include "pch.h"
#include"..\ultra-sound\patientInfo.h"
#include"..\ultra-sound\publisher.h"
#include"..\ultra-sound\pubsub_opts.h"
#include"..\ultra-sound\subscriber.h"
#include"..\ultra-sound\publisher.cpp"
#include"..\ultra-sound\subscriber.cpp"
#include"..\ultra-sound\mainMenu.cpp"
#include"..\ultra-sound\saveDataToCSV.cpp"

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