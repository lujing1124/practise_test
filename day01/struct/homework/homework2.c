#include <stdio.h>
int getRes(int a, int b, int(*opt)(int,int)){
    int res = opt(a,b);
    return res;
}
int max(int a, int b){
    return a>b?a:b;
}
int min(int a, int b){
    return a<b?a:b;
}

int main(){
    printf("max:%d\n",getRes(100,50,max));
    printf("min:%d\n",getRes(100,50,min));
    
    
    return 0;
}