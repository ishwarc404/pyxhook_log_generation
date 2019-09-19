import pandas as pd 
from datetime import datetime,date



def frequency_sorting(time,total_clicks,input_frequency):
	frequency_sorted_clicks  = []
	frequency = input_frequency #10 seconds
	j = 0
	while(j<(len(time)-1)):
		sum_clicks = 0
		start_time  = time[j]
		j = j + 1 #go to the next record
		delta = datetime.combine(date.today(), time[j]) - datetime.combine(date.today(), start_time)

		if(delta.total_seconds() <frequency):
			while(delta.total_seconds() < frequency and (j<len(time)-1)):
				#means until we encounter a change of tab or somenthing
				sum_clicks  = sum_clicks + total_clicks[j]
				j = j + 1
				delta = datetime.combine(date.today(), time[j]) - datetime.combine(date.today(), start_time)
				
			frequency_sorted_clicks.append([start_time,sum_clicks])
		else:
			frequency_sorted_clicks.append([start_time,total_clicks[j-1]])

	return frequency_sorted_clicks



#main
mouse_data_file = 'MouseLog.xlsx'
mouse_dataframe = pd.read_excel(mouse_data_file)

time = mouse_dataframe["Row Labels"][:456]
total_clicks = mouse_dataframe["Mouse Total"][:456]


#we are assuming the time data will always be in datetime.time forma
#function call here
frequency_sorted_clicks = frequency_sorting(time,total_clicks,3) #enter time in seconds

new_dataframe = pd.DataFrame()
new_time  = [i[0] for i in frequency_sorted_clicks]
new_clicks  = [i[1] for i in frequency_sorted_clicks]
new_dataframe["Time"] = new_time
new_dataframe["Total Clicks"] = new_clicks

new_dataframe.to_csv("Frequency_Record.csv")


