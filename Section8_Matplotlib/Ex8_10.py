import matplotlib.pyplot as plt
 
brand_A = [120, 130, 145, 177, 270, 211]
brand_B = [90, 41, 140, 150, 230, 193]
months = ['January','February','March','April','May','June']
 
#plot
plt.bar(x = months, height = brand_A, color = 'blue', label = 'Brand A')
plt.bar(x = months, height = brand_B, color = 'red', label = 'Brand B')
plt.title('Revenue over time')
plt.show()