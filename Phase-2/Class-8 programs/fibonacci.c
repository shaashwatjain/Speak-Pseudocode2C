#include <stdio.h>
int main()
{
    int number;
    // initialize first and second terms
    int first = 0;
    int second = 1;
    // initialize the next term (3rd term)
    int next = first + second;
    // get no. of terms from user
    printf("Enter the number of terms\n");
    scanf("%d", &number);
    // print the two terms first and second
    printf("Fibonacci Series\n");
    printf("%d\n", first);
    printf("%d\n", second);

    // print 3rd to nth terms
    for(int i = 3; i <= number; ++i)
    {
        printf("%d\n", next);
        first = second;
        second = next;
        next = first + second;
    }

    return 0;
}
