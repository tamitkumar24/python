import random
import math
import matplotlib.pyplot as plt

rows = 80
cols = 5

# -------------------------------
# Poisson function
# -------------------------------
def poisson(lam=3):
    L = math.exp(-lam)
    k = 0
    p = 1
    while p > L:
        k += 1
        p *= random.random()
    return k - 1


# -------------------------------
# Grade point conversion
# -------------------------------
def grade_point(mark):

    if mark >= 90:
        return 10
    elif mark >= 80:
        return 9
    elif mark >= 70:
        return 8
    elif mark >= 60:
        return 7
    elif mark >= 50:
        return 6
    elif mark >= 40:
        return 5
    else:
        return 0


# -------------------------------
# Generate marks matrix
# -------------------------------
matrix = []

for _ in range(rows):

    row = []

    for _ in range(cols):

        dist_type = random.choice([0,1,3])

        if dist_type == 0:
            value = int(random.gauss(20,7))
            value = max(0,min(40,value))

        elif dist_type == 1:
            value = random.randint(41,70)

        else:
            value = poisson(3)
            value = 71 + value
            value = max(71,min(95,value))

        row.append(value)

    matrix.append(row)


print("First 5 students marks")
for r in matrix[:5]:
    print(r)


# -------------------------------
# Calculate CGPA
# -------------------------------
cgpa_list = []

for row in matrix:

    gp = [grade_point(m) for m in row]

    cgpa = sum(gp)/len(gp)

    cgpa_list.append(cgpa)


print("\nFirst 5 CGPA values")
for i in range(5):
    print(matrix[i], " -> CGPA:", cgpa_list[i])


# -------------------------------
# Create target y
# -------------------------------
dataset = []

for i,row in enumerate(matrix):

    m1,m2,m3,m4,m5 = row

    noise = random.gauss(0,1)

    y = 3.1*m1 + 4.5*m2 + 5.1*m3 + 6.5*m4 + 6*m5 + noise

    dataset.append([m1,m2,m3,m4,m5,cgpa_list[i],y])


# -------------------------------
# Split dataset
# -------------------------------
random.shuffle(dataset)

train_size = int(0.70*len(dataset))
val_size = int(0.15*len(dataset))

train = dataset[:train_size]
val = dataset[train_size:train_size+val_size]
test = dataset[train_size+val_size:]


X_train = [row[:5] for row in train]
y_train = [row[6] for row in train]

X_test = [row[:5] for row in test]
y_test = [row[6] for row in test]


print("\nTraining size:",len(X_train))
print("Testing size:",len(X_test))


# -------------------------------
# Linear Regression Training
# -------------------------------
weights = [0]*5
bias = 0

lr = 0.00001
epochs = 500


for epoch in range(epochs):

    for i in range(len(X_train)):

        x = X_train[i]
        y = y_train[i]

        # prediction
        y_pred = bias

        for j in range(5):
            y_pred += weights[j]*x[j]

        error = y_pred - y

        # update weights
        for j in range(5):
            weights[j] -= lr*error*x[j]

        bias -= lr*error


print("\nLearned weights:",weights)
print("Learned bias:",bias)


# -------------------------------
# Prediction function
# -------------------------------
def predict(x):

    result = bias

    for i in range(5):
        result += weights[i]*x[i]

    return result


# -------------------------------
# Test predictions
# -------------------------------
predictions = []

for i in range(len(X_test)):

    pred = predict(X_test[i])

    predictions.append(pred)

    print("Marks:",X_test[i],
          " Predicted:",round(pred,2),
          " Actual:",round(y_test[i],2))


# -------------------------------
# Calculate MSE
# -------------------------------
error = 0

for i in range(len(predictions)):
    error += (predictions[i]-y_test[i])**2

mse = error/len(predictions)

print("\nTest MSE:",mse)


# -------------------------------
# Plot Prediction vs Actual
# -------------------------------
plt.scatter(y_test,predictions)

plt.xlabel("Actual Score")
plt.ylabel("Predicted Score")

plt.title("Prediction vs Actual")

plt.show()