'''

python分析数据并画出分析图

'''

import numpy as np
import matplotlib.pyplot as plt


def f(t):
    return np.exp(-t) * np.cos(2 * np.pi * t)


def drawOne():
    labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    sizes = [15, 27, 48, 10]
    explode = [0, 0.1, 0, 0]
    plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=False, startangle=90)
    plt.show()


# a = np.arange(0.0, 5.0, 0.02)
# plt.subplot(211)
# plt.plot(a, f(a))
# plt.subplot(2, 1, 2)
# plt.plot(a, np.cos(2 * np.pi * a), 'r--')
# plt.show()

drawOne()
