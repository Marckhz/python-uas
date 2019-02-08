#include <stdio.h>
#include <stdlib.h>

// Pass-by-Value
void modify (int a ){

	printf("2. The address of modify a is %p \n", &a);
	a = 15;
	printf("3. The value of modify a is %i\n",a);
}


//Pass-by-Reference

void modify_2(int p, int *q, int *r){

	printf("1. p is %i, q is %i, r is %i\n",p, *q, *r );
	p = 27;
	*q = 27;
	*r = 27;

}





int main(void){

	int *base = NULL;
	base = (int *) malloc(sizeof(int) *100);

	if (base == NULL){
		fprintf(stderr, "malloc failed\n");
		exit(1);
	}

	free(base);

	//int a = 1;
	//int b = 1;
	//int c = 1;
	//int *x = &c;

	//modify_2(a, &b, x);
	//printf("2. a is %i, b is %i, c is %i, x is %i\n",a,b,c,*x );

	return 0;

}


