#include "lists.h"

/**
 * recursive_traverse - goes through linked list and back
 * @p2: pointer to list node
 * @p1: pointer to pointer to list node
 *
 * Return: 1 if values of nodes are equal, 0 otherwise
 */
int recursive_traverse(listint_t *p2, listint_t **p1)
{
	if (!p2)
		return (1);

	if (recursive_traverse(p2->next, p1) == 0)
		return (0);

	if  (p2->n == (*p1)->n)
	{
		*p1 = (*p1)->next;
		return (1);
	}
	else
		return (0);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer to list's head
 *
 * Return: 0 if not palindrome, 1 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *p1 = *head;
	listint_t *p2 = *head;

	if (recursive_traverse(p2, &p1) == 0)
		return (0);

	return (1);
}
