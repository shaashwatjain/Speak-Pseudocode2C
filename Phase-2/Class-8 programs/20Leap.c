/* Write a program that prints the next 20 leap years */
#include<stdio.h>
int main()
{
    int current;
    printf("What is the current year\n");
    scanf("%d", &current);
    int year = current + 1;
    int count = 0;
    printf("The next 20 leap years are\n");

    while(count < 20)
    {
        if(year % 4 == 0)
        {
            if(year % 100 != 0 || year % 400 == 0)
            {
                ++count;
                printf("%d\n", year);
            }
        }

        ++year;
    }

    return 0;
}
