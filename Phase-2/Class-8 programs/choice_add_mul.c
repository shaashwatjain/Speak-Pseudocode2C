/* Problem3) Write a program that asks the user for a number n and gives them the possibility to choose between computing the sum and computing the product of 1,…,n.*/

#include<stdio.h>
#include<string.h>

int main()
{
    int num;
    printf("Enter the number ");
    scanf("%d", &num);

    int choice;
    printf("1. To computer sum\n2. To compute product\nEnter the choice: ");
    scanf("%d", &choice);

    int total = 0;

    if(choice == 2)
        total = 1;

    for(int i = 1; i <= num; i++)
        if(choice == 1)
            total += i;
        else
            total *= i;

    printf("The result is %d\n", total);
    return 0;
}

/*
    Start the pseudocode
    initialize num
    read num
    initalize choice
    Print "1. To compute sum 2. To compute product"
    input choice
    set total to 0
    if choice equals 2
        set total to 1
    endif
    for i in range from 1 till num increment i
        if choice equal 1
            total plus equal i
        endif
        else
            total multiply equal i
        endelse
    endfor
    print the result is total
    End
*/
