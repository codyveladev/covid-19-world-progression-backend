import numpy as np 


class DataHandler: 
    def __init__(self): 
        return 
    '''
    Function: get_data_by_country_iso
    '''
    def get_data_by_country_iso(df, country): 
        country_data_by_iso = {}
        data = df[df['iso_code'] == str(country)]
        
        #get full country for json response
        full_country = data.iat[0, 0]

        #get the columns we want. 
        filtered_data = data[['date', 'total_vaccinations', 'daily_vaccinations', 'people_vaccinated', 'people_fully_vaccinated','total_vaccinations_per_hundred','people_vaccinated_per_hundred', 'people_fully_vaccinated_per_hundred', 'source_name', 'vaccines' ]].fillna('Missing Data')

        #format the data frame into json
        formatted_filtered_data = filtered_data.to_dict('records')
        
        country_data_by_iso['country'] = full_country
        country_data_by_iso['vaccine_data'] = formatted_filtered_data


        return country_data_by_iso