#impoting json library to read json file
import json 
#importing matplotlib to plot graph
import matplotlib.pyplot as plt  
# Opening JSON file 
f = open('data.json',) 
  
# returns JSON object as  
# a dictionary 
data = json.load(f)
#list of INR from 2019-01-01 to 2019-01-31 
INR_list_1_31_jan=[]
# Iterating through the json 
# COnverting Data Of INR by date to list 
for i in range (1,31):
  if i <10:#for date 1 to 9
    date="2019-01-0"+str(i)
    if date in data["rates"]:# to check wether date is in the file if not the puting the data of previous date 
      INR_list_1_31_jan.append(data["rates"][str(date)]["INR"])
    else:
      if len(INR_list_1_31_jan)>0:
        INR_list_1_31_jan.append(INR_list_1_31_jan[len(INR_list_1_31_jan)-1])
      
  else:
    date="2019-01-"+str(i)
    if date in data["rates"]:# to check wether date is in the file if not the puting the data of previous date
      INR_list_1_31_jan.append(data["rates"][str(date)]["INR"])
    else:
      if len(INR_list_1_31_jan)>0:
        INR_list_1_31_jan.append(INR_list_1_31_jan[len(INR_list_1_31_jan)-1])


#list of INR from 2019-01-01 to 2019-01-31 
GBP_list_1_31_jan=[]
# COnverting Data Of GBP by date to list
for i in range (1,31):
  if i <10:#for date 1 to 9
    date="2019-01-0"+str(i)
    if date in data["rates"]:# to check wether date is in the file if not the puting the data of previous date 
      GBP_list_1_31_jan.append(data["rates"][str(date)]["GBP"])
    else:
      if len(GBP_list_1_31_jan)>0:
        GBP_list_1_31_jan.append(GBP_list_1_31_jan[len(GBP_list_1_31_jan)-1])
      
  else:
    date="2019-01-"+str(i)
    if date in data["rates"]:# to check wether date is in the file if not the puting the data of previous date
      GBP_list_1_31_jan.append(data["rates"][str(date)]["GBP"])
    else:
      if len(GBP_list_1_31_jan)>0:
        GBP_list_1_31_jan.append(GBP_list_1_31_jan[len(GBP_list_1_31_jan)-1])
print(GBP_list_1_31_jan)


plt.plot(INR_list_1_31_jan,label="INR")
plt.plot(GBP_list_1_31_jan,label="BGP")
# naming the x axis 
plt.xlabel('1 Jan 2019 to 31 Jan 2019') 
# naming the y axis 
plt.ylabel('INR exchange rate against EUR ') 
  
# giving a title to my graph 
plt.title('My first graph!') 
  
# function to show the plot 
plt.legend()#to Discibe line
plt.show()