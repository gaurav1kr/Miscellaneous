
# Sparse Matrix Representation and Operations

## What is a Sparse Matrix?
A **sparse matrix** is a matrix in which most of the elements are zero (or, in some contexts, a default value). The primary goal of handling sparse matrices efficiently is to save memory and computational resources by storing and operating on only the non-zero elements.

---

## Efficient Representation and Storage of a Binary 2D Sparse Array
For a **binary 2D sparse matrix** (containing only 0s and 1s), an efficient way to represent it is **using a list of coordinates (row, column)** for non-zero entries. This is often referred to as the **Coordinate List (COO) format**.

### Example:
Matrix:
```
1 0 0  
0 1 0  
0 0 1  
```
COO Representation:
```
[(0, 0), (1, 1), (2, 2)]
```

---

## Addition of Two Sparse Binary Matrices in COO Format
To add two matrices stored in this representation:
1. Merge the two lists of non-zero coordinates.
2. For overlapping coordinates, ensure the sum of binary values doesn't exceed 1 (as it remains binary).

### C++ Implementation for COO Format
```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <set>
using namespace std;

// Representation of a Sparse Matrix in COO format
typedef pair<int, int> Coordinate;
typedef vector<Coordinate> SparseMatrix;

// Function to add two sparse matrices
SparseMatrix addSparseMatrices(const SparseMatrix &A, const SparseMatrix &B) 
{
    SparseMatrix result;
    set<Coordinate> coordinates;

    // Use a set to track all unique coordinates
    for (const auto &coord : A)
        coordinates.insert(coord);
    for (const auto &coord : B) 
	{
        // If already in coordinates, it means overlap
        if (coordinates.count(coord)) 
		{
            coordinates.erase(coord); // Binary sum would cancel out
        } else 
		{
            coordinates.insert(coord);
        }
    }

    // Convert set to vector result
    for (const auto &coord : coordinates) 
	{
        result.push_back(coord);
    }

    return result;
}

// Helper function to print sparse matrix
void printSparseMatrix(const SparseMatrix &matrix) 
{
    for (const auto &coord : matrix) 
	{
        cout << "(" << coord.first << ", " << coord.second << ") ";
    }
    cout << endl;
}

int main() 
{
    // Example Sparse Matrices in COO format
    SparseMatrix A = {{0, 0}, {1, 1}, {2, 2}};
    SparseMatrix B = {{1, 1}, {2, 2}, {0, 1}};

    cout << "Matrix A: ";
    printSparseMatrix(A);

    cout << "Matrix B: ";
    printSparseMatrix(B);

    // Add the two sparse matrices
    SparseMatrix result = addSparseMatrices(A, B);

    cout << "Resultant Matrix: ";
    printSparseMatrix(result);

    return 0;
}
```

---

## Compressed Sparse Row (CSR) Format
The **Compressed Sparse Row (CSR)** format is a memory-efficient way to store a sparse matrix by compacting its rows, storing only the non-zero values and their column indices along with row pointers.

### CSR Representation Structure
For a matrix:
```
1 0 0
0 1 0
0 0 1
```
1. **Values**: Stores non-zero values: `[1, 1, 1]`  
2. **Column Indices**: Stores the column indices of these values: `[0, 1, 2]`  
3. **Row Pointers**: Stores the cumulative count of non-zero entries up to each row: `[0, 1, 2, 3]`

---

## Addition of Two Sparse Matrices in CSR Format
To add two matrices in CSR format:
1. Traverse both matrices row by row.
2. For each row, merge the column indices and values, handling overlapping indices by summing values (and ensuring the binary nature of the matrix if needed).

### C++ Implementation for CSR Format
```cpp
#include <iostream>
#include <vector>
#include <map>
using namespace std;

// CSR Representation of a Sparse Matrix
struct CSR 
{
    vector<int> values;       // Non-zero values
    vector<int> colIndices;   // Column indices of non-zero values
    vector<int> rowPointers;  // Row pointers indicating where each row starts
};

// Function to add two sparse matrices in CSR format
CSR addCSRMatrices(const CSR &A, const CSR &B, int rows) 
{
    CSR result;
    result.rowPointers.push_back(0); // Start of the first row

    for (int i = 0; i < rows; ++i) 
	{
        map<int, int> rowElements; // To merge column indices and values for current row

        // Traverse row of A
        for (int j = A.rowPointers[i]; j < A.rowPointers[i + 1]; ++j) 
		{
            rowElements[A.colIndices[j]] = A.values[j];
        }

        // Traverse row of B
        for (int j = B.rowPointers[i]; j < B.rowPointers[i + 1]; ++j) 
		{
            if (rowElements.count(B.colIndices[j])) 
			{
                rowElements[B.colIndices[j]] += B.values[j];
                // Convert to binary if needed
                if (rowElements[B.colIndices[j]] > 1)
                    rowElements[B.colIndices[j]] = 1;
            } else 
			{
                rowElements[B.colIndices[j]] = B.values[j];
            }
        }

        // Add the merged row to the result
        for (auto &entry : rowElements) 
		{
            result.values.push_back(entry.second);
            result.colIndices.push_back(entry.first);
        }

        result.rowPointers.push_back(result.values.size()); // Update row pointer
    }

    return result;
}

// Helper function to print a CSR matrix
void printCSR(const CSR &matrix) 
{
    cout << "Values: ";
    for (int val : matrix.values)
        cout << val << " ";
    cout << endl;

    cout << "Column Indices: ";
    for (int col : matrix.colIndices)
        cout << col << " ";
    cout << endl;

    cout << "Row Pointers: ";
    for (int ptr : matrix.rowPointers)
        cout << ptr << " ";
    cout << endl;
}

int main() 
{
    // Example Sparse Matrices in CSR Format
    CSR A = {
        {1, 1, 1},           // Values
        {0, 1, 2},           // Column Indices
        {0, 1, 2, 3}         // Row Pointers
    };

    CSR B = {
        {1, 1},              // Values
        {1, 2},              // Column Indices
        {0, 0, 1, 2}         // Row Pointers
    };

    int rows = 3; // Number of rows in the matrices

    cout << "Matrix A in CSR format:" << endl;
    printCSR(A);

    cout << "Matrix B in CSR format:" << endl;
    printCSR(B);

    // Add the two sparse matrices
    CSR result = addCSRMatrices(A, B, rows);

    cout << "Resultant Matrix in CSR format:" << endl;
    printCSR(result);

    return 0;
}
```

---

## Sample Output for COO and CSR

### COO Format
For input matrices:
```
A = [(0, 0), (1, 1), (2, 2)]
B = [(1, 1), (2, 2), (0, 1)]
```
Output:
```
Matrix A: (0, 0) (1, 1) (2, 2)
Matrix B: (1, 1) (2, 2) (0, 1)
Resultant Matrix: (0, 0) (0, 1)
```

### CSR Format
For input matrices:
```
Matrix A:
Values: 1 1 1
Column Indices: 0 1 2
Row Pointers: 0 1 2 3

Matrix B:
Values: 1 1
Column Indices: 1 2
Row Pointers: 0 0 1 2
```
Output:
```
Resultant Matrix:
Values: 1 1 1
Column Indices: 0 1 2
Row Pointers: 0 1 2 3
```

---

This document covers both COO and CSR representations with their respective addition implementations.
