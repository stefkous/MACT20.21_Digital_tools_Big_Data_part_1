# encoding: utf-8

##################################################
# This script shows uses the pandas and matplotlib libraries to produce different kind of plots
# It also combines data from two sources and create multiple plots
# Find extra documentation about data frame here:
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.scatter.html
##################################################
#
##################################################
# Author: Stefania Kousoula
# Copyright: Copyright 2020, IAAC
# Credits: [Institute for Advanced Architecture of Catalonia - IAAC, Advanced Architecture group]
# License:  Apache License Version 2.0
# Version: 1.0.0
# Maintainer: Diego Pajarito
# Email: diego.pajarito@iaac.net
# Status: development
##################################################

# We need to import pandas library as well as the plot library matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

biotopes = pd.read_csv('../Stephania_Kousoula/Poster_Assignment/data/wetland_biotopes.csv', delimiter=',', error_bad_lines=False)


# A simple way to extract data based on column names
slice_add = biotopes[['wet_types', 'area']]

print('My sliced csv')
print(slice_add.head())

# A slice operation based on conditionals
#slice_add_1 = address[address['localite'] == 'Olm']

#print('An example of a sliced dataframe based on conditionals')
#print(slice_add_1.head())