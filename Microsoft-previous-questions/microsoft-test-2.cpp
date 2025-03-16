// you can use includes, for example:
// #include <algorithm>
#include<map>
// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

const int N = 100001;
class Tree 
{
    vector<int> data;
    int n;

    int build(int idx, int start, int end) 
    {
        if (end < start) 
        {
            return 0;
        }
        if (start == end) 
        {
            data[idx] = 1;
        }
        else 
        {
            int mid = (start + end) / 2;
            data[idx] = build(idx * 2, start, mid) + build(idx * 2 + 1, mid + 1, end);
        }
        return data[idx];
    }

    void updateRange(int idx, int start, int end, int left, int right, int val) 
    {
        if (end < start || right < start || end < left) 
        {
            return;
        }
        if (start <= left && right <= end) 
        {
            data[idx] += val;
        }
        if (start == end) 
        {
            return;
        }
        int mid = (start + end) / 2;
        updateRange(idx * 2, start, mid, left, right, val);
        updateRange(idx * 2 + 1, mid + 1, end, left, right, val);
    }

    int queryRange(int idx, int start, int end, int left, int right) 
    {
        if (end < start || right < start || end < left) 
        {
            return 0;
        }
        if (left <= start && end <= right)
        {
            return data[idx];
        }
        int mid = (start + end) / 2;
        return queryRange(idx * 2, start, mid, left, right) +
            queryRange(idx * 2 + 1, mid + 1, end, left, right);
    }
public:
    Tree(int n) 
    {
        this->n = n;
        data = vector<int>(4 * N, 0);
        build(1, 1, n);
    }
    void decrement(int index) 
    {
        updateRange(1, 1, n, index + 1, index + 1, -1); 
    }
    int query(int left, int right) 
    {
        if (right < left) 
        {
            return 0;
        }
        return queryRange(1, 1, n, left + 1, right + 1); 
    }
};


int solution(vector<int> &T) 
{
    // Implement your solution here
    map<int, vector<int>> indexes;
	int n = T.size();
	for (int i = 0; i < n; i++) 
	{
		indexes[T[i]].push_back(i);
	}

	Tree processed(n);

	int sumSTasks = 0;
	long long int result = 0;
	long long int mod = 1e9 + 7;
	for (auto keyValue : indexes) 
	{
		int task = keyValue.first;
		auto taskIdx = keyValue.second;

		for (int index : taskIdx) 
		{
			result = (result + task) % mod; 
			result = (result + sumSTasks) % mod; 

			int lEqualLeft = processed.query(0, index - 1);
			result = (result + (lEqualLeft * task)) % mod;

			int lEqualRight = processed.query(index + 1, n - 1);
			result = (result + (lEqualRight * (task - 1))) % mod;
		}

		for (int i : taskIdx) 
		{
			processed.decrement(i);
		}

		sumSTasks += task * taskIdx.size();
	}
	return result;
}

