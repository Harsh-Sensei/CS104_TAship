#include<stdio.h>
int main()
{
    int n1,n2;
    scanf("%d",&n1);
    scanf("%d",&n2);
    if (!n1) n2 = n1 + n2;
    else n1 = ~n1;
    return 0;
}
