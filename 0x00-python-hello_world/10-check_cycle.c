#include "lists.h"
/**
 * check_cycle - Function that checks weather cycle in list
 * @list: input list
 * Return: 1 if there is a cycle and 0 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *a;
	listint_t *b;

	if (list == NULL)
		return (0);

	a = list;
	b = list;

	while (b->next != NULL && b->next->next != NULL)
	{
		a = a->next;
		b = b->next->next;

		if (a == b)
		{
			a = list;
			while (a != b)
			{
				a = a->next;
				b = b->next;
			}
			return (1);
		}
	}
	return (0);
}
