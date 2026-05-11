#include <stdio.h>
#include <stdlib.h>

int main() {
    int size = 5;
    int *numbers = (int *)malloc(size * sizeof(int));
    if (numbers == NULL) return 1;

    for (int i = 0; i < size; i++) {
        numbers[i] = i * 10;
        printf("Number %d: %d\n", i, numbers[i]);
    }

    free(numbers);
    return 0;
}