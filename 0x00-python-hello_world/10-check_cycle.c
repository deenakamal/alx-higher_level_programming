#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: pointer for first element in list
 * Return: 1 if has cycle and 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *s_ptr1, *f_ptr2;

	s_ptr1 = list;
	f_ptr2 = list;

	while (s_ptr1 != NULL && f_ptr2 != NULL && f_ptr2->next)
	{
		s_ptr1 = s_ptr1->next;
		f_ptr2 = f_ptr2->next->next;

		if (s_ptr1 == f_ptr2)
			return (1);
	}
	return (0);
}
