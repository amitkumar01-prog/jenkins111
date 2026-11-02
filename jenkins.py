from sklearn.linear_model import LinearRegression

# Training data
X = [[1], [2], [3], [4], [5]]
y = [2, 4, 6, 8, 10]

# Create the Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X, y)


# Function to make predictions
def predict(value):
    return model.predict([[value]])[0]


# Run this when the file is executed directly
if __name__ == "__main__":
    prediction = predict(6)

    print("AI/DS Linear Regression Model")
    print("-----------------------------")
    print("Input value:", 6)
    print("Predicted value:", prediction)