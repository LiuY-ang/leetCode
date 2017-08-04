#include <stdlib.h>
#include <sys/malloc.h>
void rotate(int* nums, int numsSize, int k)
{
  int *temp=(int*)malloc(sizeof(int)*numsSize);
  for(int i=0;i<numsSize;++i)
  {
    temp[(i+k)%numsSize]=nums[i];
  }
  for(int i=0;i<numsSize;++i)
  {
    nums[i]=temp[i];
    printf("%d ",temp[i]);
  }
  printf("\n" );
}
int main() {
  int a=1,numsSize=7;
  int nums[7]={1,2,3,4,5,6,7};
  rotate(nums,numsSize,3);
  printf("%d\n",a );
  return 0;
}
