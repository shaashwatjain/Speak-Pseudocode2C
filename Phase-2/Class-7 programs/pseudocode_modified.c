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
print "Enter a number"
read num
if num > 0
print num is a positive number
endif
elseif num < 0
print num is a negative number
end elseif
else
print "0 is neither positive nor negative"
end else
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
endif
else
print Number not divisible by 13
end else
return 0
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
print "number is even"
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
print "Number equals 0"
else if number = 50
print "Number equals 50"
end elseif
else if number = 100
print "Number equals 100"
end elseif
else 
print "Number not equals 0,50 or 100"
end else
return 0
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
intialize integer number1
intialize integer number2
print "Enter two integers"
read number1
read number2
if number1 >= number2
if number1 = number2
print Result number1=number2
endif
else
print Result number1>number2
end else
endif
else
print Result number1<number2
end else
return 0
end program

Write a program to calculate the power of a number.

#include <math.h>
#include <stdio.h>

int main() {
    double base, exp, result;
    printf("Enter a base number: ");
    scanf("%lf", &base);
    printf("Enter an exponent: ");
    scanf("%lf", &exp);

    // calculates the power
    result = pow(base, exp);

    printf("%.1lf^%.1lf = %.2lf", base, exp, result);
    return 0;
}

start the program
include math.h 
declare double base
declare double exp
declare double result
print Enter a base number
read base
print Enter an exponent
read exp
initialize result to pow(base,exp)
print base,exp,result
return 0

Write a program to chech if a character is a vowel or a consonant.

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
set boolean isvowel to false
print "Enter an alphabet"
read ch
if ch=a or ch=A or ch=e or ch=E or ch=i or ch=I
or ch=o or ch= O or ch=u or ch=U
set isvowel to true
endif
if isvowel=true 
print "ch is a vowel"
endif
else
print "ch is a consonant"
end else
return 0
end program

Write a program to return the ASCII value of a character.

#include <stdio.h>
int main()
{
    char ch;
    printf("Enter any character:");

    scanf("%c", &ch);

    printf("ASCII value of character %c is: %d", ch, ch);
    return 0;
}

start the program
declare char ch
print "Enter and character"
read ch
print ""
return 0
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
endif
else
print y is not leap year
end else
endif
else 
print y is a leap year
end else
endif
else
print y is not a leap year
end else
return 0

Write a program to check if the entered integer is a perfect square or not.

#include <stdio.h>
#include <math.h>
int main()
{
int num;
int iVar;
float fVar;
printf("Enter an integer number: ");
scanf("%d",&num);
fVar=sqrt((double)num);
iVar=fVar;
if(iVar==fVar)
printf("%d is a perfect square.",num);
else
printf("%d is not a perfect square.",num);
return 0;
}

start the program
include math.h
declare integer num
declare integer ivar
declare float fvar
print Enter an integer number
read num
initialize fvar to square root of 
set ivar to fvar
if ivar = fvar
print num is a perfect square
endif
else
print num is not a perfect square
end else
return 0 
end program

*/







