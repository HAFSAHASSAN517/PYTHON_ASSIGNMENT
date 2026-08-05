import pandas as pd
import numpy as np
data=(1,2,3,4,5,6,7)
def calculate_mean(data):
    
    
    return float(np.mean(data))
     
def calculate_median(data):
    
    return float(np.median(data))
    
def REPORT(data):
    
 mean_value = calculate_mean(data)
 median_value = calculate_median(data)
 print("----here is the generated report of the data -----")
 print(f"mean value of data is : {mean_value}")
 print(f"median value of data is : {median_value}")    
          