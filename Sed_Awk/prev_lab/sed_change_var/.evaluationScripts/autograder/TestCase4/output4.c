#include<stdio.h>
void util(int *,int *);
int main()
{

    int num1,number2;
    scanf("%d",&num1);
    scanf("%d",&number2);
    util(&num1,&number2);
    ++(--num1);
    ++number2;    
    return 0;
}

void util(int *num1,int *number2)
{
    int tmp;
    tmp = *num1;
    *num1=*number2;
    *number2=tmp;
}
