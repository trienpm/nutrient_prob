# importing panda library 
import pandas as pd
import os

dataDir = "/Users/thanhhuongtran/nutrient_prob/FoodNutrients"
listData = os.listdir(dataDir)

finalDataDir = "/Users/thanhhuongtran/nutrient_prob/FinalData"
if not os.path.exists(finalDataDir):
    os.makedirs(finalDataDir)

# readinag given csv file 
# and creating dataframe 
for filename in listData:
    if filename.endswith('.txt'):
        dataframe = pd.read_csv(dataDir + '/' + filename)
        dataframe.to_csv(finalDataDir + '/' + os.path.splitext(filename)[0] + '.csv')
