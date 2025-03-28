## Problem: Pricing Errors in a Store

### Problem Statement
A store maintains a catalog of products along with their correct prices. However, due to errors in the billing system, some products may have been sold at incorrect prices.

You are given:
- A list of **products** and their corresponding **correct prices**.
- A list of **products sold** and the **prices they were sold at**.

Your task is to determine the **number of pricing errors**, i.e., instances where a product was sold at a price different from its correct price.

### Function Signature
```cpp
int priceCheck(vector<string> products, vector<float> productPrices,
               vector<string> productSold, vector<float> soldPrice);
```

### Input Format
- The first line contains an integer **N** – the number of products in the store.
- The next **N** lines each contain a string (product name) and a float (correct price).
- The next line contains an integer **M** – the number of products sold.
- The next **M** lines each contain a string (product name) and a float (sold price).

### Constraints
- \( 1 \leq N, M \leq 10^5 \)
- \( 0.01 \leq \) price values \( \leq 10^4 \)
- Product names contain only lowercase English letters (1 to 20 characters).
- Each product in `products` appears at most once.
- Each product in `productSold` is guaranteed to exist in `products`.

### Output Format
Print a single integer – the number of pricing errors.

### Example

#### Input
```
3  
apple 1.5  
banana 2.0  
orange 3.25  
5  
apple 1.5  
banana 2.0  
banana 2.5  
orange 3.25  
apple 1.0  
```

#### Output
```
2
```

#### Explanation
- The correct price of `"banana"` is **2.0**, but it was once sold at **2.5** (error).
- The correct price of `"apple"` is **1.5**, but it was once sold at **1.0** (error).
- `"orange"` and one sale of `"banana"` were correctly priced.
- Thus, **2 pricing errors** occurred.

### Sample Code Stub
```cpp
#include <bits/stdc++.h>
using namespace std;

int priceCheck(vector<string> products, vector<float> productPrices, vector<string> productSold, vector<float> soldPrice) {
    unordered_map<string, float> priceMap;
    for (size_t i = 0; i < products.size(); ++i) {
        priceMap[products[i]] = productPrices[i];
    }

    int errors = 0;
    for (size_t i = 0; i < productSold.size(); ++i) {
        if (priceMap[productSold[i]] != soldPrice[i]) {
            errors++;
        }
    }
    return errors;
}

int main() {
    int N;
    cin >> N;
    vector<string> products(N);
    vector<float> productPrices(N);

    for (int i = 0; i < N; i++) {
        cin >> products[i] >> productPrices[i];
    }

    int M;
    cin >> M;
    vector<string> productSold(M);
    vector<float> soldPrice(M);

    for (int i = 0; i < M; i++) {
        cin >> productSold[i] >> soldPrice[i];
    }

    cout << priceCheck(products, productPrices, productSold, soldPrice) << endl;
    return 0;
}
```

### Complexity Analysis
- **Building the hash map:** \( O(N) \)
- **Checking sold prices:** \( O(M) \)
- **Total complexity:** \( O(N + M) \)


