#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *my_slow = list;
listint_t *my_fast = list;

	if (!list)
		return (0);

	while (my_slow && my_fast && my_fast->next)
	{
		my_slow = my_slow->next;
		my_fast = my_fast->next->next;
		if (my_slow == my_fast)
			return (1);
	}

	return (0);
}
