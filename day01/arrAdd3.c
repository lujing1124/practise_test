#include <stdio.h>

void printAll(int *arr,int n){
    // int n = sizeof(arr)/sizeof(arr[0]);
    // printf("arrlen=%d\n",n);
    for(int i=0; i<n; i++){
        printf("arr[%d]=%d\n",i,*(arr+i));
    }
    
}
int main(){
    int arr[]={1,4,23,5,88,76,8,7};
    
    printAll(arr,8);
   
    
    return 0;
}