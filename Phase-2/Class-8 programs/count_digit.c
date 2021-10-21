/* Write a program to count number of digits in a integer */
#include<stdio.h>
int main()
{
    int num;
    int count = 0;
    printf("Enter an integer: ");
    scanf("%d", &num);

    while (num != 0)
    {
        num /= 10;
        ++count;
    }

    printf("Number of digits: %d\n", count);

    return 0;
}

/*
Start the pseudocode
    Initialize num
    initialize count = 0
    print Enter an integer
    input num
    while num not equal to 0
        assign num = num / 10
        assign count = count + 1
    endwhile
    print Number of digits is variable count
End
*/
