#include "lists.h"

/**
 * reverse_listint - reverses a linked list
 * @head: pointer to the first node in the list
 * Return: pointer to the first node in the new list
 */
void reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the linked list
 *
 * Return: 1 if it is, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *perv = *head, *new = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			new = slow->next;
			break;
		}
		if (!fast->next)
		{
			new = slow->next->next;
			break;
		}
		slow = slow->next;
	}

	reverse_listint(&new);

	while (new && perv)
	{
		if (perv->n == new->n)
		{
			new = new->next;
			perv = perv->next;
		}
		else
			return (0);
	}

	if (!new)
		return (1);

	return (0);
}
