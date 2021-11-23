/* Write a program to calculate the power of a numer */

#include<stdio.h>
int main()
{
    int base, exponent;
    int result = 1;
    printf("Enter a base number ");
    scanf("%d", &base);
    printf("Enter an exponent ");
    scanf("%d", &exponent);

    while(exponent != 0)
    {
        result *= base;
        --exponent;
    }

    printf("Answer is %d\n", result);

    return 0;
}
