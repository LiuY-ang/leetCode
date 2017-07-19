int strStr(char *haystack,char *needle)
{
  if (*needle == '\0') //子串为0，即空串，无论主串是什么，则都存在
    return 0;  //则返回0
  if (*haystack=='\0' || strlen(haystack)<strlen(needle) )//主串为0
    return -1; //或者子串长度大于主串长度，则都说明在主串中不存在子串，则返回-1
  char* ph=haystack; //pn，ph的值在整个程序运行期间都没有改变
  char* pn=needle;  //故起记录的作用，记录起始地址
  while ( *haystack !='\0' && *needle!='\0')//haystack和needle没有到达文件末尾就循环
  {
    if ( *haystack==*needle)
    { //若haystack和needle位置上的值相等，则继续haystack和needle下一个位置的元素
      ++haystack;  //故将haystack和needle加1
      ++needle;
    }//若*haystack和*needle不相等，则比较pn和needle，pn的值为初始地址
    else if(pn==needle) //若needle等于初始地址(pn)，又needle（子串第一个值）和当前haystack的值
    { //不相等
      ++haystack;//则将haystack加1，以便继续和子串的第一个的值比较
    }
    else //如果以上两种情况都不满足，则是比较了子串的前(needle-pn)个元素，并且这些元素相等
    { //在needle-pn+1个元素的时候不匹配，则需要回溯
      haystack=haystack-(needle-pn)+1; //haystack回溯到haystack-(needle-pn)+1
      needle=pn; //needle回溯到起始位置
    }
  }
  if( *needle == '\0' ) //说明找到
    return haystack-ph-(needle-pn);
  return -1;
}
