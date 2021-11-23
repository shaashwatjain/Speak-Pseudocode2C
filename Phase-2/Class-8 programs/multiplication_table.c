/* Write a progrma for multiplication table upto 10 */

#include <stdio.h>
int main()
{
    int number, i;
    printf("Enter an integer: ");
    scanf("%d", &number);

    for(i = 1; i <= 10; i++)
        printf("%d * %d = %d \n", number, i, number * i);

    return 0;
}
