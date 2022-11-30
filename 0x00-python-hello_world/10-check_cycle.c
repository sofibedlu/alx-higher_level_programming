#include "lists.h"

/**
 * check_cycle - checks if the list have cycle in it
 * @list: head of the list
 * Return: 0 if there is no cycle, 1 if there is acycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	slow = list;
	fast = list->next;
	while (slow != NULL && fast->next != NULL && fast != NULL)
	{
		if (slow == fast)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
