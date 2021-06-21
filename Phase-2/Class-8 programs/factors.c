/* Write a program to find all the factors of a number. */

#include<stdio.h>
int main()
{
    int num, i;
    printf("Enter a positive integer: ");
    scanf("%d", &num);
    printf("Factors of %d are: ", num);

    for (i = 1; i <= num; ++i)
    {
        if (num % i == 0)
            printf("%d ", i);
    }
    return 0;
}

/*
    Start the pseudocode
    initialize num
    initialize i
    print "Enter a positive integer"
    input num
    print "Factors of num are"
    for i in range from 1 to num increment i
        if num mod i equal to 0
            print "i"
        endif
    endfor
end
*/
