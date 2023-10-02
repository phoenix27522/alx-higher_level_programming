#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: pointer to the head of the linked list
 * Return: 1 if there is a cycle, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *flash, *sloth;

	flash = list;
	sloth = list;
	while (flash != NULL && sloth != NULL && sloth->next != NULL)
	{
		flash = flash->next;         /* Move one step */
		sloth = sloth->next->next;          /* Move two steps */
		if (flash == sloth)             /* If they meet, there's a cycle */
			return (1);
	}
	return (0); /* No cycle found */
}

