import pandas as pd
import numpy as np
dataPath = "C:\\Users\\Nick\\Google Drive\\NorthwestLaptop\\seniorYearCollege\\bigData\\bitbucketRepos\\mapReduceChoseDatasetPractice\\Us_Accidents_Dec19Shortened.csv"
data = pd.read_csv(dataPath)
##'Start_Time','End_Time','City','State','Timezone','Visibility(mi)','Temperature(F)','Humidity(%)','Wind_Speed(mph)','Precipitation(in)','Weather_Condition'
dataSplits = np.array_split(data,4)
data = dataSplits[0]
data.to_csv("C:\\Users\\Nick\\Google Drive\\NorthwestLaptop\\seniorYearCollege\\bigData\\bitbucketRepos\\mapReduceChoseDatasetPractice\\Us_Accidents_Dec19.csv")



"""
f = open("C:\\Users\\Nick\\Google Drive\\NorthwestLaptop\\seniorYearCollege\\bigData\\bitbucketRepos\\mapReduceChoseDatasetPractice\\Us_Accidents_Dec19.txt","a")
print("writing")
try:
    f.writelines(['\n', str(data['ID']), ' ', str(data['TMC']), ' ', str(data['Severity']), ' ', str(data['Start_Time']), ' ', str(data['End_Time']), ' ', str(data['City']), ' ', str(data['County']), ' ', str(data['State']), ' ', str(data['Zipcode']), ' ', str(data['Timezone']), ' ', str(data['Visibility(mi)']), ' ', str(data['Temperature(F)']), ' ', str(data['Humidity(%)']), ' ', str(data['Wind_Speed(mph)']), ' ', str(data['Precipitation(in)']), ' ', str(data['Weather_Condition'])])
except Exception as e:
    print(e)
try:
    f.close()
except Exception as e:
    print(e)"""