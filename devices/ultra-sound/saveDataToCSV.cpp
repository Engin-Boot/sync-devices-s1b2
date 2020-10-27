#include<iostream>
#include<fstream>
#include<sstream>
#include<string>
#include<vector>

using namespace std;

void IfFirstOperationCreateCSV()
{
	fstream fout;
	fout.open("patientdetailsReport.csv");
	if (fout.fail())
	{
		fout.open("patientdetailsReport.csv", ios::out);
		fout << "PatientName" << "," << "Age" << "," << "Gender" << "," << "Procedure" << "," << "\n";
	}
	return;
}

void saveDataToCSV(string msg)
{
	fstream fout;
	IfFirstOperationCreateCSV();
	fout.open("patientdetailsReport.csv", ios::app);
	string param;
	vector<string> patientParam;
	stringstream ss(msg);
	while (getline(ss, param,';' ))
	{
		
		patientParam.push_back(param);
		
	}
	for (int i = 0;i < patientParam.size();i++)
	{
		fout << patientParam[i] << ",";
	}
	fout <<"\n";
	
}
