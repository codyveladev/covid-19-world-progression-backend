import pandas as pd
import json
from dh import DH

dh = DH()
df = pd.read_csv('vaccine_data/country_vaccinations.csv')

def get_data(country):
    return dh.get_data_by_country_iso(df, country)

def get_top_ten():
    #get countries based on name
    data = df[['country']].drop_duplicates().dropna()

    #format dataframe into dictionary
    countries = data.to_dict('records')


    #to store all list of countries
    list_of_countries = []

    #store all countries
    for i in range(len(countries)):
        list_of_countries.insert(i, countries[i]['country'],)

    #get the total number of vaccines per country
    countries_with_max = {}
    for country in range(len(list_of_countries)):
        data = df[df['country'] == list_of_countries[country]]
        curr_country = data['total_vaccinations']
        most = curr_country.max()
        countries_with_max[list_of_countries[country]] = most


   #format dict into dataframe to be sorted
    tes = pd.DataFrame(list(countries_with_max.items()), columns=['Country', 'Max'])
    
    #sort the data
    sorted_df = tes.sort_values(by="Max", ascending=False)


    #format the response into nice json 
    top_ten_unformatted = sorted_df.head(10).to_dict('records')
    response_dict = {}
    response_dict['totals'] = top_ten_unformatted

    return response_dict



def get_types_of_vaccine_used_in_countries():
    #get countries based on name
    data = df[['vaccines']].drop_duplicates().dropna()

    vaccines = data.to_dict('records')

    names_of_vaccines = set()
    list_of_vaccines = []

    #store all vaccines
    for i in range(len(vaccines)):
        list_of_vaccines.insert(i, vaccines[i]['vaccines'],)
    
    for i in range(len(list_of_vaccines)):
        #set variable names
        current_word = list_of_vaccines[i]
        comma = ','

        #check if word has a comma
        if current_word.find(comma) != -1:
            #split the string based on commas
            current_word_split_by_commas = current_word.split(", ")

            #iterate through the split words
            for index in range(len(current_word_split_by_commas)):
                current = current_word_split_by_commas[index]
                names_of_vaccines.add(current)
        else: 
            names_of_vaccines.add(current_word)
        
    return list(names_of_vaccines)

def get_count_of_vaccines_in_countries():
    #get names of vaccines anm
    names = get_types_of_vaccine_used_in_countries()
    vaccine_with_count = {}

    #get the data of country and vaccines
    data = df[['country','vaccines']].drop_duplicates().dropna()
    vaccines = data.to_dict('records')

    #initialize dictionary with 0 values.
    for i in range(len(names)):
        vaccine_with_count[names[i]] = 0

    for i in range(len(names)):
        for j in range(len(vaccines)):
            if vaccines[j]['vaccines'].find(names[i]) != -1:
                current_count = vaccine_with_count[names[i]]
                vaccine_with_count[names[i]] = current_count + 1
    
    return vaccine_with_count


def find_vaccine_country():
    #get the data of country and vaccines
    data = df[['country','vaccines']].drop_duplicates().dropna()
    vaccines = data.to_dict('records')
    to_search = 'Pfizer/BioNTech'

    count = 0 
    for i in range(len(vaccines)):
        if vaccines[i]['vaccines'].find(to_search) != -1:
            count = count + 1
            print(vaccines[i], count)


