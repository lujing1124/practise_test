#include <stdio.h>

int findIndex(int arr[],int size,int num){
    int i;
    for(i=0; i<size; i++){
        if(arr[i] == num){
            return ++i;
        }
    }
    return -1;
}

int main(){
    
    int arr[] = {1,2,3,4,5,6,7,8,9};
    int i = findIndex(arr,9,0);
    printf("i:%d",i);
    
    return 0;
}