#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 14:45:23 2019

@author: harun
"""

import numpy as np
import pandas as pd
data= pd.read_csv('mutations_encoded.tsv',sep="\t",encoding='utf-8', lineterminator='\n')
data.columns=['#Feature_AC' ,'Feature_short_label', 'Feature_range(s)',
 'Original_sequence' ,'Resulting_sequence' ,'Feature_type',
 'Feature_annotation' ,'Affected_protein_AC', 'Affected_protein_symbol',
 'Affected_protein_full_name' ,'Affected_protein_organism',
 'Interaction_participants', 'PubMedID', 'Figure_legend', 'Interaction_AC']

elaspicData= pd.read_csv('will_be_classified.csv')
elaspicInteraction = pd.DataFrame()
elaspicInteraction = elaspicData[elaspicData.Type=='interface' ]

homoSapiens=pd.DataFrame()
homoSapiens= data[data.Affected_protein_organism=='9606 - Homo sapiens'] #get homosapiens
homoSapiens.to_csv('homoSapiens.csv', sep='\t', encoding='utf-8')
compare = pd.read_csv('compare.csv')


print('start')


def getDuplicateColumns(df):
    '''
    Get a list of duplicate columns.
    It will iterate over all the columns in dataframe and find the columns whose contents are duplicate.
    :param df: Dataframe object
    :return: List of columns whose contents are duplicates.
    '''
    duplicateColumnNames = set()
    # Iterate over all the columns in dataframe
    for x in range(df.shape[1]):
        # Select column at xth index.
        col = df.iloc[:, x]
        # Iterate over all the columns in DataFrame from (x+1)th index till end
        for y in range(x + 1, df.shape[1]):
            # Select column at yth index.
            otherCol = df.iloc[:, y]
            # Check if two columns at x 7 y index are equal
            if col.equals(otherCol):
                duplicateColumnNames.add(df.columns.values[y])
 
    return list(duplicateColumnNames)
#1  Mutation (MI:0118)

homoSapiens = homoSapiens.drop(columns=getDuplicateColumns(homoSapiens))
print('here')
homoSapiensMutation = homoSapiens[homoSapiens['Feature_type']=='mutation(MI:0118)']

for i in range(len(elaspicInteraction)):
    for k in range(len(homoSapiensMutation)):
        if(elaspicInteraction.iloc[i,1]==homoSapiensMutation.iloc[k,7] and 
           elaspicInteraction.iloc[i,3]==homoSapiensMutation.iloc[k,1]):
            elaspicInteraction.iloc[i,0] = homoSapiensMutation.iloc[k,5]
print('1 homoSapiens mutation')


#2  (MI:2227)
homoSapiensCausing = homoSapiens[homoSapiens['Feature_type']=='mutation causing(MI:2227)']

for i in range(len(elaspicInteraction)):
    for k in range(len(homoSapiensCausing)):
        if(elaspicInteraction.iloc[i,1]==homoSapiensCausing.iloc[k,7] and 
           elaspicInteraction.iloc[i,3]==homoSapiensCausing.iloc[k,1]):
            elaspicInteraction.iloc[i,0] = homoSapiensCausing.iloc[k,5]
print('2 homoSapiensCausing ')


#3 (MI:0119)

homoSapiensDecreasing = homoSapiens[homoSapiens['Feature_type']=='mutation decreasing(MI:0119)']

for i in range(len(elaspicInteraction)):
    for k in range(len(homoSapiensDecreasing)):
        if(elaspicInteraction.iloc[i,1]==homoSapiensDecreasing.iloc[k,7] and 
           elaspicInteraction.iloc[i,3]==homoSapiensDecreasing.iloc[k,1]):
            elaspicInteraction.iloc[i,0] = homoSapiensDecreasing.iloc[k,5]
print('3 homoSapiensDecreasing')

#4 (MI:1130)

homoSapiensDecrRate = homoSapiens[homoSapiens['Feature_type']=='mutation decreasing rate(MI:1130)']


for i in range(len(elaspicInteraction)):
    for k in range(len(homoSapiensDecrRate)):
        if(elaspicInteraction.iloc[i,1]==homoSapiensDecrRate.iloc[k,7] and 
           elaspicInteraction.iloc[i,3]==homoSapiensDecrRate.iloc[k,1]):
            elaspicInteraction.iloc[i,0] = homoSapiensDecrRate.iloc[k,5]
            


print('4 ')

#5  (MI:1133)


homoSapiensDecreasingStrength = homoSapiens[homoSapiens['Feature_type']=='mutation decreasing strength(MI:1133)']

for i in range(len(elaspicInteraction)):
    for k in range(len(homoSapiensDecreasingStrength)):
        if(elaspicInteraction.iloc[i,1]==homoSapiensDecreasingStrength.iloc[k,7] and 
           elaspicInteraction.iloc[i,3]==homoSapiensDecreasingStrength.iloc[k,1]):
            elaspicInteraction.iloc[i,0] = homoSapiensDecreasingStrength.iloc[k,5]
            
print('5 homoSapiensDecreasingStrength')


#6 (MI:0573):
homoSapiensDist = homoSapiens[homoSapiens['Feature_type']=='mutation disrupting(MI:0573)']


for i in range(len(elaspicInteraction)):
    for k in range(len(homoSapiensDist)):
        if(elaspicInteraction.iloc[i,1]==homoSapiensDist.iloc[k,7] and 
           elaspicInteraction.iloc[i,3]==homoSapiensDist.iloc[k,1]):
            elaspicInteraction.iloc[i,0] = homoSapiensDist.iloc[k,5]
            
#7 MI:1129
homoSapiensDistRate = homoSapiens[homoSapiens['Feature_type']=='mutation disrupting rate(MI:1129)']

for i in range(len(elaspicInteraction)):
    for k in range(len(homoSapiensDistRate)):
        if(elaspicInteraction.iloc[i,1]==homoSapiensDistRate.iloc[k,7] and 
           elaspicInteraction.iloc[i,3]==homoSapiensDistRate.iloc[k,1]):
            elaspicInteraction.iloc[i,0] = homoSapiensDistRate.iloc[k,5]
            
print('7 homoSapiensDistRate')

            
            
#8  (MI:1128)
homoSapiensDistStrength = homoSapiens[homoSapiens['Feature_type']=='mutation disrupting strength(MI:1128)']

for i in range(len(elaspicInteraction)):
    for k in range(len(homoSapiensDistStrength)):
        if(elaspicInteraction.iloc[i,1]==homoSapiensDistStrength.iloc[k,7] and 
           elaspicInteraction.iloc[i,3]==homoSapiensDistStrength.iloc[k,1]):
            elaspicInteraction.iloc[i,0] = homoSapiensDistStrength.iloc[k,5]

print('8- homoSapiensDistStrength DONE' )

#9 (MI:0382)
homoSapiensMutInc= homoSapiens[homoSapiens['Feature_type']=='mutation increasing(MI:0382)']

for i in range(len(elaspicInteraction)):
    for k in range(len(homoSapiensMutInc)):
        if(elaspicInteraction.iloc[i,1]==homoSapiensMutInc.iloc[k,7] and 
           elaspicInteraction.iloc[i,3]==homoSapiensMutInc.iloc[k,1]):
            elaspicInteraction.iloc[i,0] = homoSapiensMutInc.iloc[k,5]

print('9- homoSapiensMutInc DONE' )

#10 (MI:1131)

homoSapiensMutIncRate = homoSapiens[homoSapiens['Feature_type']=='mutation increasing rate(MI:1131)']


for i in range(len(elaspicInteraction)):
    for k in range(len(homoSapiensMutIncRate)):
        if(elaspicInteraction.iloc[i,1]==homoSapiensMutIncRate.iloc[k,7] and 
           elaspicInteraction.iloc[i,3]==homoSapiensMutIncRate.iloc[k,1]):
            elaspicInteraction.iloc[i,0] = homoSapiensMutIncRate.iloc[k,5]
            
#11 (MI:2226)
            
homoSapiensMutNoEffect = homoSapiens[homoSapiens['Feature_type']=='mutation with no effect(MI:2226)']

for i in range(len(elaspicInteraction)):
    for k in range(len(homoSapiensMutNoEffect)):
        if(elaspicInteraction.iloc[i,1]==homoSapiensMutNoEffect.iloc[k,7] and 
           elaspicInteraction.iloc[i,3]==homoSapiensMutNoEffect.iloc[k,1]):
            elaspicInteraction.iloc[i,0] = homoSapiensMutNoEffect.iloc[k,5]
            
print('11 homoSapiensMutNoEffect')

#12  (MI:1132)

#mutation increasing strength(MI:1132)

homoSapiensStrength = homoSapiens[homoSapiens['Feature_type']=='mutation increasing strength(MI:1132)']

for i in range(len(elaspicInteraction)):
    for k in range(len(homoSapiensStrength)):
        if(elaspicInteraction.iloc[i,1]==homoSapiensStrength.iloc[k,7] and 
           elaspicInteraction.iloc[i,3]==homoSapiensStrength.iloc[k,1]):
            elaspicInteraction.iloc[i,0] = homoSapiensStrength.iloc[k,5]
            
print('12 mutation increasing strength(MI:1132')







#elaspicInteraction.to_csv('finalLLLL.csv')

print('done')


#homoSapiens=homoSapiens[homoSapiens['#Feature_AC']=='NON']


##homoSapiens.to_csv('final.csv')

final = pd.read_csv('final.csv')



print('done')

#print(homoSapiens.iloc[2,6])
#for i in range(len(homoSapiens)):
#        for k in range(len(elaspicInteraction)):
#            if(homoSapiens.iloc[i,1] == elaspicInteraction.iloc[k,3] and homoSapiens.iloc[i,7] == elaspicInteraction.iloc[k,1]):
#                elaspicInteraction.iloc[k,0]= homoSapiens.iloc[i,6]
#                print('mutation' , homoSapiens.iloc[i,2],elaspicInteraction.iloc[k,3],'protein',homoSapiens.iloc[i,7],elaspicInteraction.iloc[k,1] )
#                print(homoSapiens.iloc[i,5])
#print('done')

#homoSapiens1.iloc[i,2] MUTATİON
            
