#include <stdio.h>

struct Person{
    char name[20];
    int age;
};

int main(){
    
   struct Person arr[3] = {
        {"jiang",40},{"jenny",41},{"siyuan",10}
    };
    for(int i=0; i<3; i++){
        printf("name:%s, age:%d\n",arr[i].name,arr[i].age);
    }
    
    
    return 0;
}