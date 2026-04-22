import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['font.sans-serif'] = [
    'WenQuanYi Micro Hei', 
    'Noto Sans CJK SC', 
    'SimHei', 
    'Arial'
]
plt.rcParams['axes.unicode_minus'] = False  # 解决负号 '-' 显示为方块的问题

x = np.linspace(0, 10, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)
categories = ['A组', 'B组', 'C组', 'D组', 'E组']
values = [23, 45, 56, 78, 32]
values_2 = [12, 30, 45, 60, 20]

fig, ax = plt.subplots(figsize=(10, 6))

# 折线图
ax.plot(x, y_sin, label='正弦', color='b', linewidth=2)
ax.plot(x, y_cos, label='余弦', color='r',  linestyle='--')
ax.set_title('趋势分析：正弦与余弦')
ax.set_xlabel('时间/步长')
ax.set_ylabel('振幅')
ax.legend()


plt.tight_layout()
plt.savefig('line.png')
plt.show()
