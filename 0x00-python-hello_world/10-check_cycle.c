#include "lists.h"

/**
 * check_cycle - check whether the linked list has cycle in it
 * @list: linked list
 * Return: 0 if there is no cycle, else 1
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list->next;

	if (list == NULL)
		return (0);
	while (slow != NULL && fast->next != NULL && fast != NULL)
	{
		if (slow == fast)
			return (1);
		fast = fast->next->next;
		slow = slow->next;
	}
	return (0);
}
