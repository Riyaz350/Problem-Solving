#include <stdio.h>

int main(){
    int i,remain, div, new=0;
    printf("Enter the number you want to revers: ");
    scanf("%d", &i);
    div = i;
    while(div >0){
        remain = div%10;
        new = new*10+remain;
        div = div/10;
    }
        printf("%d \n",new);
    
}