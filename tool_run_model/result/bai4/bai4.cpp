#include <iostream>
#include <cstdio>
 
enum { max = 127 };
static char str[max + 1] = "";
 
using namespace std;
 
int main()
{
    int max = 127;
    fgets(str, max, stdin);
    int n = atoi(str);
    cout<<(n+25);
 
    return 0;
}