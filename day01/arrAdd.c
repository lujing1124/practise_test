#include <stdio.h>


int main(){
    int arr[] = {1,2,34,45,56,67,87,22};
    // for(int i=0; i<sizeof(arr)/sizeof(arr[0]); i++){
    //     // printf("result=%d\n",arr[i]);
    //     printf("arr[%d]=%d\n",i,*(arr+i));
    // }
    int n = sizeof(arr)/sizeof(arr[0]);
    int *p = arr;
    for(int i=0; i<n; i++){
        // printf("result=%d\n",arr[i]);
        printf("arr[%d]=%d\n",i,*(p+i));
    }
    
    return 0;
}