/* Problem2) Write a program that asks the user for a number n and gives them the possibility to choose between computing the sum and computing the product of 1,…,n.*/

#include<stdio.h>
#include<string.h>

int main()
{
    int number;
    printf("Enter the number ");
    scanf("%d", &number);

    int choice;
    printf("1. To computer sum\n2. To compute product\nEnter the choice: ");
    scanf("%d", &choice);

    int total = 0;

    if(choice == 2)
        total = 1;

    for(int i = 1; i <= number; i++)
        if(choice == 1)
            total += i;
        else
            total *= i;

    printf("The result is %d\n", total);
    return 0;
}
