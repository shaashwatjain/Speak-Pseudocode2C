/* Problem3) Write the program such that only multiples of three or five are considered in the sum, e.g. 3, 5, 6, 9, 10, 12, 15 for n=17 */

#include<stdio.h>
#include<string.h>

int main()
{
    int number;
    printf("Enter the number till you need to compute sum: ");
    scanf("%d", &number);
    int total = 0;

    for(int i = 0; i <= number; i++)
        if(i % 3 == 0 || i % 5 == 0)
            total += i;

    printf("The sum of the number is %d\n", total);
    return 0;
}

/*
    Start the pseudocode
    declare number
    print Enter the number till you need to compute sum
    input number
    initialize total = 0
    for i in range from 0 till number increment by 1
        if i mod 3 is zero or i mod 5 is zero
            assign total = total + i
        endif
    endfor
    print the sum of number is variable total
    End
*/
