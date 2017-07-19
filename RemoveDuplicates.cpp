#include <stdio.h>
int removeDuplicates(int* nums, int numsSize)
{
    if( numsSize == 0 )
      return 0;

    int length = 1;  //初始化为1
    for ( int i=1;i<numsSize;++i )
    {
      if( nums[length-1] < nums[i] )
      {
        int temp = nums[i];
        nums[i] = nums[length];
        nums[length] = temp;
        ++length;
      }
    }
    return length;
}
int main()
{
  int nums[3];
  nums[0]=nums[1]=1;nums[2]=2;
  int length = removeDuplicates(nums,3);
  for( int i=0;i<length;++i )
  {
    if (i==length-1)
      printf("%d\n",nums[i]);
    else
      printf("%d ",nums[i] );
  }
}
