import matplotlib.pyplot as plt

models = ["Initial Prototype", "Enhanced ETL", "Optimized AutoAI"]
quality_improvement = [60, 85, 95]  # Hypothetical data quality score out of 100

plt.figure(figsize=(8, 4))
plt.bar(models, quality_improvement, color=['gray', 'blue', 'green'])
plt.xlabel("System Versions")
plt.ylabel("Data Quality Score (%)")
plt.title("Evolution of Data Quality Improvement")
plt.ylim(50, 100)
plt.show()
