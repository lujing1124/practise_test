#include <stdio.h>
#include <string.h>
struct Student
{
    char name[20];
    int age;
};
void func(struct Student temp){
    printf("temp name:%s,age:%d\n",temp.name,temp.age);
    strcpy(temp.name,"jacky");
    temp.age = 50;
    printf("temp name:%s,age:%d",temp.name,temp.age);
}
void funcAdd(struct Student *temp){
    printf("temp name:%s,age:%d\n",temp->name,temp->age);
    strcpy(temp->name,"jennyBig");
    temp->age = 18;
    printf("temp name:%s,age:%d",temp->name,temp->age);
}
int main(){
    struct Student s = {
        "tom",20
    };
    struct Student s1 = {
        "jenny",180
    };
    func(s);
    funcAdd(&s1);
    printf("Sname:%s,Sage:%d\n",s.name,s.age);
    printf("Sname:%s,Sage:%d\n",s1.name,s1.age);
    // strcpy(s.name,"jacky");
    // s.age = 20;
    // printf("name:%s,age:%d",(&s)->name,(&s)->age);
    return 0;
}