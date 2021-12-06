#include<stdio.h>

int main()
{
    int number;
    scanf("%d",&number);
    if (number % 13==0)
    {
        printf("The number is divisible by 13\n");
    }
    else
    {
        printf("Number not divisible by 13");
    }
    return 0;
}
