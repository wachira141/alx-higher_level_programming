#include "lists.h"
/**
 * insert_node - function to insert node
 * @head: the head node
 * @number: the number to insert
 * Retun: address of the node or Null if it fails
 */

listint_t *insert_node(listint_t **head, int number)
{
listint_t *temp = *head;
listint_t *new_node;

new_node = malloc(sizeof(listint_t));
if(!new_node)
	return (NULL);

if (temp == NULL || temp->n >= number)
{
new_node->next = temp;
*head = new_node;
return(new_node);
}
while (temp && temp->next && temp->next->n < number)
	temp = temp->next;

new_node->next = temp->next;
new_node->n = number;
temp->next = new_node;

return (new_node);
}
