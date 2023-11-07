#include <stdio.h>

int main(void)
{
	int arr[] = {1, 2, 3, 5, 3, 2, 1};
	int *p1 = arr;
	int *p2 = arr;
	int len = sizeof(arr)/sizeof(*arr);

	for (int i = 0; i < len/2; i++)
	{
		printf("first pointer --> %d\n", *p1);
		for (int j = i; j < len - i; j++)
		{
			if (j == len - i - 1)
			{
				printf("second pointer --> %d\n", *p2);
			}
			p2++;
		}
		p1++;
		p2 = p1;
	}

	return (0);
}
