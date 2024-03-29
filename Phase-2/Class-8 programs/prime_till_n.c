/* Write a program that prints all prime numbers. (Note: if your programming language does not support arbitrary size numbers, printing all primes up to the number n */

#include <stdio.h>
int main()
{
    int num, i = 3, count, c;

    printf("Enter the number of prime numbers to print till\n");
    scanf("%d", &num);

    if (num >= 1)
    {
        printf("First %d prime numbers are:\n", num);
        printf("2\n");
    }

    for (count = 2; count <= num;)
    {
        for (c = 2; c <= i - 1; c++)
        {
            if (i % c == 0)
                break;
        }

        if (c == i)
        {
            printf("%d\n", i);
            count++;
        }

        i++;
    }

    return 0;
}


/*
start the pseudocode
    Initialize num
    Initialize count
    Initialize c
    Set i to 3
    Print "Enter the number of prime number to prill till"
    Input num
    If nums greater than equal to 1
      Print "First num prime number are"
      print "2"
    endif
    for count in range from 2 until count less than equal to num
        for c in range from 2 until c less than equal to i-1 increment c
            if i mod c eual to 0
                break
            endif
        endfor
        if c equal to i
            Print "i"
            increment count
        endif
        increment i
    endfor
End
*/
