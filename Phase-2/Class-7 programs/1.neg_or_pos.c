#include <stdio.h>
 
int main()
{
    int number;
 
    printf("Enter a number: \n");
    scanf("%d", &number);
    if (number > 0)
    {
        printf("%d is a positive number \n", number);
    }
    else if (number < 0)
    {
        printf("%d is a negative number \n", number);
    }
    else
    {
        printf("0 is neither positive nor negative");
    }
}
