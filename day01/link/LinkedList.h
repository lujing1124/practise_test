#ifndef __LINKED__LIST_H_
#define __LINKED__LIST_H_

typedef struct LinkedListNode {
    int data;
    struct LinkedListNode *next;
}NODE;

int add_node(int data);
void print_all_node();
int delete_node(int delete_node);
int update_node(int old_data, int new_data);

#endif