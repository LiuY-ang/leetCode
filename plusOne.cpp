/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* plusOne(int* digits, int digitsSize, int* returnSize) {
    if ( digits==NULL || digitsSize<1)
      return NULL;
    int i=digitsSize-1;
    int* newDigits=NULL;
    while( digits[i]+1 > 9 && i>=0 )
    {//从后往前扫描，直到遇到直到遇到某位数digits[i]+1<=9或者i<0时，停止循环
      digits[i]=0;
      i--;
    }
    if( i == -1 )  //溢出的情况
    {
      *returnSize=digitsSize+1;
      newDigits=(int*)malloc(sizeof(int)*(*returnSize));
      memcpy(newDigits+1,digits,digitsSize*sizeof(int));
      newDigits[0]=1;
    }
    else
    {
      *returnSize=digitsSize;
      newDigits=(int*)malloc(sizeof(int)*(*returnSize));
      memcpy(newDigits,digits,sizeof(int)*(*returnSize));
      newDigits[i]=digits[i]+1;
    }
    return newDigits;
}
