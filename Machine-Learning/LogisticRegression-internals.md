
# How Logistic Regression Works Internally

## 1. Basic Idea

- Takes weighted sum of input features.
- Applies a Sigmoid function to squash output between 0 and 1.
- If probability > 0.5 → predict class 1, else class 0.

## 2. Step-by-Step

Given input features `X = [x1, x2]`, weights `[w1, w2]`, and bias `b`:

### Step 1: Linear Combination
```python
z = w1 * x1 + w2 * x2 + b
```

### Step 2: Apply Sigmoid
```python
sigmoid(z) = 1 / (1 + exp(-z))
```

### Step 3: Make Prediction
```python
if sigmoid(z) >= 0.5:
    predict class 1
else:
    predict class 0
```

## 3. Training the Model

- **Loss Function:** Binary Cross-Entropy Loss

The Loss is calculated as:  
**Loss = - [ y × log(p) + (1 - y) × log(1 - p) ]**

where:
- `y` = actual label (0 or 1)
- `p` = predicted probability output by the sigmoid function

- **Optimization:** Use Gradient Descent to update weights and bias.

## 4. Full Python Code (From Scratch)

```python
import numpy as np

class LogisticRegressionFromScratch:
    def __init__(self, learning_rate=0.1, n_iterations=1000):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.weights = None
        self.bias = None

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.n_iterations):
            linear_model = np.dot(X, self.weights) + self.bias
            y_predicted = self.sigmoid(linear_model)

            dw = (1 / n_samples) * np.dot(X.T, (y_predicted - y))
            db = (1 / n_samples) * np.sum(y_predicted - y)

            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db

    def predict(self, X):
        linear_model = np.dot(X, self.weights) + self.bias
        y_predicted = self.sigmoid(linear_model)
        y_predicted_cls = [1 if i >= 0.5 else 0 for i in y_predicted]
        return np.array(y_predicted_cls)

# Example Usage
if __name__ == "__main__":
    X = np.array([[1, 1], [1, 0], [0, 1], [0, 0]])
    y = np.array([1, 0, 0, 0])

    model = LogisticRegressionFromScratch(learning_rate=0.1, n_iterations=1000)
    model.fit(X, y)
    predictions = model.predict(X)

    print("Predictions:", predictions)
```

## 5. Quick Summary

| Step | What happens |
|:----:|:-------------|
| Linear model | z = wX + b |
| Non-linearity | Sigmoid activation σ(z) |
| Loss function | Binary Cross-Entropy |
| Optimization | Gradient Descent |

---

This provides a clear intuition and a working base implementation of Logistic Regression from scratch! 🚀
