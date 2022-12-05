#include "lists.h"
#include <stdio.h>
listint_t *reverse(listint_t **second);
/**
 * is_palindrome - check for singly linked list is palindrome
 * @head: head of linked list
 * Return: 0 if it is not a palindrome, else 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *start_second;
	listint_t *rev;
	int size = 0, i;
	listint_t *temp = *head;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (temp)
	{
		temp = temp->next;
		size++;
	}
	temp = *head;
	for (i = 0; i < (size / 2) - 1; i++)
		temp = temp->next;
	if (size / 2 != 0)
		start_second = temp->next->next;
	else
		start_second = temp->next;
	temp = *head;
	rev = reverse(&start_second);
	while (rev != NULL)
	{
		if (temp->n != rev->n)
		{
			return (0);
		}
		temp = temp->next;
		rev = rev->next;
	}
	return (1);
}
/**
 * reverse - reverse the linked list
 * @second: second half list
 * Return: listint_t
 */
listint_t *reverse(listint_t **second)
{
	listint_t *temp;
	listint_t *prev = NULL;

	while (*second != NULL)
	{
		temp = (*second)->next;
		(*second)->next = prev;
		prev = *second;
		*second = temp;
	}
	*second = prev;
	return (*second);
}
