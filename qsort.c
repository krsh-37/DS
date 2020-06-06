#include <stdio.h>
#include <stdlib.h>

char values[5] = { 'a','z','c','b','p'};

int cmpfunc (const void * a, const void * b) {
   return ( *(char*)a - *(char*)b );
}

int main () {
   int n;

   printf("Before sorting the list is: \n");
   for( n = 0 ; n < 5; n++ ) {
      printf("%c ", values[n]);
   }

   qsort(values, 5, sizeof(char), cmpfunc);

   printf("\nAfter sorting the list is: \n");
   for( n = 0 ; n < 5; n++ ) {   
      printf("%c ", values[n]);
   }
  
   return(0);
}
