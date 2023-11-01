#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to pointer to list's head
 * @number: number to be inserted
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *p1, *p2, *node;

	if (head == NULL)
		return (NULL);

	if (*head == NULL || number < (*head)->n)
	{
		node = malloc(sizeof(listint_t));
		node->n = number;
		node->next = *head;
		*head = node;
		return (node);
	}
	p1 = *head;
	p2 = p1->next;
	while (p2 != NULL)
	{
		if (number > p2->n)
		{
			p1 = p1->next;
			p2 = p2->next;
		}
		else
		{
			node = malloc(sizeof(listint_t));
			node->n = number;
			node->next = p2;
			p1->next = node;
			if (node->next == *head)
				*head = node;
			return (node);
		}
	}
	node = malloc(sizeof(listint_t));
	node->n = number;
	p1->next = node;
	if (*head == NULL)
		*head = node;
	return (node);
}
