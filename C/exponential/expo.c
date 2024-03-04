#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>       /*Για την περίπτωση που θέλουμε να μετρήσουμε τον χρόνο εκτέλεσης ή να δώσουμε seed για διαφορετικό σύνολο ψευδοτυχαίων αριθμών*/

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
    x[i] = (1/l) * exponential();
    s += x[i];
  }
  printf("Theory mean E[X] = %lf \n",1/l);
  printf("My function mean E[X] = %lf \n",s/MAX);
  return 0;
}

/* gcc expon01.c -o exp -lm */
