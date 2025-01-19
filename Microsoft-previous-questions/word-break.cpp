/*Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
*/
#define MAX 26
#define INDEX(c) (int)c - (int)'a'
class Solution
{
public:  
    int dictionaryContains(string word , vector<string> dictionary)
    {
        int size = dictionary.size();
        for (int i = 0; i < size; i++)
            if (dictionary[i].compare(word) == 0)
                return true;
        return false;
    }

    bool wordBreak(string s, vector<string>& wordDict)
    {
        int n = s.size();
        if (n == 0)
            return true;
        vector<bool> dp(n + 1, 0);
        vector<int> matched_index;
        matched_index.push_back(-1);

        for (int i = 0; i < n; i++) 
        {
            int msize = matched_index.size();
            int f = 0;
            for (int j = msize - 1; j >= 0; j--) 
            {
                string sb = s.substr(matched_index[j] + 1, i - matched_index[j]);

                if (dictionaryContains(sb,wordDict))
                {
                    f = 1;
                    break;
                }
            }
            if (f == 1) 
            {
                dp[i] = 1;
                matched_index.push_back(i);
            }
        }
        return dp[n - 1];
    }
};
