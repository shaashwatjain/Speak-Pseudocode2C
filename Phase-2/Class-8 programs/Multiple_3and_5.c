/* Problem3) Write the program such that only multiples of three or five are considered in the sum, e.g. 3, 5, 6, 9, 10, 12, 15 for n=17 */

#include<stdio.h>
#include<string.h>

int main()
{
    int num;
    printf("Enter the number till you need to compute sum");
    scanf("%d", &num);
    int total = 0;

    for(int i = 0; i <= num; i++)
        if(i % 3 == 0 || i % 5 == 0)
            total += i;

    printf("The sum of the number is %d\n", total);
    return 0;
}

/*
Start the pseudocode
    initialize num
    print "Enter the number till you need to compute sum"
    read num
    initialize total equal to 0
    for i in range from 0 till num increment i
        if i mod 3 is zero or i mod 5 is zero
            total plus equal to i
        endif
    endfor
    print the sum of number is total
End
*/
