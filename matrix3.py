import random
import math
import matplotlib.pyplot as plt

rows = 80
cols = 5

# ===============================
# Poisson Random Generator
# ===============================
def poisson(lam=3):
    L = math.exp(-lam)
    k = 0
    p = 1
    while p > L:
        k += 1
        p *= random.random()
    return k - 1


# ===============================
# Step 1: Generate 80x5 Matrix
# ===============================

matrix = []

for _ in range(rows):
    row = []
    for _ in range(cols):

        dist_type = random.choice([0,1,3])

        if dist_type == 0:
            value = int(random.gauss(20,7))
            value = max(0, min(40,value))

        elif dist_type == 1:
            value = random.randint(41,70)

        else:
            value = poisson(3)
            value = 71 + value
            value = max(71, min(95,value))

        row.append(value)

    matrix.append(row)

print("Generated 80x5 Marks Matrix:\n")
for r in matrix[:5]:
    print(r)


# ===============================
# Step 2: Create Target Column y
# ===============================

dataset = []

for row in matrix:

    m1,m2,m3,m4,m5 = row

    noise = random.gauss(0,1)

    y = 3.1*m1 + 4.5*m2 + 5.1*m3 + 6.5*m4 + 6*m5 + noise

    dataset.append([m1,m2,m3,m4,m5,y])

print("\nDataset with target column (first 5 rows):\n")
for r in dataset[:5]:
    print(r)


# ===============================
# Step 3: Split Dataset
# ===============================

random.shuffle(dataset)

train_size = int(0.70 * len(dataset))
val_size = int(0.15 * len(dataset))

train_data = dataset[:train_size]
val_data = dataset[train_size:train_size+val_size]
test_data = dataset[train_size+val_size:]

print("\nDataset Split")
print("Training:",len(train_data))
print("Validation:",len(val_data))
print("Testing:",len(test_data))


# ===============================
# Step 4: Separate X and y
# ===============================

X_train = [row[:5] for row in train_data]
y_train = [row[5] for row in train_data]

X_val = [row[:5] for row in val_data]
y_val = [row[5] for row in val_data]

X_test = [row[:5] for row in test_data]
y_test = [row[5] for row in test_data]

print("\nExample Training Sample")
print("X:",X_train[0])
print("y:",y_train[0])


# ===============================
# Step 5: Histogram
# ===============================

all_marks = [mark for row in matrix for mark in row]

plt.figure(figsize=(8,5))
plt.hist(all_marks, bins=15, edgecolor='black')

plt.title("Histogram of Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")

plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()


# ===============================
# Step 6: Standardization
# ===============================

all_values = [val for row in matrix for val in row]

mean = sum(all_values) / len(all_values)

std = (sum((x-mean)**2 for x in all_values)/len(all_values))**0.5


standardized_matrix = []

for row in matrix:
    standardized_row = [(x-mean)/std for x in row]
    standardized_matrix.append(standardized_row)


print("\nStandardized Matrix (first 5 rows)\n")
for r in standardized_matrix[:5]:
    print(r)


# ===============================
# Step 7: Heatmap
# ===============================

plt.figure(figsize=(10,8))

plt.imshow(standardized_matrix, cmap='coolwarm', aspect='auto')

plt.colorbar(label='Standardized Marks (Z-score)')

plt.title("Heatmap of Standardized Marks")
plt.xlabel("Subjects")
plt.ylabel("Students")

# How YOU can SEE the training data

print("\nFirst 5 Training Samples")
for row in train_data[:5]:
    print(row)

print("\nFirst 5 Validation Samples")
for row in val_data[:5]:
    print(row)

print("\nFirst 5 Test Samples")
for row in test_data[:5]:
    print(row)

plt.show()