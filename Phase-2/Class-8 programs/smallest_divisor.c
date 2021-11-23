/* Write a program which calculates the smallest divisor of a number. */

#include<stdio.h>
int main()
{
    int number;
    int i = 2;
    printf("Enter the number to find the smallest divisor\n");
    scanf("%d", &number);

    while(i <= number)
    {
        if(number % i == 0)
        {
            printf("The smallest number is %d\n", i);
            break;
        }

        i++;
    }

    return 0;
}
