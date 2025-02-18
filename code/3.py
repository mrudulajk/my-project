import matplotlib.pyplot as plt

labels = ['Completeness', 'Consistency']
before = [75, 70]
after = [98, 95]

x = range(len(labels))
width = 0.35

plt.figure(figsize=(8, 4))
plt.bar(x, before, width, color='red', label='Before Cleaning')
plt.bar([p + width for p in x], after, width, color='green', label='After Cleaning')
plt.xlabel('Metrics')
plt.ylabel('Percentage')
plt.title('Data Consistency and Completeness')
plt.xticks([p + width/2 for p in x], labels)
plt.legend()
plt.show()
