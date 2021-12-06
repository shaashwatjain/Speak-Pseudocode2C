#include <stdio.h>
int main()
{
    int n, count, sum;

    printf("Enter the value of n\n");
    scanf("%d",&n);

    for(count=1; count <= n; count++)
    {
        sum = sum + count;
    }

    printf("Sum of first %d natural numbers is: %d",n, sum);

    return 0;
}
