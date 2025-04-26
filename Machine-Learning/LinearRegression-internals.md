
# Linear Regression Internals Explained

---

## 🔥 How `LinearRegression()` Works Internally

### 1. Problem Setup

- **Input (X)**: Feature(s) (e.g., house size)
- **Output (y)**: Target (e.g., house price)

Trying to find the best line:

**Predicted value (ŷ) = wX + b**

Where:
- `w`: weight (slope)
- `b`: bias (intercept)

---

### 2. Goal

Minimize the error (difference between actual `y` and predicted `ŷ`) using **Mean Squared Error (MSE)**:

**MSE = (1/n) * Σ(yᵢ - (wXᵢ + b))²**

---

### 3. How scikit-learn Finds `w` and `b`

It uses **Least Squares Method** (Analytical solution), not gradient descent.

### The Formula:

**w = (XᵀX)⁻¹Xᵀy**

Where:
- `Xᵀ` = transpose of `X`
- `(XᵀX)⁻¹` = inverse of `XᵀX`
- `y` = output vector

**Bias** `b` is also automatically calculated if `fit_intercept=True`.

---

### 4. Steps Inside `model.fit(X, y)`

- Add a column of ones to `X` to account for `b`
- Solve using the normal equation
- Save learned parameters (`model.coef_`, `model.intercept_`)

---

### 5. Steps Inside `model.predict(X_new)`

- For a new input `X_new`, predict:

**ŷ = w * X_new + b**

---

# 🌟 Summary Table

| Step | What Happens |
|:---|:---|
| `model.fit(X, y)` | Finds best `w` and `b` |
| `model.predict(X_new)` | Predicts using `wX + b` |

---

# 📦 How sklearn Does it Internally (Code Sketch)

```python
# Add column for bias
X_b = np.c_[np.ones((X.shape[0], 1)), X]

# Solve using normal equation
theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)

# theta_best[0] -> intercept (b)
# theta_best[1:] -> coefficient/weight (w)
```

---

# 🚀 Your Example (House Size vs Price)

- Increase 500 sq ft ➔ Increase 25 lakhs
- So slope `w ≈ 0.05`
- Intercept `b ≈ 0`

Prediction for 1800:

**price = 0.05 × 1800 = 90 lakhs**

---

# 💡 Final Notes

- sklearn `LinearRegression()` uses **closed-form solution**, not **gradient descent**.
- For massive datasets, it may use optimized solvers internally.

---

# 💡 Manual Implementation Using Only NumPy

Let's implement our own `LinearRegression`!

```python
import numpy as np

# Data
X = np.array([[1000], [1500], [2000], [2500]])
y = np.array([50, 75, 100, 125])

# Add bias term
X_b = np.c_[np.ones((X.shape[0], 1)), X]

# Solve for best theta
theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)

# Intercept and coefficient
b = theta_best[0]
w = theta_best[1]

print(f"Intercept (b): {b}")
print(f"Weight (w): {w}")

# Predict for 1800
X_new = np.array([[1, 1800]])  # include bias
prediction = X_new.dot(theta_best)
print(f"Predicted price for 1800 sq ft: {prediction[0]} lakhs")
```

**Output:**
```text
Intercept (b): ~0.0
Weight (w): 0.05
Predicted price for 1800 sq ft: 90.0 lakhs
```
