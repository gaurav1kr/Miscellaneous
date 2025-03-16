// you can use includes, for example:
// #include <algorithm>
#include<limits.h>

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

int solution(vector<int> &A) 
{
    // Implement your solution here
    int mval = INT_MAX;
    int ival = 1;
    int jval = A.size() - 2;
    while (ival < (jval - 1)) 
    {
        mval = min((A[ival] + A[jval]), mval);
        if (A[ival] < A[jval]) 
        {
            jval--;
        }
        else
        {
            ival++;
        }
    }
    return mval;
}
