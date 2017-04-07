#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void
Solve(char *String, int len, char *Output)
{
	int i = 0;
	
	for (i = 0; i < len; i++) {
		if (i == 0) {
			Output[i] = String[i];
		} else if (String[i] < Output[0]) {
			Output[i] = String[i];
		} else {
			memmove(Output+1, Output, i);
			Output[0] = String[i];
		}
	}
}


int
main(void)
{
	int i;
	int T;
	int len = 0;
	char *String = calloc(1, 1005);
	char *Output = calloc(1, 1005);
	
	if (NULL == String || NULL == Output) {
		printf("\n Failed to allocate memory\n");
		return -1;
	}
	
	scanf("%d", &T);

	for (i = 0; i < T; i++) {
		memset(Output, 0, 1001);
		memset(String, 0, 1001);
		
		scanf("%s", String);
		Solve(String, strlen(String), Output);
		printf("Case #%d: %s\n", i+1, Output);
	}
	free(String);
	free(Output);
	return 0;
}
