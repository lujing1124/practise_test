#include <stdio.h>
#include <string.h>
union Tag
{
    int a;
    short b;
    char c;
};
int main(){
    union Tag t;

    // printf("name:%s,age:%d\n",s.name,s.age);
    // strcpy(s.name,"jacky");
    // s.age = 20;
    printf("%p\n%p\n%p\n",&t.a,&t.b,&t.c);
    return 0;
}