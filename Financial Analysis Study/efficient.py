import pandas as pd
import matplotlib.pyplot as plt
#from rf import return_porrettfolios, optimal_portfolio
import numpy as np

path='./data/quarters.csv'
stock_data = pd.read_csv(path)
print(stock_data.head())
selected=list(stock_data.columns[1:])
print(selected)
