#include <stdio.h>
int main()
{
    int first, second, temp;
    printf("Enter First Number: ");
    scanf("%d", &first);

    printf("Enter Second Number: ");
    scanf("%d",&second);

    printf("Before swapping:\n");
    printf("number 1 is: %d and number 2 is: %d\n", first, second);
    
    temp = first;
    
    first = second;
    second = temp;

    printf("After swapping:\n");
    printf("number 1 is: %d and number 2 is: %d", first, second);
    return 0;
}
