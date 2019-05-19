#include <iostream>
#include <string.h>

using std::cout;

// Never hard-code constants
const std::string TXT1 = "Fizz";
const std::string TXT2 = "Buzz";
const int NUM1 = 3;
const int NUM2 = 5;
const int ITER = 100;	

int main()
{
	for(int i=1; i<=ITER; i++)
	{
		if(i%NUM1==0 || i%NUM2==0)
		{
			if(i%NUM1==0) cout << TXT1;
			if(i%NUM2==0) cout << TXT2;
		}
		else
		{
			cout << i;
		}
		cout << std::endl;
	}
	return 0;
}
