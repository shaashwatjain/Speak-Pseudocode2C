/* Write a progrma for multiplication table upto 10 */

#include <stdio.h>
int main()
{
    int num, i;
    printf("Enter an integer: ");
    scanf("%d", &num);

    for (i = 1; i <= 10; ++i)
        printf("%d * %d = %d \n", num, i, num * i);

    return 0;
}

/*
Start the pseudocode
    Initialize num
    Initialize i
    Print "Enter the integer"
    Input num
    for i in range from 1 till 10 increment i
        Print "num, i, num multiply i"
    endfor
End
*/
