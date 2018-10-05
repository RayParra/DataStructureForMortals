//factorialRecursivo.cpp

#include  <iostream>
using namespace std;
int factorial(int n) {
   if(n < 0) return 0;
   else if(n > 1) return n*factorial(n-1);
   return 1;
}
int main(void) {
   int numero;
   cout<<"ingresa un numero: ";
   cin>>numero;
   cout<<"Factorial de "<< factorial(numero) << endl;
}