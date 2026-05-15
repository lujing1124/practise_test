#include "LinkedList.h"
#include <stdio.h>
#include <stdlib.h>

NODE *head = NULL;
int add_node(int data){
    NODE *new_node_point = malloc(sizeof(NODE));
    if(new_node_point==NULL){
        printf("add failed!");
        return 0;
    }
    new_node_point->data = data;
    new_node_point->next = NULL;

    if(head == NULL){
        head = new_node_point;
        printf("first success\n");
        return 1;
    } 
    NODE *current = head;
    while(current->next){
        current = current->next;
    }
    current->next = new_node_point;
    printf("next success\n");
    return 1;

    // free(new_node_point);
}

void print_all_node(){
    NODE *current = head;
    while(current->next){
        printf("current data:%d\n",current->data);
        current = current->next;
    }
}

int delete_node(int delete_node){
    if(!head){
        printf("there is no node can be deleted!\n");
        return 0;
    }
    NODE *current = head;
    NODE *previous = NULL;
    while(current->data && current->data != delete_node){
        previous = current;
        current = current->next;
        if(!current){
            printf("can't find the data you want to delete.\n");
            return 0;
        }
        //第一个就找到了
        if(previous->data == delete_node){
            head = current->next;
            free(current);
            return 1;
        }

        if(current->data == delete_node){
            previous->next = current->next;
            free(current);
            return 1;
        }
    }
}
int update_node(int old_node, int new_node){

}

