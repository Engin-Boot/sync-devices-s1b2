#include<string.h>
#include<stdio.h>
#include<iostream>
#include<stdlib.h>
#include "publisher.h"
#include "subscriber.h"
using namespace std;
extern int patientcount();
extern void mainMenu();


bool userInput()
{
	cout << "welcome!!! enter 1 if you want to enter your details\n enter 0 to exit\n else do nothing\n";
	int option;
	cin >> option;

	if (option == 0)
	{
		cout << "exiting the device" << endl;
		Sleep(2000);
		return false;
	}
	if (option == 1)
		mainMenu();
	Sleep(2000);

	return true;
}

int main()
{
	int check = SUBSCRIBEmain();
	if (check != 0)
	{
		cout << "subscription failed:" << endl;
		cout << check << endl;
	}
	PUBLISHmain();

	while (userInput());
	return 0;
}