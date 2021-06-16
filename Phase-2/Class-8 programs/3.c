/* Problem3) Modify the previous program such that only multiples of three or five are considered in the sum, e.g. 3, 5, 6, 9, 10, 12, 15 for n=17 */

#include<stdio.h>
#include<string.h>

int main()
{
    int n;
    scanf("%d", &n);
    int total = 0;

    for(int i = 0; i <= n; i++)
        if(i % 3 == 0 || i % 5 == 0)
            total += i;

    printf("The sum of the number is %d\n", total);
    return 0;
}

/*
    Pseudocode:-
    Start the pseudocode
    read a number
    initialize total equal to 0
    for i in range of n+1
        if i mod 3 is zero or i mod 5 is zero
            add i to total
        endif
    endfor
    print the sum of number is total
    End
*/
