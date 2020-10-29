#include<string.h>
#include<stdio.h>
#include<iostream>
#include<stdlib.h>
#include "./inc/publisher.h"
#include "./inc/subscriber.h"
using namespace std;
extern bool userInput();

char* subclientID = (char*)"x-ray1";
char* pubclientID = (char*)"x-ray";

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