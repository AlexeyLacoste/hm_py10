# import random
#
# import pandas as pd
#
# # Создаем список 'lst'
# lst = ['robot'] * 10 + ['human'] * 10
#
# # Перемешиваем элементы списка
# random.shuffle(lst)
#
# # Создаем DataFrame
# data = pd.DataFrame({'whoAmI': lst})
#
# # Преобразуем в One-Hot Encoding
# one_hot_data = pd.get_dummies(data)
#
# # Показываем первые несколько строк
# one_hot_data.head()




import pandas as pd
import numpy as np

# Создаем список 'lst'
lst = ['robot'] * 10 + ['human'] * 10

# Перемешиваем элементы списка
np.random.shuffle(lst)

# Создаем DataFrame
data = pd.DataFrame({'whoAmI': lst})

# Создаем новые столбцы для каждого уникального значения
unique_values = data['whoAmI'].unique()
for value in unique_values:
    data[value] = (data['whoAmI'] == value).astype(int)

# Удаляем исходный столбец 'whoAmI'
data.drop(columns='whoAmI', inplace=True)

# Показываем первые несколько строк

data.head()