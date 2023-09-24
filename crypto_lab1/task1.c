#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define KEYSIZE 16

void main(){
    int i;
    char key[KEYSIZE];
    printf("%lld", (long long) time(NULL));

    // srand(time(NULL));
    for(int i=0; i<KEYSIZE; i++){
        key[i] = rand()%256;
        printf("%.2x\n", (unsigned char)key[i]);
    }
    printf("\n");
}

/**
in C srand is usally called before rand to create random value
because the default seed in rand() is 1. So we have to call srand() to give
a seed to rand()
*/