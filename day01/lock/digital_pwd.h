#ifndef __DIGITAL_PWD_H__
#define __DIGITAL_PWD_H__

#define ADMIN_DEFAULT_PWD 123456

typedef struct Digital_PWD_Linked_List_Node{
    char pwd[20];
    struct Digital_PWD_Linked_List_Node *next;
} NODE;

int add_node(char new_pwd[20]);

int delete_node(char delete_pwd[20]);

int delete_all_node();

//是否已经包含 1：包含，0：不包含
int is_contain(char new_pwd[20]);

#endif