#include <stdio.h>
#include <stdlib.h>

struct node
{
    int item;
    struct node *next; // recursive DS
};

struct list
{
    struct llnode *front;
};

struct list *list_create(void)
{
    struct list *lst = malloc(sizeof(struct list));
    lst->front = NULL;
    return lst;
}