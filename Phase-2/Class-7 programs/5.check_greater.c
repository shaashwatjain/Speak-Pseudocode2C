#include <stdio.h>
int main() 
{
    int a, b;
    printf("Enter two integers: ");
    scanf("%d", &a);
    scanf("%d", &b);

    if (a >= b) 
    {
      if (a == b) 
      {
        printf("%d = %d",a,b);
      }
      else 
      {
        printf("%d > %d", a, b);
      }
    }
    else 
    {
        printf("%d < %d",a, b);
    }

    return 0;
}
