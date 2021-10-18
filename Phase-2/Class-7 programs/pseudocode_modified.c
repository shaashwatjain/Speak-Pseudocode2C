/*
Write a program to find if a number is positive or negative.
#include <stdio.h>
 
void main()
{
    int num;
 
    printf("Enter a number: \n");
    scanf("%d", &num);
    if (num > 0)
        printf("%d is a positive number \n", num);
    else if (num < 0)
        printf("%d is a negative number \n", num);
    else
        printf("0 is neither positive nor negative");
}

start the program
declare integer num
print Enter a number
read num
if num > 0
    print num is a positive number
else if num < 0
    print num is a negative number
else
    print 0 is neither positive nor negative
end if
end program

Write a program to check if a number is divisible by 13 or not.

#include<stdio.h>
int main(){
    int num;
    scanf("%d",&num);
    if (num % 13==0)
    {
        printf("The number is divisible by 13\n");
    }
    else
        printf("Number not divisible by 13");
    return 0;
}

start the program
declare integer num
read num
if num%13 = 0
print The number is divisible ny 13
else
print Number not divisible by 13
end if
end program

Write a program to check if a number is even or not

#include<stdio.h>
int main(){
int number=0;
printf("Enter a number:");
scanf("%d",&number);
if(number%2==0){
printf("number is even");
}
return 0;
}

start the program
set integer number to 0
print Enter a number
read number
if number % 2 = 0
    print number is even
endif
return 0
end program

Write a program to check if a number is 0,50 or 100.

#include<stdio.h>
int main(){
int number=0;
printf("enter a number:");
scanf("%d",&number);
if(number==10){
printf("number is equals to 10");
}
else if(number==50){
printf("number is equal to 50");
}
else if(number==100){
printf("number is equal to 100");
}
else{
printf("number is not equal to 10, 50 or 100");
}
return 0;
}

start the program
set integer number to 0
print "Enter a number"
read number
if number = 0
    print Number equals 0
else if number = 50
    print Number equals 50
else if number = 100
    print Number equals 100
else
    print Number not equals 0,50 or 100
end if
end program

Write a program to input two numbers and check which one is greater.

#include <stdio.h>
int main() {
    int number1, number2;
    printf("Enter two integers: ");
    scanf("%d %d", &number1, &number2);

    if (number1 >= number2) {
      if (number1 == number2) {
        printf("Result: %d = %d",number1,number2);
      }
      else {
        printf("Result: %d > %d", number1, number2);
      }
    }
    else {
        printf("Result: %d < %d",number1, number2);
    }

    return 0;
}

start the program
declare integer number1
declare integer number2
print "Enter two integers"
read number1
read number2
if number1 >= number2
    if number1 = number2
        print Result number1 = number2
    else
        print Result number1 > number2
    end if
else
    print Result number1 < number2
end if
end program

Write a program to check if a character is a vowel or a consonant.

#include <stdio.h>
int main()
{
    char ch;
    bool isVowel = false;

    printf("Enter an alphabet: ");
    scanf("%c",&ch);

    if(ch=='a'||ch=='A'||ch=='e'||ch=='E'||ch=='i'||ch=='I'
    		||ch=='o'||ch=='O'||ch=='u'||ch=='U')
    {
    	isVowel = true;

    }
    if (isVowel == true)
        printf("%c is a Vowel", ch);
    else
        printf("%c is a Consonant", ch);
    return 0;
}

start the program
initialize character ch
print "Enter an alphabet"
read ch
if ch=a or ch=A or ch=e or ch=E or ch=i or ch=I
or ch=o or ch= O or ch=u or ch=U
    print vowel
else
    print not a vowel
end program


Write a program to check if the input year is a leap year.
int main()
{
    int y;

    printf("Enter year: ");
    scanf("%d",&y);

    if(y % 4 == 0)
    {
        if( y % 100 == 0)
        {
            if ( y % 400 == 0)
                printf("%d is a Leap Year", y);
            else
                printf("%d is not a Leap Year", y);
        }
        else
            printf("%d is a Leap Year", y );
    }
    else
        printf("%d is not a Leap Year", y);

    return 0;
}

start the program
declare integer y
print "Enter year"
read y
if y%4=0
    if y%100 =0
        if y%400 = 0
            print y is leap year
        else
            print y is not leap year
        end if
    else
        print y is a leap year
    end if
else
    print y is not a leap year
end if
return 0

