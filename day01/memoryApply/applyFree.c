#include <stdio.h>
#include <stdlib.h>

int main(){
    int size;
    printf("please input the number you want to apply:\n");
    scanf("%d",&size);

    int memoryLength = sizeof(int)*size;
    int *arr = malloc(memoryLength);
    if(arr==NULL){
        printf("apply falled!");
        return 0;
    }
    printf("apply address:%p\n",arr);
    int i;
    for(i=0; i<size; i++){
        arr[i] = i*10;
    }
    for(i=0; i<size; i++){
        printf("arr[%d]=%d\n",i,arr[i]);
    }
    free(arr);
    arr=NULL;
    for(i=0; i<size; i++){
        printf("arr[%d]=%d\n",i,arr[i]);
    }
    return 0;
}