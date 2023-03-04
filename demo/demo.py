import matplotlib.pyplot as plt
import numpy as np

# Tạo dữ liệu giả
x = np.arange(0, 10, 0.1)
y = np.sin(x)

# Tạo đồ thị
plt.plot(x, y)
plt.table

# Lưu đồ thị thành ảnh PNG
plt.savefig('myplot.png')
