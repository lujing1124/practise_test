#include <stdio.h>
int add(int x, int y){
    printf("+,a%d,y%d", x,y);
    return x+y;
}
int sub(int x, int y){
    printf("-,a= %d,b=%d", x,y);
    return x-y;
}
int calc(int a, int b,int(*p)(int, int)){
    int res = p(a,b);
    return res;
}

int main(){
    
    printf("result=%d",calc(20,55, add));
    return 0;
}