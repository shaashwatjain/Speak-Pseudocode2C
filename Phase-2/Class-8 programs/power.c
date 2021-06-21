/* Write a program to calculate the power of a numer */
#include<stdio.h>
int main()
{
    int base, exponent;
    int result = 1;
    printf("Enter a base number ");
    scanf("%d", &base);
    printf("Enter an exponent ");
    scanf("%d", &exponent);

    while (exponent != 0)
    {
        result *= base;
        --exponent;
    }

    printf("Answer is %d\n", result);

    return 0;
}

/*
Start the pseudocode
    Initialize base
    Initialize exponent
    set result to 1
    print "Enter the base number"
    input base
    print "Enter the exponent number"
    input exponent
    while exponent not equal to 0
        result multiply equal base
        Decrement exponent
    endwhile
    print "Answer is result"
End
*/
