# encoding: utf-8

##################################################
# This script shows uses the pandas and matplotlib libraries to produce different kind of plots
# It also combines data from two sources and create multiple plots
# Find extra documentation about data frame here:
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.scatter.html
##################################################
#
##################################################
# Author: Stephania Kousoula
# Copyright: Copyright 2020, IAAC
# Credits: [Institute for Advanced Architecture of Catalonia - IAAC, Advanced Architecture group]
# License:  Apache License Version 2.0
# Version: 1.0.0
# Maintainer: Diego Pajarito
# Email: stefania-maria.kousoula@students.iaac.net
# Status: development
##################################################

# We need to import pandas library as well as the plot library matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

biotopes_south = pd.read_csv('../Stephania_Kousoula/Poster_Assignment/code/south_corridor_wetlands.csv', delimiter=',', error_bad_lines=False)


# Slicing the two columns I am interested in
slice_wet_south = biotopes_south[['Area', 'wet_types']]
print(slice_wet_south)

#Calculate total area of wetlands
tot_south_wet_area = slice_wet_south['Area'].sum()
print(tot_south_wet_area)


# A slice operation based on conditionals for each wet type
slice_shallow_south = slice_wet_south[slice_wet_south['wet_types'] == 'Shallow marshes']
print(slice_shallow_south.head())

slice_mead_south = slice_wet_south[slice_wet_south['wet_types'] == 'Wet meadows']
print(slice_mead_south.head())

slice_fen_south = slice_wet_south[slice_wet_south['wet_types'] == 'Fens']
print(slice_fen_south.head())

slice_deep_south = slice_wet_south[slice_wet_south['wet_types'] == 'Deep marshes']
print(slice_deep_south.head())



#Calculate the total area of each wet type
shallow_tot_south_area = slice_shallow_south['Area'].sum()
print(shallow_tot_south_area)

mead_tot_south_area = slice_mead_south['Area'].sum()
print(mead_tot_south_area)

fen_tot_south_area = slice_fen_south['Area'].sum()
print(fen_tot_south_area)

deep_tot_south_area = slice_deep_south['Area'].sum()
print(deep_tot_south_area)


# Histogram and normal distribution
sns.distplot(slice_shallow_south['Area'])
plt.show()

sns.distplot(slice_mead_south['Area'])
plt.show()

sns.distplot(slice_fen_south['Area'])
plt.show()

sns.distplot(slice_deep_south['Area'])
plt.show()



#Calculate the percentage of each wetland type to the total area
per_shallow_south =(shallow_tot_south_area/tot_south_wet_area) * 100
print(per_shallow_south)

per_mead_south =(mead_tot_south_area/tot_south_wet_area) * 100
print(per_mead_south)

per_fens_south =(fen_tot_south_area/tot_south_wet_area) * 100
print(per_fens_south)

per_deep_south =(deep_tot_south_area/tot_south_wet_area) * 100
print(per_deep_south)


#Create a pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Shallow Marshes', 'Wet Meadows', 'Fens', 'Deep Marshes'
sizes = [per_shallow_south, per_mead_south, per_fens_south, per_deep_south]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()


