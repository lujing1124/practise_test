#include "LinkedList.h"
#include <stdio.h>
#include <stdlib.h>

int main(){
    printf("---%d\n",add_node(10));
    printf("---%d\n",add_node(20));
    printf("---%d\n",add_node(30));
    printf("---%d\n",add_node(40));
    printf("---%d\n",add_node(50));
    print_all_node();
    delete_node(30);
    print_all_node();
    return 0;
}

