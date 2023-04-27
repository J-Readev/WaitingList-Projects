#Pandas Needed.
import pandas as pd

#Need file path. Unable to figure out how to do this differently.
Whole_Spreadsheet = pd.read_excel(r"C:\Users\joshl\Desktop\Work\Portfolio\Python\WaitingListProject\Learning_Activities_Waiting_List.xlsx")

#Whole Spreadsheet if needed.
#print(Whole_Spreadsheet)

Course_Title = [0]


#Counting Number on WL, using 2 columns.
df = pd.read_excel(r"C:\Users\joshl\Desktop\Work\Portfolio\Python\WaitingListProject\Learning_Activities_Waiting_List.xlsx",usecols =['Course Title','Forename'])

#Renamed Forename to 
dfRenamed = df.rename(columns={'Forename' : 'Number On Waiting List'}, inplace=True)

#print(df.groupby(['Course Title']).count())

#Defining.
WLNum = df.groupby(['Course Title']).count()

#Writing to notepad file. Needs to convert Dataframe to string.
with open('WaitingListNumbers.txt','w') as f:
    f.write(str(WLNum))
    f.write("\n"+"\n"+"Listed above is the current waiting list. Please see course titles followed by the number of participants on waiting list.")


