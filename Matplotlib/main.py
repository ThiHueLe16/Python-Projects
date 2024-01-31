import matplotlib.pyplot as plt

# Sample data for lines
x_values = [786, 2252.8, 3891.2, 8601.6, 27955.2, 59904]
y_values1 = [0.014120, 0.025882, 0.044095, 0.085574, 0.342793, 0.768934]
y_values2 = [0.015046, 0.037155, 0.069187, 0.165030, 0.485623, 1.326942]
y_values3 = [0.015628, 0.038885, 0.068070, 0.165154, 0.505280, 3.744245]

# Plotting the first line
plt.plot(x_values, y_values1, label='All SIMD', color='blue', marker='o')

# Plotting the second line
plt.plot(x_values, y_values2, label='Brightness SIMD', color='green', marker='s')

# Plotting the third line
plt.plot(x_values, y_values3, label='No SIMD', color='red', marker='v')

# Adding labels and title
plt.xlabel("Picture's Size")
plt.ylabel('Average Run Time')
plt.title('Performance Analyse')

# Adding a legend
plt.legend()

# Display the plot
plt.show()
