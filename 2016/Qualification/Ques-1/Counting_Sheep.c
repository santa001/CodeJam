#include <stdio.h>

void
populate_array(unsigned long long num, int *array, int *sum)
{
	unsigned long long temp = num;
	int val = 0;

	while (temp > 0) {
		val = temp % 10;
		if (0 == array[val]) {
			array[val]++;
			*sum += (val+1);
		}
		temp /= 10;
	}
}


unsigned long long
solve(unsigned long long num)
{
	int array[10] = {0};
	int sum = 0;
	int max_iteration = 100000;
	int mul = 0;

	if (num == 0) {
		return 0;
	}

	while ((sum < 55) && (++mul < max_iteration)) {
		populate_array((num * mul), array, &sum);
	}

	if (sum != 55) {
		return 0;
	} else {
		return (mul*num);
	}
}


int
main(void)
{
	int i = 0;
	int T;
	unsigned long long N;
	unsigned long long Num;

	scanf("%d", &T);

	for (i = 0; i < T; i++) {
		scanf("%llu", &N);
		Num = solve(N);
		if (Num == 0) {
			printf("Case #%d: INSOMNIA\n", (i+1));
		} else {
			printf("Case #%d: %llu\n", (i+1), Num);
		}
	}
}

