#include <stdio.h>



int suma(int a, int b){

	int c = a + b;
	printf("la suma es > %d \n", c );
	return c;
}

int resta(int a, int b){

	int c = a -b;
	printf("la resta es > %d\n",c );
}

int division(int a, int b){

	if(b == 0){
		printf("error no esta permitido la divsion por cero\n");
	}
	else{
		int c = a / b;
		printf("La division es > %d\n",c);

		return c;
	}	
}

int multiplicacion(int a, int b){

	int c = a * b;
	printf("La multiplicacion es > %d \n", c);

	return c;
}


int main(int argc, char const *argv[])
{
	
	//suma(4,2);
	division(5,5);
	multiplicacion(2,2);
	return 0;
}