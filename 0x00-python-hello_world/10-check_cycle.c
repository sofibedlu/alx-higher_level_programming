#include "lists.h"

/**
 * check_cycle - checks if the list have cycle in it
 * @list: head of the list
 * Return: 0 if there is no cycle, 1 if there is acycle
 */
int check_cycle(listint_t *list)
{
	char **addres = NULL, **pr;
	listint_t *temp;
	int size = 3, tp = 0, i = 0;

	if (list ==NULL)
		return (0);
	addres = malloc(sizeof(char *) * size);
	if (addres == NULL)
	{
		printf("can't allocate memory");
		exit(EXIT_FAILURE);
	}
	temp = list;
	while(temp != NULL)
	{
		addres[i] = (char *)temp;
		if (i == size - 1)
		{
			size += size;
			pr = realloc(addres, sizeof(char *) * size);
			if (!pr)
			{
				printf("allocation error");
				exit(EXIT_FAILURE);
			}
			addres = pr;
		}
		if (i > 0)
		{
			tp = i;
			while(tp >= 0)
			{
				if ((char *)(temp->next) == addres[tp])
				{
					free(addres);
					return (1);
				}
				tp--;
			}

		}
		temp = temp->next;
		i++;
	}
	free(addres);
	return (0);
}
