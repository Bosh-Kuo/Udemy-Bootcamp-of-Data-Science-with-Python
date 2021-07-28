import matplotlib.pyplot as plt
 
sales = [1500.2, 1378, 671, 431, 700]
labels = ['Brand '+str(number) for number in range(1,len(sales)+1)]
explode = (0.1, 0.1, 0, 0, 0)
 
plt.pie(sales, labels = labels, autopct = '%1.2f%%', explode = explode, shadow = True)
plt.legend(labels, loc = 'upper left')
plt.show()