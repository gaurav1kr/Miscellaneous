#include<iostream>
#include<vector>
using namespace std;

const long MOD = 1e9 + 7;

int givesum(int A[], int n)
{
	int max = *max_element(A, A + n);
	int maxBit = log2(max) + 1;
	int totalSubarrays = n * (n + 1) / 2;
	long long s = 0;

	for (int i = 0; i < maxBit; i++) 
	{
		int c1 = 0;
		vector<int> vec;
		int sum = 0;
		for (int j = 0; j < n; j++) 
		{
			int a = A[j] >> i;
			if (!(a & 1)) 
			{
				vec.push_back(j);
			}
		}
		int cntSubarrNotSet = 0;
		int cnt = 1;
		for (int j = 1; j < vec.size(); j++) 
		{
			if (vec[j] - vec[j - 1] == 1) 
			{
				cnt++;
			}
			else 
			{
				cntSubarrNotSet += cnt * (cnt + 1) / 2;
				cnt = 1;
			}
		}

		cntSubarrNotSet += cnt * (cnt + 1) / 2;
		if (vec.size() == 0)
		{
			cntSubarrNotSet = 0;
		}

		int cntSubarrIthSet = totalSubarrays - cntSubarrNotSet;
		s += cntSubarrIthSet * pow(2, i);
		}

		return s%MOD;
	}

	// Driver code
	int main()
	{
		int A[] = { 1000000000, 1000000000, 1000000000};
		int n = sizeof(A) / sizeof(A[0]);

		cout << givesum(A, n);// expected output - 999999965

		return 0;
	}
