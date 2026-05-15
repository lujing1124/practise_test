#include <stdio.h>
int main(){
    int i = 0;
    while (i<7){
        
        i++;
        printf("xi xi shua shua %d day\n", i);
        if(i==3){
            goto End;
        }
        
    }
    End:printf("end\n");
    
    return 0;
}