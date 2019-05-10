#include <iostream>
#include <string.h>

using namespace std;

// Test whether a string is a palindrome
// From Bjarne Stroustrup, Programming - Principles and Practice Using C++ (Second Edition), Chapter 18: Vectors and Arrays (free sample)
// Not sure which dependencies he's assuming

// Compiler errors for special characters copied from PDF
// Retyped everything

// Version 2: add graceful exit instead of Ctrl+C

bool is_palindrome(const string& s)
{
	int first = 0;				// index of first letter
	int last = s.length()-1; 	// index of last letter
	while (first < last) {		// we haven't reached the middle
		if (s[first]!=s[last]) return false;
		++first;				// move forward
		--last;					// move backward
	}
	return true;
}

int main()
{
	for (string s; cin>>s; ) {
		if (s=="exit") break; 	// wouldn't this be too simple? no, it works
		cout << s << " is";
		if (!is_palindrome(s)) cout << " not";
		cout << " a palindrome\n";
	}	
}	
