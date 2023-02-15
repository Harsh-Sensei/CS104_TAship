#include<stdio.h>
int main()
{
    int number,n2;
    scanf("%d",&number);
    scanf("%d",&n2);
    if (!number) n2 = number + n2;
    else number = ~number;
    return 0;
}
