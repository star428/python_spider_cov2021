import pandas as pd
import pygal
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('data.csv',encoding='utf-8')

time = df['时间']
newConfirmed = df['新增确诊人数']
newDead = df['新增死亡人数']
newSuspected = df['新增疑似人数']
newCured = df['新增治愈人数']

nowConfirmed = df['现有确诊人数']
sumCure = df['累计治愈人数']
sumDead = df['累计死亡人数']
sumConfirmed = df['累计确诊人数']
nowSuspected = df['现有疑似人数']
sumCloseContant = df['累计密切接触者']

# print(df)
# 时间             1.24
# 新增确诊人数       444.00
# 新增死亡人数        16.00
# 新增疑似人数      1118.00
# 新增治愈人数         0.00
# 现有确诊人数      1287.00
# 累计治愈人数        38.00
# 累计死亡人数        41.00
# 累计确诊人数      1287.00
# 累计密切接触者    15197.00
# 现有疑似人数      1965.00
#
# line_chart = pygal.Line()
# line_chart.title = '新增数目统计图'
# line_chart.x_labels = list(time)
# line_chart.add('新增确诊人数', list(newConfirmed))
# line_chart.add('新增死亡人数',  list(newDead))
# line_chart.add('新增疑似人数',  list(newSuspected))
# line_chart.add('新增治愈人数',  list(newCured))
# line_chart.render_to_png('line_chart.png')
#
# line_chart = pygal.Line()
# line_chart.title = '累计数目统计图'
# line_chart.x_labels = list(time)
# line_chart.add('现有确诊人数', list(nowConfirmed))
# line_chart.add('累计治愈人数',  list(sumCure))
# line_chart.add('累计死亡人数',  list(sumDead))
# line_chart.add('累计确诊人数',  list(sumConfirmed))
# line_chart.add('现有疑似人数',  list(nowSuspected))
# # line_chart.add('累计密切接触者',  list(newCured))
#
# line_chart.render_to_png('line_chart_2.png')

x = np.array(list(range(len(time))))

# Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
fig, ax = plt.subplots()  # Create a figure and an axes.
# ax.plot(x, newConfirmed, label='newConfirmed')  # Plot some data on the axes.
# ax.plot(x, newDead, label='newDead')  # Plot more data on the axes...
# ax.plot(x, newSuspected, label='newSuspected')  # ... and some more.
# ax.plot(x, newCured, label='newCured')
ax.plot(x, nowConfirmed, label='nowConfirmed')
ax.plot(x, sumCure, label='sumCure')
ax.plot(x, sumDead, label='sumDead')
ax.plot(x, sumConfirmed, label='sumConfirmed')
ax.plot(x, nowSuspected, label='nowSuspected')
ax.plot(x, sumCloseContant, label='sumCloseContant')
ax.set_xlabel('x label')  # Add an x-label to the axes.
ax.set_ylabel('y label')  # Add a y-label to the axes.
ax.set_title("sum map")  # Add a title to the axes.
ax.legend()  # Add a legend.
plt.show()
