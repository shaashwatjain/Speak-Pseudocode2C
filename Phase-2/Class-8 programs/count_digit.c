/* Write a program to count number of digits in a integer */
#include<stdio.h>
int main()
{
    int number;
    int count = 0;
    printf("Enter an integer: ");
    scanf("%d", &number);

    while(number != 0)
    {
        number /= 10;
        ++count;
    }

    printf("Number of digits: %d\n", count);

    return 0;
}

/*
    Start the pseudocode
    Initialize number
    initialize count = 0
    print Enter an integer
    input number
    while number not equal to 0
        assign number = number / 10
        assign count = count + 1
    endwhile
    print Number of digits is variable count
    End
*/
