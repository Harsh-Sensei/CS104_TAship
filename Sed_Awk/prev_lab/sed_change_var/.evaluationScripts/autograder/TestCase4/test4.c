#include<stdio.h>
void util(int *,int *);
int main()
{

    int number1,number2;
    scanf("%d",&number1);
    scanf("%d",&number2);
    util(&number1,&number2);
    ++(--number1);
    ++number2;    
    return 0;
}

void util(int *number1,int *number2)
{
    int tmp;
    tmp = *number1;
    *number1=*number2;
    *number2=tmp;
}
