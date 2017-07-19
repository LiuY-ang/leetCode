int strStr(char* haystack, char* needle) {
    if(*needle == '\0')
        return 0;
    //printf("%s\n", needle += (strlen(needle)));
    if(*haystack == '\0' || strlen(haystack) < strlen(needle) )
        return -1;
    char* pStart = needle;
    char* phStart = haystack;
    while(*haystack != '\0' && *needle != '\0')
    {
        if(*haystack == *needle)
        {
            haystack++;
            needle++;
        }
        else if(needle == pStart)
        {
            haystack++;
        }
        else
        {
            haystack = haystack - (needle - pStart) + 1;
            needle = pStart;
        }
    }
    if(*needle == '\0')
        return (haystack - phStart) - (needle - pStart);
    else
        return -1;
}
