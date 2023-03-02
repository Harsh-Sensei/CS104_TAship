#include "stdio.h"
int x=2, y=5;

int main(int argc, char* argv[])
{
    printf("x : %d, y : %d\n", x, y);
    increment();
    printf("x : %d, y : %d\n", x, y);
}
