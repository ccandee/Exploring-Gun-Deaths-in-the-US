
# coding: utf-8

# In[23]:

import csv, datetime
f= open("guns.csv", "r")
data = list(csv.reader(f))
print(data[0:5])
data = data[1:]
print(len(data))


# In[24]:

year_counts = {}
for row in data:
    if row[1] in year_counts:
        year_counts[row[1]] += 1
    else:
        year_counts[row[1]] = 1
print(year_counts)


# In[25]:

dates = []
for row in data:
    dates.append( datetime.datetime(year = int(row[1]),
                              month = int(row[2]), day = 1))
print (dates[0:5])
    


# In[35]:

date_counts = {}
for date in dates:
    if date in date_counts:
        date_counts[date] += 1
    else:
        date_counts[date] = 1


# In[36]:

sex_counts = {}
race_counts = {}
for row in data:
    if row[5] in sex_counts:
        sex_counts[row[5]] += 1
    else:
        sex_counts[row[5]] = 1
    if row[7] in race_counts:
        race_counts[row[7]] += 1
    else:
        race_counts[row[7]] = 1
print(sex_counts)
print(race_counts)


# From the result we can see that in the report, men are more likely to got shoot.
# 

# In[29]:

import csv
f = open("census.csv", "r")
census = list(csv.reader(f))
print (census)


# In[33]:

mapping = {'Asian/Pacific Islander':int(census[1][15])+int(census[1][16]), 
           "Black": census[1][13], "Hispanic" : census[1][12], "Native American/Native Alaskan":
           census[1][14], "White": census[1][11]}
print (mapping)


# In[34]:

race_per_hundredk = {}
for item, value in race_counts.items():
    race_per_hundredk[item] = value/float(mapping[item])*100000
print(race_per_hundredk)


# Seems that black got gun shot more than other races in proportion. What is the couse? Now we analyse together with 
# intent.

# In[43]:

intents = [row[3] for row in data]
races = [row[7] for row in data]
homicide_race_per_hundredk = {}
for i, race in enumerate(races):
    if intents[i] == "Homicide":
        if race not in homicide_race_per_hundredk:
            homicide_race_per_hundredk[race] = 1
        else:
            homicide_race_per_hundredk[race] += 1
print(homicide_race_per_hundredk)
for item, value in homicide_race_per_hundredk.items():
    homicide_race_per_hundredk[item] = value/float(mapping[item])*100000
print(homicide_race_per_hundredk)


# oh! the result is startling! Black has high homicide rate, which is really a big concern.  

# In[ ]:



