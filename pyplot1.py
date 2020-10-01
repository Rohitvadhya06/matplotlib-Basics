from matplotlib import pyplot as plt

#print(plt.style.available)
#plt.style.use('fivethirtyeight')
plt.style.use('ggplot')

#Median rohit Developer Salaries by Age
dev_x = [25 , 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]

#plt.plot(dev_x, dev_y, 'k--', label='All Devs')
#plt.plot(dev_x, dev_y, color='k', linestyle='--', marker='.', label='All Devs')
plt.plot(dev_x, dev_y, color='#444444', linestyle='--', label='All Devs')

#Median Python Developer Salaries by Age
py_dev_x = [25 , 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]

plt.plot(py_dev_x, py_dev_y, label='Python')
#plt.plot(py_dev_x, py_dev_y, 'b', label='Python')
#plt.plot(py_dev_x, py_dev_y, color='b', marker='o', label='Python')
#plt.plot(py_dev_x, py_dev_y, color='#5a7d9a', label='Python')
#plt.plot(py_dev_x, py_dev_y, color='#5a7d9a', linewidth=3, label='Python')

#Median JavaScript Developer Salaries by Age
js_dev_x = [25 , 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68746, 68748, 74583]

plt.plot(js_dev_x, js_dev_y, label='JavaScript')
#plt.plot(js_dev_x, js_dev_y, color='#adad3b', label='JavaScript')
#plt.plot(js_dev_x, js_dev_y, color='#adad3b', linewidth=3, label='JavaScript')


plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Median Salary (USD) by Age')

plt.legend()

#plt.legend(['All Devs', 'Python'])

#plt.grid(True)
#plt.tight_layout()
plt.show()
