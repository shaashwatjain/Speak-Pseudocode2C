#include<stdio.h>

int main(int argc, char const *argv[])
{
    int a, b;
    printf("Enter base length");
    scanf("%d", &a);
    printf("Enter perpendicular height");
    scanf("%d", &b);
    int result = a * b * 1/2;
    printf("%d\n", result);
    return 0;
}
