# Step 1: Create two lists of numerical values
X = [2, 4, 6, 8, 10]
Y = [1, 3, 5, 7, 9]
# Step 2: Compute Euclidean distances without using math functions or zip
distances = []
for i in range(len(X)):
    diff = (Y[i] - X[i]) ** 2  # Squaring the difference
    approx_sqrt = diff ** 0.5  # Manual square root using exponentiation
    distances.append(approx_sqrt)
# Step 3: Implement Bubble Sort to sort the distances
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:  # Swap if the element is greater than the next
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
# Sort the distances list
bubble_sort(distances)
# Step 4: Print the sorted distances
print("Sorted Euclidean distances:", distances)
