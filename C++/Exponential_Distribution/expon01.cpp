// exponential_distribution
#include <iostream>
#include <random>
#include <cstdlib> 

#define MAX 100000

using namespace std;

double my_exponential(){
  return -log((double)rand()/(double)RAND_MAX);
}

int main() {
  double x[MAX],l,s;

  cout << " λ = ";
  cin >> l;
  
  default_random_engine generator;
  exponential_distribution<double> distribution(1);
  s = 0;
  for (int i=0; i<MAX; ++i) {
    x[i] = (1/l) * distribution(generator);
    s += x[i];
  }
  cout << "From Theory  mean E[X} = " << 1/l << endl;
  cout << "From c++ random library " << endl;
  cout << "mean E[X] = " << s/MAX <<endl;
  s = 0;
  for (int i=0; i<MAX; ++i) {
    x[i] = (1/l) * my_exponential();
    s += x[i];
  }
  cout << "From my function" << endl;
  cout << "mean E[X] = " << s/MAX <<endl;
  
  return 0;

}

/* g++ -o exp02 -p exponential02.cpp  */
