import matplotlib.pyplot as plt
 
sales = [1500.2, 1378, 671, 431, 700]
labels = ['Brand '+str(number) for number in range(1,len(sales)+1)]
 
plt.pie(sales,labels = labels)
plt.show()