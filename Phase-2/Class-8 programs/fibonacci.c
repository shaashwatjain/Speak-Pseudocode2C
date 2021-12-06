#include <stdio.h>
int main()
{
    int number;
    // initialize first and second terms
    int a = 0;
    int value = 1;
    // initialize the next term (3rd term)
    int next = a + value;
    // get no. of terms from user
    printf("Enter the number of terms\n");
    scanf("%d", &number);
    // print the first two terms a and value
    printf("Fibonacci Series\n");
    printf("%d\n", a);
    printf("%d\n", value);

    // print 3rd to nth terms
    for(int i = 3; i <= number; ++i)
    {
        printf("%d\n", next);
        a = value;
        value = next;
        next = a + value;
    }

    return 0;
}
