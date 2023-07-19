import pandas
from itertools import islice, groupby
import openpyxl


def search_keywords(input_string, dict):
    matched_phrases = []
    #print(dict)
    for keyword,phrases in dict.items():
        #for phrase in phrases:
            #print(phrase.strip)
            if keyword in input_string:
                #we dont want duplicates
                if keyword not in matched_phrases:
                    matched_phrases.append(keyword)
    return matched_phrases



dataframe = openpyxl.load_workbook("Log_Data.xlsx")
worksheet = dataframe.active
#CHANGE TO 1 FOR HACKATHON
index  = 0
primarylist = []
commandlist = []

prev_index = None
#iterate through our rows
for row in islice(worksheet.iter_rows(), 1, None):
    #if the row has a value and isnt None
    if row[2].value is not None:
        stringt = row[2].value
        #the format of the string is "0 show ap debug radio-stats X | include MCS"
        current_index = int(stringt[0])
        #we set prev index to our current
        if prev_index is None:
            prev_index = current_index
        #if the current is the same as the prev meaning if its 0 = 0, we append it to a list with commands
        if current_index == prev_index:
            commandlist.append(stringt)
        else: #else meaning its not the same, we are done with that commandlist so we push it to the primarylist, thatll be a list of lists
            primarylist.append(commandlist)
            commandlist = [stringt]
            prev_index = current_index #and we set previndex to the current

# Append the last commandlist if there are any remaining commands
if commandlist:
    primarylist.append(commandlist)


list_of_lists = []
colindex = 1
#for row in worksheet.iter_rows():
index = 1
for row in islice(worksheet.iter_rows(), 1, None):
    temp = ""
    
    if row[1].value is not None:

        database_string = row[1].value
        #split by the string and add it to list
        split_items = database_string.split(',')
        list_of_lists.append(split_items)
        #print(row[2].value)
        #temp = row[2].value
        #print(temp)
    #in our excel sheet there are values where row[1] is None such as A3 and A5
    if row[2].value is not None:
        #print(row[2].value)
        temp = row[2].value
        #print(temp)

#print(list_of_lists)
#print(primarylist)

mydict = {}

listcount = 0
for list in list_of_lists:
    counter = 0
    
    for item in list:
        
        #print(counter)
        #rint(item,listcount)

        #print(item, primarylist[counter])
        mydict[item] = primarylist[listcount]
        counter +=1
    listcount +=1

#print the command list with lists
#print(primarylist)


print(mydict)
input_string = " Performance Deauth and disconnect internt "
#print(search_keywords(input_string, dict))
listofKeywords = search_keywords(input_string, mydict)
print(listofKeywords)
#we iterate the list of keywords and search for them in our dictionary
for word in listofKeywords:
    counter = 1
    if word in mydict:
        #print(len(mydict[word]) )
        #print( "The keyword is: ", word , "The commands are " , mydict[word])
        
        commandstring = mydict[word]
        print("Use these commands: ",word)
        print("")
        for command in commandstring:
            print(command, counter)
            counter += 1
    print("")


        
        

