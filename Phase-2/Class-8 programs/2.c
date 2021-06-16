/* Problem2) Write a program that asks the user for a number n and prints the sum of the numbers 1 to n */

#include<stdio.h>
#include<string.h>

int main() {
    int n;
    scanf("%d", &n);
    int total = 0;

    for (int i = 0; i <= n; i++)
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
        add i to total
    endfor
    print the sum of number is total
    End
*/
