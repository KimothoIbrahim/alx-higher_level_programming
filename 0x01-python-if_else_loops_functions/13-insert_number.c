#include "lists.h"

/**
 * insert_node - puts into singly-linked list.
 * @head: head of linked list.
 * @number: what to insert.
 *
 * Return: NULL on failure, else return a pointer to new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *neww;

	neww = malloc(sizeof(listint_t));
	if (neww == NULL)
		return (NULL);
	neww->n = number;

	if (node == NULL || node->n >= number)
	{
		neww->next = node;
		*head = neww;
		return (neww);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	neww->next = node->next;
	node->next = neww;

	return (neww)
