#include <stdio.h>

//Macros
#define PI 3.1416
#define CUBO(a) a*a*a



int call_macro(int a){


	printf("Macro a la potencia > %d\n",CUBO(a) );

	return a;
}


int main(int argc, char const *argv[])
{
	
	call_macro(3);

	return 0;
}
