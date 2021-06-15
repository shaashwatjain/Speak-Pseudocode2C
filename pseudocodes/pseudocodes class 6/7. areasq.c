#include<stdio.h>

int main(int argc, char const *argv[])
{
    int side;
    printf("Enter side of square");
    scanf("%d", &side);
    int result = side * side;
    printf("%d\n", result);
    return 0;
}
