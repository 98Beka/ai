import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import random

# Возможные категории
categories = ['A', 'B', 'C']

# Метод для генерации одного объекта
def generate_point():
    return {
        'x': random.uniform(-10, 10),
        'y': random.uniform(-10, 10),
        'category': random.choice(categories)
    }

# Количество точек
num_points = 100

# Генерируем список объектов
points = [generate_point() for _ in range(num_points)]
custom_palette = {'A': 'green', 'B': 'blue', 'C': 'red'}

# Разбиваем на отдельные списки
x = [point['x'] for point in points]
y = [point['y'] for point in points]
hue = [point['category'] for point in points]

# Строим scatter plot
sns.scatterplot(x=x, y=y, hue=hue, palette=custom_palette)

# Добавляем заголовок и легенду
plt.title("Random Scatter Plot with Objects")
plt.legend(title="ff")
plt.show()
