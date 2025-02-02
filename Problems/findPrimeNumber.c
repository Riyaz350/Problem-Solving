#include <stdio.h>
#include <stdbool.h>
#include <math.h>

int main() {
    int i ;
    bool prime = true;

     

    for(int num = 2; num <100; num++){
         
    
        for (i = 2; i <= sqrt(num); i++) {
            if (num % i == 0) {
                prime = false;
                printf("%d is not a prime number.\n", num);
                break;
            }else{
                prime = true;
            }
        }
    
        if (prime) {
            printf("%d is a prime number.\n", num);
        }
    }

    return 0;
}