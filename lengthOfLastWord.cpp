int lengthOfLastWord(char* s)
{
  int len=0;
  for(int i=0;i<strlen(s);++i)
  {
    if( s[i]==' ' )
    {
      while(s[i]==' ')
        ++i;
      if( s[i]=='\0')
          return len;
      else
          len=0;
    }
    ++len;
  }
  return len;
}
int main()
{
  char s[3]={' ','a','\0'};
  printf("%d\n",lengthOfLastWord(s) );
}
