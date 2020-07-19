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


#Code for the current rate for INR and GBP on the graph itself.
#opening the latest rates file
latest_data= open('latest-rates.json',)
data = json.load(latest_data)

INR_Latest_rate=[data["rates"]["INR"]]
GBP_Latest_rate=[data["rates"]["GBP"]]




fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
fig.suptitle('A tale of 3 subplots')

#subgraph for INR 
ax1.plot(INR_list_1_31_jan, 'o-')
ax1.set_ylabel('INR rate against EUR')
#Sub Graph for BGP
ax2.plot(GBP_list_1_31_jan, '.-')
ax2.set_xlabel('1 Jan 2019 to 31 Jan 2019')
ax2.set_ylabel('GBP rate against EUR')

#Sub graph for current rate against EUR
ax3.plot(INR_Latest_rate, 'o-', label="INR")  
ax3.plot(GBP_Latest_rate, '.-', label="GBP")   
ax3.set_xlabel('CURRENT Rate')
ax3.set_ylabel('Current INR and GBP rate against EUR')
ax3.legend()
# function to show the plot
plt.show()