#include <stdio.h>

typedef struct Student 
{
    char name[20];
    int age;
} Stu;
int main(){
    Stu s = {"jenny",20}; 
    printf("name:%s, age:%d\n",s.name,s.age);

    Stu *p = &s;
    printf("name:%s, age:%d",p->name,p->age);

    return 0;
  
}