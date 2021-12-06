#include <stdio.h>
int main() 
{
    int first, second;
    printf("Enter two integers: ");
    scanf("%d", &first);
    scanf("%d", &second);

    if (first >= second) 
    {
      if (first == second) 
      {
        printf("%d = %d",first,second);
      }
      else 
      {
        printf("%d > %d", first, second);
      }
    }
    else 
    {
        printf("%d < %d",first, second);
    }

    return 0;
}
