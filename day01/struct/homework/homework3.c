#include <stdio.h>

int main(){
    int arr[5];
    int sum = 0;
    for(int i=0; i<5; i++){
        printf("please input %d number:\n",i+1);
        scanf("%d",&arr[i]);
        printf("arr[%d]=%d\n",i,arr[i]);
        sum += arr[i];
    }
    printf("sum:%d\n",sum);
    double av = sum/5.0;
    printf("av:%lf\n",av);
    
    
    return 0;
}