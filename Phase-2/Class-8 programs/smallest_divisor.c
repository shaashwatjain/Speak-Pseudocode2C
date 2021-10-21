/* Write a program divisor.py which calculates the smallest divisor of a number. */

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

/*
    Start the pseudocode
    declare number
    initialize i = 2
    print Enter the number to find the smallest divisor
    input number
    while i less than equal to number
        if number mod i equal to 0
            print The smallest number is variable i
            break
        endif
        assign i = i + 1
    endwhile
    end
*/
