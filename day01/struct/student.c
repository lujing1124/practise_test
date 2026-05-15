#include <stdio.h>
#include <string.h>
struct Student
{
    char name[20];
    int age;
};
int main(){
    struct Student s = {
        "tom",18
    };

    printf("name:%s,age:%d\n",s.name,s.age);
    strcpy(s.name,"jacky");
    s.age = 20;
    printf("name:%s,age:%d",(&s)->name,(&s)->age);
}