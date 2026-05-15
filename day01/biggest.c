#include <stdio.h>

int main(){
    int arr[] = {1,2,3,40,5,-1,90,4,-4,20};
    int max = arr[0];
    int size = sizeof(arr)/sizeof(arr[0]);// 整个内存的长度/某个元素的长度
    printf("size=%d\n", size);

    for(int i=1; i<size; i++){
        // if(arr[i]>max){
        //     max = arr[i];
        // }
        max = max > arr[i]? max: arr[i];
    }
    printf("max = %d", max);
    return 0;
}