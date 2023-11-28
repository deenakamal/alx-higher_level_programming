#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - a function in C that inserts a number into a sorted singly linked list.
 * @head: head
 * @number: number input
 *
 * Return: NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr1;
	listint_t *ptr2;
	listint_t new_;

	new_ = malloc(sizeof(listint_t));

	if (!new_)
		return (NULL);
	new_->n = number;
	new_->next = NULL;

	if (!(*head))
	{
		*head = new_;
		return (*head);
	}
	if (new_->n < (*head)->n)
	{
		new_->next = *head;
		*head = new_;
		return (*head);
	}
	ptr2 = *head;
	while (ptr2 && (new_->n > ptr2->n))
	{
		ptr1 = ptr2;
		ptr2 = ptr2->next;
	}
	new_->next = ptr2;
	ptr1->next = n_node;
	return (*head);
}
