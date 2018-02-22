from matplotlib import pyplot as plt

# Define data.
x_values = list(range(5001))
cubes = [x**3 for x in x_values]

# Make plot.
plt.scatter(x_values, cubes, edgecolor='none', c=cubes, cmap=plt.cm.BuGn, s=40)

# Customize plot.
plt.title("Market Trends", fontsize=34)
plt.xlabel('Margin', fontsize=17)
plt.ylabel('Sales', fontsize=17)
plt.tick_params(axis='both', labelsize=15)
plt.axis([0, 5100, 0, 5100**3])


# Show plot.
plt.show()