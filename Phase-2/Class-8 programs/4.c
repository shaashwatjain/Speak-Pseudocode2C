/* Problem3) Write a program that asks the user for a number n and gives them the possibility to choose between computing the sum and computing the product of 1,…,n.*/

#include<stdio.h>
#include<string.h>

int main()
{
    int n;
    scanf("%d", &n);

    int choice;
    printf("1. To computer sum\n2. To compute product\nEnter the choice: ");
    scanf("%d", &choice);

    int total = 0;

    if(choice == 2)
        total = 1;

    for(int i = 1; i <= n; i++)
        if(choice == 1)
            total += i;
        else
            total *= i;

    printf("The result is %d\n", total);
    return 0;
}

/*
    Pseudocode:-
    Start the pseudocode
    read a number
    initialize total equal to 0
    for i in range of n
        if i mod 3 is zero or i mod 5 is zero
            add i to total
        endif
    endfor
    print the sum of number is total
    End
*/
