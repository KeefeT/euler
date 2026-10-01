
#include <stdio.h>

#define LIMIT 1000

int solve(void) {
  int sum = 0;
  for (int i = 1; i < LIMIT; i++) {
    if ((i % 3 == 0) || (i % 5 == 0)) {
      sum += i;
    }
  }

  return sum;
}


int main(void) {
  printf("%d\n", solve());
  return 0;
}
