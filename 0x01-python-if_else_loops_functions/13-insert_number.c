#include "lists.h"
/**
* insert_node - The function that inserts a number into a sorted singly linked list
* @head: pointer to head node
* @val: value to be inserted
*
* Return: address of new node or NULL on failure
*/
listint_t *insert_node(listint_t **head, int val)
{
		listint_t *current = &head;
		listint_t *next = current->next;
		while (current->next != '\0')
		{
				if (next->n > val)
				{
						current->n = val;
						current->next = current->next;
						return (current);
				}
				current = current->next;
		}
		return (NULL);
}
