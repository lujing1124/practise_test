#include <stdio.h>
void sayHi(){
    printf("hello world");
}

int main(){
    void (*ptr)();  //申明
    ptr = sayHi;
    ptr();
    return 0;
}