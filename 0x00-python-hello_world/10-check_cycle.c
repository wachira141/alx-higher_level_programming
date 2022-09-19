#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: singly list to check
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
listint_t *next_node = list;
listint_t *prev_node = list;

if (list == NULL)
	return (0);

while (1)
{
if (next_node->next != NULL && next_node->next->next != NULL)
{
next_node = next_node->next->next;
prev_node = prev_node->next;

if (next_node == prev_node)
	return (1);
}
else
return (0);
}
}
