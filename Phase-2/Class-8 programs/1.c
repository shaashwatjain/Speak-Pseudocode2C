 // Program1) Modify the previous program such that only the users Alice and Bob are greeted with their names.

#include<stdio.h>
#include<string.h>

int main()
{
    char name1[100];
    char name2[100];
    scanf("%[^\n]%*c", name1);
    scanf("%[^\n]%*c", name2);

    if(!strcmp(name1, "Alice"))
        printf("Welcome %s\n", name1);

    if(!strcmp(name2, "Bob"))
        printf("Welcome %s\n", name2);

    return 0;
}

/*
Pseudocode:-
Start the pseudocode
    read first name
    read second name
    if first name is Alice then
        print Welcome Alice
    endif
    if second name is Bob then
        print Welcome Bob
    endif
End
*/
