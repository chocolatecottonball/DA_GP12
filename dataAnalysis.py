import xlrd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

column = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,27,28,29,30,31,32,33,34]
rows = [241]
dA = pd.read_excel('IMVA.xlsx', sheet_name='IMVA')
pd.set_option('display.max_columns', 34)
pd.set_option('display.max_rows', 480)
pd.set_option('display.max_colwidth', 1000)

range = (dA.iloc[262:480, :34])
calc = (dA.iloc[262:480, 1:35].sum(axis=0))
top_3 = (dA.iloc[262:480, 1:35].sum(axis=0).nlargest(3))

# pie chart
label = [' Australia ', ' USA ', ' New Zealand ']  # Data to plot
visitors = [21851470, 12740828, 3449302] # Inserting values of top 3 countries to chart
colors = ['lightblue', 'lightpink', 'purple'] # Colors of pie chart
explode = (0.1, 0, 0) # Largest value will be sliced out
plt.pie(visitors, explode=explode, labels=label, colors=colors, autopct='%1.1f%%', shadow=True, startangle=110 ) # styles for pie chart and % value and angle
plt.title('Top 3 Countries', fontsize= 18) # piechart title
plt.axis('equal') # to make it to a fixed circle
plt.legend(label) # Print out labels at the top right
plt.tight_layout() # to make the pie chart compact
plt.show()

print(range)
print(calc)
print(top_3)