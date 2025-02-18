import matplotlib.pyplot as plt

# Example data (in seconds and records per minute)
steps = ['Ingestion', 'Transformation', 'Loading']
processing_time = [20, 35, 15]
throughput = [1000, 800, 1200]  # records per minute

fig, ax1 = plt.subplots(figsize=(8, 4))

color = 'tab:blue'
ax1.set_xlabel('ETL Steps')
ax1.set_ylabel('Processing Time (s)', color=color)
ax1.bar(steps, processing_time, color=color, alpha=0.6, label='Processing Time')
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # second y-axis
color = 'tab:green'
ax2.set_ylabel('Throughput (records/min)', color=color)
ax2.plot(steps, throughput, color=color, marker='o', label='Throughput')
ax2.tick_params(axis='y', labelcolor=color)

plt.title('ETL Pipeline Performance')
fig.tight_layout()
plt.show()
