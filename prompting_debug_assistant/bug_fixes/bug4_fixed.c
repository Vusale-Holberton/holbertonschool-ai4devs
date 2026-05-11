#include <stdio.h>
#include <stdlib.h>

int main() {
    int size = 10;
    int *array = (int *)malloc(size * sizeof(int));
    
    if (array == NULL) {
        return 1;
    }

    for (int i = 0; i < size; i++) {
        array[i] = i * 100;
        printf("Index %d: %d\n", i, array[i]);
    }

    printf("Array processing finished.\n");
    
    free(array);
    return 0;
}