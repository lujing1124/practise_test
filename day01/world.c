#include <stdio.h>

int main(){
    const double pi = 3.1415926;
    double r;

    printf("please input r:\n");
    scanf("%lf", &r);

    double len = 2* pi * r;
    double area = r * r * pi;

    printf("circle's length:%.2lf, circle's area:%.2lf", len, area);
    return 0;
}