alpha [a-zA-Z]
digit [0-9]
alnum [a-zA-Z0-9]
%{
#include <stdio.h>
#include <string.h>
char a[500];
int i;
%}
%%
[iI]f[ ]{alpha}+[ ]is[ ]greater[ ]than[ ]or[ ]equal[ ]to[ ]{alnum}+[\n] {
printf("if(");
for(i=3;yytext[i]!=' ';i++)
{
printf("%c",yytext[i]);
}
printf(">=");
for(i=yyleng-1;i>=0;i--)
{
if(yytext[i]==' '&&yytext[i-1]=='o'&&yytext[i-2]=='t')
{
break;
}
}
i++;
for(;yytext[i]!='\n';i++)
{
printf("%c",yytext[i]);
}
printf(")\n{\n");
}


[iI]f[ ]{alpha}+[ ]is[ ]lesser[ ]than[ ]or[ ]equal[ ]to[ ]{alnum}+[\n] {
printf("if(");
for(i=3;yytext[i]!=' ';i++)
{
printf("%c",yytext[i]);
}
printf("<=");
for(i=yyleng-1;i>=0;i--)
{
if(yytext[i]==' '&&yytext[i-1]=='o'&&yytext[i-2]=='t')
{
break;
}
}
i++;
for(;yytext[i]!='\n';i++)
{
printf("%c",yytext[i]);
}
printf(")\n{\n");
}



[iI]f[ ]{alpha}+[ ]is[ ]greater[ ]than[ ]{alnum}+[\n] {
printf("if(");
for(i=3;yytext[i]!=' ';i++)
{
printf("%c",yytext[i]);
}
printf(">");
for(i=yyleng-1;i>=0;i--)
{
if(yytext[i]==' '&&yytext[i-1]=='n'&&yytext[i-2]=='a')
{
break;
}
}
i++;
for(;yytext[i]!='\n';i++)
{
printf("%c",yytext[i]);
}
printf(")\n{\n");
}

[iI]f[ ]{alpha}+[ ]is[ ]lesser[ ]than[ ]{alnum}+[\n] {
printf("if(");
for(i=3;yytext[i]!=' ';i++)
{
printf("%c",yytext[i]);
}
printf("<");
for(i=yyleng-1;i>=0;i--)
{
if(yytext[i]==' '&&yytext[i-1]=='n'&&yytext[i-2]=='a')
{
break;
}
}
i++;
for(;yytext[i]!='\n';i++)
{
printf("%c",yytext[i]);
}
printf(")\n{\n");
}

[iI]f[ ]{alpha}+[ ]is[ ]equal[ ]to[ ]{alnum}+[\n] {
printf("if(");
for(i=3;yytext[i]!=' ';i++)
{
printf("%c",yytext[i]);
}
printf("==");
for(i=yyleng-1;i>=0;i--)
{
if(yytext[i]==' '&&yytext[i-1]=='o'&&yytext[i-2]=='t')
{
break;
}
}
i++;
for(;yytext[i]!='\n';i++)
{
printf("%c",yytext[i]);
}
printf(")\n{\n");
}

[iI]f[ ]{alpha}+[ ]is[ ]not[ ]equal[ ]to[ ]{alnum}+[\n] {
printf("if(");
for(i=3;yytext[i]!=' ';i++)
{
printf("%c",yytext[i]);
}
printf("!=");
for(i=yyleng-1;i>=0;i--)
{
if(yytext[i]==' '&&yytext[i-1]=='o'&&yytext[i-2]=='t')
{
break;
}
}
i++;
for(;yytext[i]!='\n';i++)
{
printf("%c",yytext[i]);
}
printf(")\n{\n");
}

[Ww]hile[ ]{alpha}+[ ]is[ ]greater[ ]than[ ]or[ ]equal[ ]to[ ]{alnum}+[\n] {
printf("while(");
for(i=6;yytext[i]!=' ';i++)
{
printf("%c",yytext[i]);
}
printf(">=");
for(i=yyleng-1;i>=0;i--)
{
if(yytext[i]==' '&&yytext[i-1]=='o'&&yytext[i-2]=='t')
{
break;
}
}
i++;
for(;yytext[i]!='\n';i++)
{
printf("%c",yytext[i]);
}
printf(")\n{\n");
}


[Ww]hile[ ]{alpha}+[ ]is[ ]lesser[ ]than[ ]or[ ]equal[ ]to[ ]{alnum}+[\n] {
printf("while(");
for(i=6;yytext[i]!=' ';i++)
{
printf("%c",yytext[i]);
}
printf("<=");
for(i=yyleng-1;i>=0;i--)
{
if(yytext[i]==' '&&yytext[i-1]=='o'&&yytext[i-2]=='t')
{
break;
}
}
i++;
for(;yytext[i]!='\n';i++)
{
printf("%c",yytext[i]);
}
printf(")\n{\n");
}



[Ww]hile[ ]{alpha}+[ ]is[ ]greater[ ]than[ ]{alnum}+[\n] {
printf("while(");
for(i=6;yytext[i]!=' ';i++)
{
printf("%c",yytext[i]);
}
printf(">");
for(i=yyleng-1;i>=0;i--)
{
if(yytext[i]==' '&&yytext[i-1]=='n'&&yytext[i-2]=='a')
{
break;
}
}
i++;
for(;yytext[i]!='\n';i++)
{
printf("%c",yytext[i]);
}
printf(")\n{\n");
}

[Ww]hile[ ]{alpha}+[ ]is[ ]lesser[ ]than[ ]{alnum}+[\n] {
printf("while(");
for(i=6;yytext[i]!=' ';i++)
{
printf("%c",yytext[i]);
}
printf("<");
for(i=yyleng-1;i>=0;i--)
{
if(yytext[i]==' '&&yytext[i-1]=='n'&&yytext[i-2]=='a')
{
break;
}
}
i++;
for(;yytext[i]!='\n';i++)
{
printf("%c",yytext[i]);
}
printf(")\n{\n");
}

[Ww]hile[ ]{alpha}+[ ]is[ ]equal[ ]to[ ]{alnum}+[\n] {
printf("while(");
for(i=6;yytext[i]!=' ';i++)
{
printf("%c",yytext[i]);
}
printf("==");
for(i=yyleng-1;i>=0;i--)
{
if(yytext[i]==' '&&yytext[i-1]=='o'&&yytext[i-2]=='t')
{
break;
}
}
i++;
for(;yytext[i]!='\n';i++)
{
printf("%c",yytext[i]);
}
printf(")\n{\n");
}

[Ww]hile[ ]{alpha}+[ ]is[ ]not[ ]equal[ ]to[ ]{alnum}+[\n] {
printf("while(");
for(i=6;yytext[i]!=' ';i++)
{
printf("%c",yytext[i]);
}
printf("!=");
for(i=yyleng-1;i>=0;i--)
{
if(yytext[i]==' '&&yytext[i-1]=='o'&&yytext[i-2]=='t')
{
break;
}
}
i++;
for(;yytext[i]!='\n';i++)
{
printf("%c",yytext[i]);
}
printf(")\n{\n");
}



endwhile[\n] {
printf("}\n");
}




[Ii]nitialize[ ]{alnum}+[ ]to[ ]{alnum}+[\n] {
printf("int ");
for(i=11;yytext[i]!=' ';i++)
{
printf("%c",yytext[i]);
}
printf("=");
for(i=yyleng-1;i>=0;i--)
{
if(yytext[i]==' '&&yytext[i-1]=='o'&&yytext[i-2]=='t')
{
break;
}
}
i++;
for(;yytext[i]!='\n';i++)
{
printf("%c",yytext[i]);
}
printf(";\n");
}

else[\n] {
printf("}\nelse\n{\n");
}
endif[\n] {
printf("}");
}

[Pp]rint[ ]["]{alnum}+["][\n] {
printf("printf(\"");
for(i=7;yytext[i]!='"';i++)
{
printf("%c",yytext[i]);
}
printf("\");\n");
}

[Ss]et[ ]{alnum}+[ ]to[ ]{alnum}+[\n] {
for(i=4;yytext[i]!=' ';i++)
{
printf("%c",yytext[i]);
}
printf("=");
for(i=yyleng-1;i>=0;i--)
{
if(yytext[i]==' '&&yytext[i-1]=='o'&&yytext[i-2]=='t')
{
break;
}
}
i++;
for(;yytext[i]!='\n';i++)
{
printf("%c",yytext[i]);
}
printf(";\n");
}

[Aa]dd[ ]{alnum}+[ ]to[ ]{alnum}+[\n] {
for(i=yyleng-1;i>=0;i--)
{
if(yytext[i]==' '&&yytext[i-1]=='o'&&yytext[i-2]=='t')
{
break;
}
}
i++;
while(yytext[i]!='\n')
{
printf("%c",yytext[i]);
i++;
}
printf("+=");
for(i=4;yytext[i]!=' ';i++)
{
printf("%c",yytext[i]);
}
printf(";\n");
}
%%


int yywrap(void)
{
    return 1;
}

int main()
{

 yyin=fopen("inp.txt","r");

 yylex();
 return 0;
}

int yyerror(char *s)
{
 return 1;
}
