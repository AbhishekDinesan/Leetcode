// implementation based on CS136, UWaterloo
#include <stdio.h>
#include <stdlib.h>
#include "functions.c"

// A Linked List is a List where each index contains a NODE, which contains an item, and a pointer to another NODE

int main()
{
    char str[50];
    printf("Welcome to the LinkedList Driver.\n");
    printf("Select your command from the list below...\n");
    printf("A - add to a specified index\n");
    printf("R - remove from a specified index\n");
    printf("REVERSE - reverse the list\n");
    printf("MERGE - merge two sorted LinkedLists\n");
    printf("ROTATE - rotate a LinkedList\n");
    printf("MNDelete - Delete M nodes after n nodes in a list\n");
    printf("CONVERT - Convert single LinkedList to Double\n");
    printf("REVERSE* - Reverse a doubly LinkedList\n");
    printf("REMOVE* - Remove all occurances of one linkedlist from another\n");
    printf("MERGE* - Merge K sorted linked lists\n");
    scanf("%s", &str);
    printf("Nah you entered %s", str);
}