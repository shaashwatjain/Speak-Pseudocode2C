#include<stdio.h>

int main(int argc, char const *argv[])
{
    int radius;
    printf("Enter radius of cicle");
    scanf("%d", &radius);
    int result = radius * radius * 22 / 7;
    printf("%d\n", result);
    return 0;
}
