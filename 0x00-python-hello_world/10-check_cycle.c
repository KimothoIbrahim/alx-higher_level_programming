#include "lists.h"

/**
 * check_cycle - check for a cycle
 * @list: linked list to check
 *
 * Return: if cycle return 1, if it doesn't return 0
 */
int check_cycle(listint_t *list)
{
	listint_t *low = list;
	listint_t *high = list;

	if (!list)
		return (0);

	while (low && high && high->next)
	{
		low = low->next;
		high = high->next->next;
		if (low == high)
			return (1);
	}
	return (0);
}
