
#include <stdio.h>
#include <stdlib.h>
#include <math/fibonacci.h>

#define LIMIT 4000000 // 4 million

int solve(void) {
  size_t count = 0;
  int* fibonacci_numbers = fibonacci_limit(LIMIT, &count);
  if (NULL == fibonacci_numbers) {
    printf("unable to get %d fibonacci numbers!\n", LIMIT);
    return -1;
  }

  int sum = 0;
  int n;

  for (size_t i = 0; i < count; i++) {
    n = fibonacci_numbers[i];
    if (n % 2 == 0) {
      sum += n;
    }
  }

  free(fibonacci_numbers);

  return sum;
}


int main(void) {
  printf("%d\n", solve());
  return 0;
}
