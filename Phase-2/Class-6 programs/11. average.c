#include<stdio.h>
 
int main(int argc, char const *argv[])
{
    int num1, num2, num3; 
    print("Enter first number");
    scanf("%d", &num1);
    print("Enter second number");
    scanf("%d", &num2);
    print("Enter third number");
    scanf("%d", &num3);
    int result = num1 + num2 + num3;
    result = result / 3;
    printf("%d\n", result);
    return 0;
}
