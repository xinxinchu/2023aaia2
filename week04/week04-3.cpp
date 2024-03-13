#include <stdio.h>
int main()
{
  int a = 3;
  while(a>0)
  {
    printf("a是%d\n",a);
    a--;///其實是a -=1 的縮寫
  }
}

