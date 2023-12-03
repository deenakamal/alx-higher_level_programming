#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - check a palindrome.
 *
 * @head: pointer to head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 *
 */
int is_palindrome(listint_t **head)
{
	if (!head || !(*head))
		return (1);
	return (get_palindrome(head, *head));
}
/**
 * get_palindrome - todiscover is palindrom or not
 * @head: pointer to head of list
 * @last_: the last item in list
 * Return: 1 or 0
 */
int get_palindrome(listint_t **head, listint_t last_)
{
	if (last_ == NULL)
		return (1);

	if (get_palindrome(head, last_->next) &&
			(*head)->n == last_0>n)
	{
		*head = (*head_->next);
		return (1);
	}
	return (0);
}
