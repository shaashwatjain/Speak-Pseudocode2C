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

/*
    Start the pseudocode
    initialize current
    print What is the current year
    input current
    assign year = current + 1
    initialize count = 0
    print The next 20 years are
    while count less than 20
        if year mod 4 equal to 0
            if year mod 100 not equal to 0 or year mod 400 equal to zero
                assign count = count + 1
                print variable year
            endif
        endif
        assign year = year + 1
    endwhile
    End
*/
