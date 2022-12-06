#include "lists.h"
/**
 * insert_node - insert nod in sorted linked list
 * @head: head of the list
 * @number: the number that will be added to the list
 * Return: head of the new list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *prev, *insert;

	insert = malloc(sizeof(listint_t));
	if (insert == NULL)
		return (NULL);
	insert->n = number;
	insert->next = NULL;
	temp = (*head)->next;
	prev = *head;
	if (*head == NULL)
	{
		*head = insert;
		return (*head);
	}
	if ((*head)->n > insert->n)
	{
		insert->next = *head;
		*head = insert;
	}
	else
	{
		while (temp != NULL)
		{
			if (temp->n >= insert->n)
			{
				insert->next = temp;
				prev->next = insert;
				break;
			}
			prev = temp;
			temp = temp->next;
			if (temp == NULL)
			{
				prev->next = insert;
				break;
			}
		}
	}
	return (*head);
}
