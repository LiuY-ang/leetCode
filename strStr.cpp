int strStr(char* haystack, char* needle)
{
  int i=0,j=0;
  for( i=0;haystack[i]!='\0';++i)
  {
    int t=i;  //记录下i的位置
    for( j=0;needle[j]!='\0';++j)
    {
      if (haystack[i] != needle[j])
      { //一旦发现有不相等的，循环停止
        break;
      }
      else  //若相等，则将i加1。j的值在for语句中加1
        ++i;
    }
    i=t; //循环结束之后，将i的值恢复
    if (needle[j] == '\0' )//若循环结束之后，needle[j]的值为'\0'
    {        //子串与主串相匹配，返回i即可
      return i;
    }
    //若needle[j]不等'\0'，则i进行下一次循环
  }
  if (i==0 && needle[0]=='\0') //如果都为空串,代表根本就没有进入循环
    return 0;
  return -1;
}
