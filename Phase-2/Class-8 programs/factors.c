/* Write a program to find all the factors of a number. */

#include<stdio.h>
int main()
{
    int number, i;
    printf("Enter a positive integer: ");
    scanf("%d", &number);
    printf("Factors of %d are: ", number);

    for(i = 1; i <= number; i++)
    {
        if(number % i == 0)
            printf("%d ", i);
    }

    return 0;
}

/*
    Start the pseudocode
    declare number
    declare i
    print Enter a positive integer
    input number
    print Factors of number are
    for i in range from 1 till number
        if number mod i equals 0
            print variable i
        endif
    endfor
    end
*/
