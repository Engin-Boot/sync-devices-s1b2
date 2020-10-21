#pragma once

#include <iostream>
#include<string>

using namespace std;

class patientInfo {
private:
    string name;
    string gender;
    int age;
    string procedureName;
    string Rmsg;

public:
    patientInfo() {}
    patientInfo(const string& Name,const string& Gender,int Age,const string& ProcedureName,const string& RMSG) : name(Name), gender(Gender), age(Age), procedureName(ProcedureName),Rmsg(RMSG) {}

    string getName() {
        return name;
    }

    string getGender() {
        return gender;
    }

    int getAge() {
        return age;
    }

    string getProcedureName() {
        return procedureName;
    }
    string getReceivedString()
    {
        return Rmsg;
    }

    void setName(const string& newName) {
        name = newName;
    }

    void setGender(const string& newGender) {
        gender = newGender;
    }

    void setAge(int newAge) {
        age = newAge;
    }
    void setProcedureName(const string& newProcedure) {
        procedureName = newProcedure;
    }
    void setReceivedString(const string& msg)
    {
        Rmsg = msg;
        
    }
    string toString() {
        string result = name + ";" + to_string(age) + ";" + gender + ";" + procedureName;
        return result;
    }
};

extern string rec_msg;

