import matplotlib.pyplot as plt

# Example data for illustration
metrics = ['Missing Values', 'Duplicates', 'Inconsistencies']
before = [30, 25, 40]  # Percentages before cleaning
after = [5, 3, 10]     # Percentages after cleaning

plt.figure(figsize=(8, 4))
plt.plot(metrics, before, marker='o', color='red', label='Before Cleaning')
plt.plot(metrics, after, marker='o', color='green', label='After Cleaning')
plt.xlabel('Data Quality Issues')
plt.ylabel('Percentage')
plt.title('Impact of Data Cleaning')
plt.legend()
plt.show()
