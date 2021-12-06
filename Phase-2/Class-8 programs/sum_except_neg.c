/* Write a program to calculate the sum of numbers, If the user enters a negative number, it's not added to the result */

#include <stdio.h>
int main()
{
    int number;
    int value;
    printf("Enter the number of integer to consider for sum\n");
    scanf("%d", &number);
    int sum = 0;

    for(int i = 1; i <= number; ++i)
    {
        printf("Enter a number %d: ", i);
        scanf("%d", &value);

        if(value < 0)
        {
            continue;
        }
        sum += value;
    }

    printf("Sum is %d\n", sum);
    return 0;
}
