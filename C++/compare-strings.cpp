#include <iostream>
#include <string.h>

// using namespace std;
using std::cin;
using std::cout;

// Does strcmp return a specific number when it's <>0?
// Yes!

// Fatal error: iostream.h - no such file or directory
// ISO C++ standard headers do not have any extensions unless they are compiler-specific or user-defined
// More errors for the oneliner: 	cout << strcmp("Veenendaal", "Venlo");
// Solutions: https://stackoverflow.com/questions/15185801/cout-was-not-declared-in-this-scope
// I thought it was declared in iostream, but that was not enough

// Read why using standard namespace is not a good idea for beginners: https://stackoverflow.com/questions/1452721/why-is-using-namespace-std-considered-bad-practice
// Collisions! The std namespace has tons of identifiers, many of which are very common ones (think list, sort, string, iterator, etc.) which are very likely to appear in other code, too.
// It's especially bad in header files

// Changed WSL background color to read error messages (can't use black background for vim, can't use white background for gcc)

// Output: -1 // This was wrong
// Edited to use input
// Difference between "c" and "b": 1
// Difference between "Nederland" and "Utrecht": -7
// Difference between "Sch" and "Aca": 18
// Difference between "Veenendaal" and "Venlo": -9
// Difference between "A" and "a": -32
// Difference between "Programma" and "Programm": 97
// Difference between "1533" and "1532": 1
// Difference between "133" and "13": 51
// Difference between "1542" and "1521": 2
// Difference between "A" and "1": 16
// See ASCII table

int main()
{
	int verschil = 0;
	char string1[64], string2[64];
	  cout << "Enter first string: ";
	  cin >> string1;
	  cout << "Enter second string: ";
	  cin >> string2;
	verschil = strcmp(string1, string2);
	cout << "The difference is: " << verschil;
	return 0;
}	
