#include <stdio.h>
#include <string.h>

void
get_unHappyIndices(char *Stack, int len, int *array)
{
	int i = 0;
	int s = 0;
	int c = 0;

	for (i = 0; i < len; i++) {
		if ((Stack[i] == '-') && (c == 0)) {
			s = i;
			c = 1;
		} else if (Stack[i] == '-') {
			c++;
		} else if (Stack[i] == '+') {
			if (c != 0) {
				array[s] = c;
				s = 0;
				c = 0;
			}
		}
	}
	if (c != 0) {
		array[s] = c;
		s = 0;
		c = 0;
	}
}

int
Solve(char *Stack, int len)
{
	int i = 0;
	int count = 0;
	int ent = 0;
	int unHappyIndices[120] = {0};

	get_unHappyIndices(Stack, len, unHappyIndices);

	while (i < len) {
		if (unHappyIndices[i]) {
			ent = unHappyIndices[i];
			if (i == 0) {
				count++;
			} else {
				count += 2;
			}
			i += ent;
		} else {
			i++;
		}
	}
	return count;
}

int
main(void)
{
	int i = 0;
	int T;
	int count = 0;
	char Stack[120] = {0};

	scanf("%d", &T);

	for (i = 0; i < T; i++) {
		memset(Stack, 0, sizeof(Stack));
		scanf("%s", Stack);
		count = Solve(Stack, strlen(Stack));
		printf("Case #%d: %d\n", (i+1), count);
	}
	return 0;
}

