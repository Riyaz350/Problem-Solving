#include <stdio.h>

int main() {
    // Write C code here
    int num, fact=1;
    printf("Enter the number you want to get factorial of.");
    scanf("%d", &num);
    for(int i = 1; i<=num; i++){
         fact = fact*i;
    }
    printf("Factorial of %d is %d", num, fact);
    return 0;
}