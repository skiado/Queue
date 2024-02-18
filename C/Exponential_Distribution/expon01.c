#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>       # Απαραίτητη βιβλιοθήκη για τη δημιουργία τυχαίων αριθμών με διαφορετικό seed κάθε φορά.

#define MAX 100000

double exponential(){
  return -log((double)rand()/(double)RAND_MAX);
}

int main(){
  double x[MAX],l,s;
  
  srand(time(NULL));
  printf(" λ = ");
  scanf("%lf",&l);
  for(int i=0;i<MAX;i++){
    x[i] = l * exponential();
    s += x[i];
  }
  printf("mean E[X] = %lf \n",s/MAX);
  return 0;
}
