#include <stdio.h>

enum week
{
    SUN ,MON,TUE
};
int main(){
    enum week day ;
    day = TUE;

    switch (day){
        case MON:
            printf("1");
            break;
        case TUE:
            printf("2");
            break;
        default:
            printf("---");
            break;
    }

    return 0;
  
}