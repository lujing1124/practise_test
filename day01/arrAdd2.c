#include <stdio.h>


int main(){
    int *arr[3];
    int a = 10;
    int b = 30;
    int c = 60;

    arr[0] = &a;
    arr[1] = &b;
    arr[2] = &c;

    // *arr+0
    printf("**arr[0]=%d\n",*(*(arr+2)));
   
    
    return 0;
}