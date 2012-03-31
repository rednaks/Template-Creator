#!/usr/bin/python

import os
import sys



# Creating directory
def MakeDir(dir_name):
	#d = os.path.dirname(dir_name)
	if not os.path.exists(dir_name):
		os.makedirs(dir_name)


# Creating class header
def Class_H(class_name):
	header = '''#ifndef %s_H
#define %s_H
#include "../../main.h"

class %s{
//Attributs :
private:


//Constructors & Destructors:
public:
	%s();	// default Constructor you can add yours here.
	~%s();

//Ops :
public:

};
#endif''' % (class_name.upper(), class_name.upper(), class_name.title(), class_name.title(), class_name.title())

	f = open(class_name+'/'+class_name+'.h', 'w')
	f.write(header)
	f.close()

def Class_CPP(class_name):
	cpp = '''#include "%s.h"
// Constructor 
%s::%s{

}

// Destructor
%s::~%s{

}


// Other Ops:''' % (class_name, class_name.title(), class_name.title(), class_name.title(), class_name.title())

	f = open(class_name+'/'+class_name+'.cpp',"w")
	f.write(cpp)
	f.close()

# Main :
def Main_H():
	header = '''#ifndef MAIN_H
#define MAIN_H
#include <iostream>

using namespace std;

#endif'''
	f = open("main/main.h","w")
	f.write(header)
	f.close()

def Main_CPP():
	cpp = '''#include "main.h"

int main(int argc, char **argv)
{
	// Implement your program here


	return 0;
}'''
	f = open("main/main.cpp","w")
	f.write(cpp)
	f.close()

def MainTemplate():
	MakeDir("main")
	Main_H()
	Main_CPP()

# Creating class
def ClassTemplate(class_name):
	MakeDir(class_name)
	Class_H(class_name)
	Class_CPP(class_name)



# Make sure to pass lowser case args !

if __name__ == "__main__":
	print 'Creating MainTemplate ...'
	MainTemplate()
	for i in range(1,len(sys.argv)):
		class_n = sys.argv[i].lower()
		print 'Creating %s ClassTemplate' % (class_n)
		ClassTemplate(class_n)

