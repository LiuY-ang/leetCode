int lengthOfLastWord(char* s)
{
  int length=strlen(s),i;
  int lastWord=0;
  if(length==0) //字符串的长度为0
    return 0; //直接返回
  while ( s[length-1] == ' ' ) //从后往前扫描
  {  //直到最后一个单词的最后一个字母结束
    length--;
  }
  for ( i = length-1; i >= 0; i--)//从最后一个单词的最后字母开始计数长度
  {
    if(s[i]==' ') //碰到' '说明最后一个单词已经结束
      break;//退出循环即可
    else  //如果不是‘ ’，说明还是最后一个单词
      lastWord++; //继续计数字符个数
  }
  return lastWord; //返回最后一个单词的长度
}
int main()
{
  char s[3]={' ','a','\0'};
  printf("%d\n",lengthOfLastWord(s) );
}
