#include <stdio.h>
#include <string.h>

int array[2501];

int
main(void)
{
	int T, N, i, j, k, val;

	scanf("%d", &T);
	for (i = 0; i < T; i++) {
		memset(array, 0, sizeof(array));
		scanf("%d", &N);
		printf("Case #%d: ", i+1);
		for (j = 0; j < ((2 * N) - 1) * N; j++) {
			scanf("%d ", &val);
			array[val-1]++;
		}
		for (j = 0; j < 2501; j++) {
			if ((array[j] & 1) != 0) {
				printf("%d ", j+1);
			}
		}
		printf("\n");
	}
	return 0;
}
