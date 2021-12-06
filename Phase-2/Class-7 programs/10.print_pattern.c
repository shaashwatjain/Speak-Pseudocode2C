#include <stdio.h>
int main() 
{
   int first, second, rows;
   printf("Enter the number of rows: ");
   scanf("%d", &rows);
   for (first = 1; first <= rows; ++first) 
   {
      for (second = 1; second <= first; ++second) 
      {
         printf(1);
      }
      printf("\n");
   }
   return 0;
}
