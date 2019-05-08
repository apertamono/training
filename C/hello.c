#include <stdio.h>

// Hello World but shifting characters one place
// Real test is whether fputc and stdout work
// No. This is a C program, actually.

int main()
{
  for (char *s="Ifmmp!Xpsme\v"; *s; fputc((*s++)-1, stdout));
  return 0;
}	
