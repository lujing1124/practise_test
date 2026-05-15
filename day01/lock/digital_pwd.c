#include "digital_pwd.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

NODE *head = NULL;
int add_node(char new_pwd[20]){
    NODE *new_node = malloc(sizeof(NODE));
    if(!new_node){
        return 0;
    }

    // new_node->pwd = new_pwd;
    strcpy(new_node->pwd, new_pwd);
    new_node->next = NULL;

    if(!head){
        head = new_node;
        return 1;
    }
    
    NODE *current = head;
    while(current->next != NULL){
        current = current->next;
    }

    current->next = new_node;
    return 1;
}

int is_contain(char new_pwd[20]){
    if(!head){
        return 0;
    }
    NODE *current = head;
    while(current != NULL){
        if(!strcmp(current->pwd, new_pwd)){
            printf("已经有相同的密码了！");
            return 1;
        }
        current = current->next;

    }
    return 0;
}

int delete_node(char delete_pwd[20]){}

int delete_all_node(){}
