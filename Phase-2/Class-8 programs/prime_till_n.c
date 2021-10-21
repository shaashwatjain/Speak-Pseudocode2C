/* Write a program that prints all prime numbers. (Note: if your programming language does not support arbitrary size numbers, printing all primes up to the number n */

#include <stdio.h>
int main()
{
    int num, i = 3, count, c;

    printf("Enter the number of prime numbers to print till\n");
    scanf("%d", &num);

    if(num >= 1)
    {
        printf("First %d prime numbers are:\n", num);
        printf("2\n");
    }

    for(count = 2; count <= num;)
    {
        for(c = 2; c <= i - 1; c++)
        {
            if(i % c == 0)
                break;
        }

        if(c == i)
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
    declare num
    declare count
    declare c
    initialize i = 3
    print Enter the number of prime number to prill till
    input num
    If nums greater than equal to 1
        print First num prime number are
      print 2
    endif
    for count in range from 2 till count less than equal to num no update
        for c in range from 2 till c less than equal to i - 1 increment by 1
            if i mod c equal to 0
                break
            endif
        endfor
        if c equal to i
            Print variable i
            assign count = count + 1
        endif
        assign i = i + 1
    endfor
    End
*/
