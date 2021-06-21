/* Write a program divisor.py which calculates the smallest divisor of a number. */

#include<stdio.h>
int main()
{
    int num;
    int i=2;
    printf("Enter the number to find the smallest divisor\n");
    scanf("%d", &num);
    while(i <= num)
    {
        if(num % i == 0)
        {
            printf("The smallest number is %d\n", i);
            break;
        }

        i++;
    }
    return 0;
}

/*
Start the pseudocode
    initialize num
    set i to 2
    print "Enter the number to find the smallest divisor"
    input num
    while i less than equal to num
        if num mod i equal to 0
            print "The smallest number is i"
            break
        endif
        Increment i
    endwhile
end
*/
