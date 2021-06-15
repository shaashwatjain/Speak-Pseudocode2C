#include<stdio.h>

int main(int argc, char const *argv[])
{
    int num1, num2;
    printf("Enter first number");
    scanf("%d", &num1);
    printf("Enter second number");
    scanf("%d", &num2);
    int sum = num1 / num2; 
    printf("%d\n", sum);
    return 0;
}
