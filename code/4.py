import matplotlib.pyplot as plt

sources = ['Database A', 'API B', 'Files C']
errors_before = [35, 40, 45]
errors_after = [5, 8, 10]

x = range(len(sources))
width = 0.35

plt.figure(figsize=(8, 4))
plt.bar(x, errors_before, width, color='red', label='Errors Before')
plt.bar([p + width for p in x], errors_after, width, color='green', label='Errors After')
plt.xlabel('Data Sources')
plt.ylabel('Error Count')
plt.title('Error Distribution Across Data Sources')
plt.xticks([p + width/2 for p in x], sources)
plt.legend()
plt.show()
