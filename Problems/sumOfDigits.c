#include <stdio.h>

int main(){
    int number,sum =0, remain, div;
    printf("enter the number : ");
    scanf("%d", &number);
    div = number;
    while(div != 0){
        remain = div%10;
        sum = sum +remain;
        div = div /10;
    }
    printf("Sum of %d is %d", number, sum);
}